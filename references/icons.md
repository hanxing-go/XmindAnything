# Icon Theme Reference for XmindAnything
# 图标方案：Unicode Emoji 嵌入标题文字
#
# ⚠️ PNG 图片注入 (image 字段) 方案已废弃
# 原因：无论 xmind SDK 还是手动注入 content.json + manifest.json，XMind 均报文件损坏
# 可能原因：XMind Zen JSON 格式的主题(theme)与 image 属性存在兼容性问题
# 
# 未来研究方向：
#   1. 在 XMind 桌面端手动添加图片后导出，逆向 content.json 结构
#   2. 探索 XMind 内置 Marker 系统（priority/smiley/flag/star 等）
#   3. 考虑生成旧版 XMind 8 XML 格式（.xmind 兼容）
#
# 当前方案：emoji 嵌入节点文字，简单可靠，XMind 天然支持

## 🎓 Academic Papers / 学术论文

| 场景 | 图标 | 适用节点 |
|------|:---:|------|
| Title/Info | 📌 | 论文信息、作者 |
| Motivation | 🎯 | 研究动机、问题定义 |
| Background | 📖 | 背景介绍、相关工作 |
| Method | ⚙️ | 方法、架构、算法 |
| Key Design | 🧠 | 核心设计、创新点 |
| Experiments | 🔬 | 实验设置、数据集 |
| Results | 📊 | 实验结果、性能数据 |
| Comparison | 📈 | 对比分析、消融实验 |
| Defense | 🛡️ | 防御、安全性、鲁棒性 |
| Insight | 💡 | 核心洞察、发现 |
| Limitation | ⚠️ | 局限性、不足 |
| Conclusion | 📝 | 总结、结论 |
| Contribution | ✨ | 贡献汇总 |

## 🏗️ Technical Projects / 技术项目

| 场景 | 图标 | 适用节点 |
|------|:---:|------|
| Architecture | 🏗️ | 架构设计、系统概述 |
| Module | 🧩 | 模块、组件、包 |
| API/Interface | 🔌 | 接口、API |
| Pipeline | 🔄 | 流水线、流程 |
| Config | ⚙️ | 配置、参数 |
| Performance | ⚡ | 性能、优化 |
| Deployment | 🚀 | 部署、发布 |
| Testing | 🧪 | 测试、验证 |
| Data | 📦 | 数据、存储 |
| Security | 🔒 | 安全、权限 |

## 📝 General Documents / 通用文档

| 场景 | 图标 | 适用节点 |
|------|:---:|------|
| Goal | 🎯 | 目标、目的 |
| Features | ✨ | 亮点、特性 |
| Structure | 📋 | 结构、目录 |
| Steps | 🔢 | 步骤、流程 |
| Note | 💬 | 备注、提示 |
| Warning | ⚠️ | 注意事项 |
| Example | 💡 | 示例、演示 |
| Reference | 🔗 | 参考、链接 |
| Timeline | ⏱️ | 时间线、计划 |

## 🎨 Design / 设计类

| 场景 | 图标 | 适用节点 |
|------|:---:|------|
| Visual | 🎨 | 视觉设计、UI |
| Color | 🌈 | 配色、主题 |
| Layout | 📐 | 布局、排版 |
| Typography | 🔤 | 字体、文字 |
| Interaction | 👆 | 交互、手势 |
| Animation | 🎬 | 动画、动效 |

## 📊 Business / 商业类

| 场景 | 图标 | 适用节点 |
|------|:---:|------|
| Revenue | 💰 | 收入、盈利 |
| Growth | 📈 | 增长、趋势 |
| Strategy | ♟️ | 策略、规划 |
| Team | 👥 | 团队、组织 |
| Market | 🎯 | 市场、定位 |
| Risk | ⚠️ | 风险、挑战 |

## 新增：进阶图标集 (v2.3)

用于更精准的语义表达，按需选用：

| 场景 | 图标 | 含义 |
|------|:---:|------|
| Code | 💻 | 代码、编程 |
| Algorithm | 🔢 | 算法、计算 |
| Network | 🌐 | 网络、通信 |
| Database | 🗄️ | 数据库、存储 |
| Cache | ⚡ | 缓存、加速 |
| Queue | 📬 | 消息队列 |
| Log/Monitor | 📡 | 日志、监控 |
| Schedule | ⏰ | 调度、定时 |
| Lock | 🔐 | 锁、同步 |
| Error | ❌ | 错误、异常 |
| Thread | 🧵 | 线程、并发 |
| Memory | 💾 | 内存、存储 |
| Compile | 🔨 | 编译、构建 |
| Package | 📦 | 打包、分发 |
| Config File | 📄 | 配置文件 |
| Protocol | 📜 | 协议、规范 |
| Cert/SSL | 🛡️ | 证书、安全 |
| Docker/Container | 📦 | 容器化 |
| K8s/Orchestra | ☸️ | 编排 |
| CI/CD | 🔄 | 持续集成 |

## Usage Rules

1. **只给关键节点加图标** — 不是每个节点都加，否则视觉疲劳
2. **优先加在层级切换处** — 主分支和重要的子分支顶部
3. **同一层级图标风格统一** — 不要混用不同类别的图标
4. **避免红色标志** — 🔴🛑⛔ 等负面图标会让脑图显得警报警惕
5. **每层图标不超过 60%** — 留一些无图标节点做呼吸感

## 🧪 图片注入实验总结 (2026-05-15)

**已尝试方案 (全部失败，XMind 报文件损坏)：**
| # | 方案 | 结果 |
|---|------|:--:|
| 1 | 手写 content.json + image string | ❌ 结构无效 |
| 2 | xmindmark + image string + resources base64 | ❌ 损坏 |
| 3 | xmindmark + image object + resources base64 | ❌ 损坏 |
| 4 | XMind 官方 SDK (xmind npm) | ❌ 损坏 |
| 5 | xmindmark + image object + resources PNG + manifest | ❌ 损坏 |

**关键发现：**
- PNG 必须作为独立文件存入 ZIP，不能 base64 内联
- manifest.json 必须登记所有文件
- image 字段格式应为 `{"src":"xap:resources/xxx.png","width":"24","height":"24"}`
- 即使以上全部满足，XMind 仍然报损坏 — 说明还有其他结构约束未满足

**下一步：** 需要从 XMind 桌面端导出一个包含图片的 .xmind 文件，完整逆向其 content.json 结构，找出缺失的关键字段。
