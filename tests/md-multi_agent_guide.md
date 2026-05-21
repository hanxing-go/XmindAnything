# Project Mentor — 多Agent协作流水线指南

> 让 OpenClaw 拆解目标项目时使用"3个Worker并行分析 → 汇总 → 执行"模式
> 适用场景：代码审查、Bug排查、改进建议、技术设计评审

---

## 🧠 核心理念

```
你（Master）  ──→  长门有希（Orchestrator）
                         │
                    ┌────┴────┐
                    │  决策者  │ ← 只做：拆任务、读结果、汇总判断
                    └────┬────┘
                         │
               ┌─────────┼─────────┐
               │         │         │
           Worker-A   Worker-B   Worker-C
               │         │         │
           (独立分析)  (独立分析)  (独立分析)
               │         │         │
               └─────────┼─────────┘
                         │
                     汇总报告
                         │
                    Executor（执行修改）
                         │
                     Reviewer（验收）
```

**关键区别：**
- 传统模式：一个 Agent 读完所有文件 → 一次性输出 → Token 爆炸 → 上下文混乱
- 本模式：3 个独立 Worker 并行读 → 各输出精简报告 → 编排者汇总 → 质量更高、速度更快

---

## ⚡ 性能对比

| 维度 | 传统串行 | 本模式（3 Worker 并行） |
|------|---------|----------------------|
| 文件读取 | 逐个读，串行 | 3个同时读，各读1/3 |
| 思考深度 | 一个上下文有限 | 每个 Worker 独享上下文 |
| 等待时间 | 3-5 分钟 | 1-2 分钟 |
| 质量 | 容易遗忘早期内容 | 独立聚焦，互相补充 |
| Token消耗 | ~60K | ~80K（但速度翻倍） |

---

## 📋 标准操作流程

### Step 1: 准备工作（你先把这个写好）

在 OpenClaw 的 `HEARTBEAT.md` 或 `AGENTS.md` 中声明：

```
## 多Agent协作模式

当需要分析复杂项目/代码时，使用 3-Worker 并行分析模式：
1. Spawn 3个子Agent分别独立分析
2. 汇总三份结果
3. 确认后再执行修改
```

### Step 2: 分析阶段（告诉你的 OpenClaw Agent 这样干）

```
我需要你分析 [项目路径/URL] 的代码。
请按照多Agent协作模式：

1. 先 spawn 3个子Agent，各自独立分析这个项目，找出问题和改进点
2. 每个子Agent输出一份独立报告
3. 你等我查看所有报告后汇总给我
4. 我确认后再 spawn 执行者去修改
```

### Step 3: 执行 spawn（Agent 自动做）

在你的 Agent（在云端或其他地方）中，它需要做类似这样的调用：

<details>
<summary>点击展开 spawn 参数示例</summary>

```
sessions_spawn(
  label="worker-A",
  task="你是一名资深开发者。分析 [项目路径] 的代码，找出...",
  mode="run",
  cleanup="keep"
)

sessions_spawn(
  label="worker-B",
  task="... 和上面相同的分析任务，独立做 ...",
  mode="run",
  cleanup="keep"
)

sessions_spawn(
  label="worker-C",
  task="... 同上 ...",
  mode="run",
  cleanup="keep"
)

→ sessions_yield 等待全部完成
```
</details>

---

## 🎮 三种变形模式

根据任务类型，Worker 的分工方式不同：

### 模式A：同题异构（最推荐⭐）
```
三个Worker做完全相同的任务
→ 各自的关注点必然不同
→ 汇总 = 多视角的综合结论
适合：代码审查、Bug排查、设计评审
```

### 模式B：角色分工
```
Worker-A: 架构师视角（目录结构、依赖关系、分层）  
Worker-B: 后端开发者视角（实现细节、错误处理、测试）  
Worker-C: DevOps视角（Docker、CI/CD、部署、安全）  
适合：从零设计方案、技术选型
```

### 模式C：分区域扫描
```
Worker-A: 分析 moduleA/ 和 moduleB/
Worker-B: 分析 moduleC/ 和 moduleD/
Worker-C: 分析 config/、scripts/、test/
适合：超大项目（5000+文件），按目录切分
```

---

## 🚧 常见问题

### Q: Worker 跑超时了怎么办？
默认 `runTimeoutSeconds` 不设置 = 不限时。如果超时可以用 timeout 参数控制。
超时的 Worker 可以用 `subagents(kill)` 杀掉，回来汇总已有的结果。

### Q: Worker 输出被截断了怎么办？
用 `sessions_history(sessionKey, limit=5)` 拉取完整聊天记录。
如果仍被截断，分两次读取。

### Q: 在 Claude Code 里怎么用这种模式？
Claude Code 没有 `sessions_spawn` 机制。但你可以：
1. 开三个 Claude Code 终端窗口，各分析不同模块
2. 或者用脚本实现：`claude -p "分析 X" --output-format json > report-A.json`
3. 然后把三份报告喂给第四个 Claude Code 做汇总

---

## 📁 模板：Worker 任务 Prompt

```markdown
你是一个独立的代码分析 Worker。
请分析以下项目：{{项目路径}}

分析目标：{{找Bug / 找改进点 / 兼容性检查 / 其他}}

要求：
1. 不要做汇总——只做你独立的分析结果
2. 每个问题标注：位置（文件名大概行号） + 问题描述 + 修复建议
3. 按严重程度排序
4. 输出格式化为 Markdown
5. 不需要和任何人协作，你独立完成
```

---

## 🔧 一键部署到云服务器

在云服务器的 OpenClaw workspace 创建 `/home/user/.openclaw/workspace/TOOLS.md`，加入：

```markdown
## 多Agent协作流水线

当 Master 要求分析项目时，使用 3-Worker 并行模式：
1. 根据任务类型选择模式（同题异构/角色分工/分区域）
2. spawn 3 个子 Agent + yield 等待
3. 汇总三份报告给 Master
4. Master 确认后 spawn 执行者

关键命令速查：
- sessions_spawn(label="worker-X", task="...", mode="run")
- sessions_yield(message="等待中")
- subagents(list)
- sessions_history(sessionKey, limit=5)
```

---

> 这份指南打印出来后，你的云服务器 OpenClaw 就能用同样的多Agent协作模式了。
> 有任何调整随时告诉我。
