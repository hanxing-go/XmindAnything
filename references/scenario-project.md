# Scenario: Project / Directory → Architecture Mind Map

输入为 GitHub 开源项目 URL 或本地目录路径时使用本场景。

---

## 子场景 A：开源项目 → 架构脑图

### Step A1: 获取项目

```bash
# GitHub URL → 浅克隆
python3 scripts/clone_project.py https://github.com/owner/repo 2>&1

# 本地路径 → 直接使用
cp -r /path/to/project /tmp/proj
```

**GitHub URL 不完整时**：用户给 `owner/repo` 而非完整 URL，自动补全为 `https://github.com/owner/repo`。

**大项目警告**：`git clone --depth 1` 失败或目录 >500 文件时，告知用户并建议仅转换 README。

### Step A2: 提取 README（核心信息来源）

```bash
# 按优先级查找 README
for f in README.md README.rst README README.txt README.org; do
  [ -f "/tmp/proj/$f" ] && { README_FILE="$f"; break; }
done
```

从 README 提取四部分信息：
1. **项目名称** — 第一个 `#` 标题
2. **简介** — 标题后的第一段文字（1-2 句）
3. **核心功能列表** — `## Features` 下的列表项，或散落在简介附近的动词短语
4. **快速开始** — `## Quick Start / Getting Started / Installation` 下的关键命令

### Step A3: 扫描目录结构

```bash
# 排除构建产物和依赖
tree -L 2 --dirsfirst -I "node_modules|__pycache__|target|build|dist|.git|vendor|*.pyc" /tmp/proj
```

识别：
- **源码目录**：`src/`, `lib/`, `pkg/`, `internal/`, 包名目录
- **文档目录**：`docs/`, `doc/`, `examples/`
- **配置目录**：`config/`, `configs/`, `deploy/`, `docker/`
- **测试目录**：`tests/`, `test/`, `__tests__/`, `spec/`

### Step A4: 扫描构建文件

找到对应构建文件后，用 `head -30` + `grep` 提取关键信息：

| 构建文件 | 信息提取 |
|----------|---------|
| `go.mod` | module 名 + Go 版本 + `require` 段的前几个依赖 |
| `package.json` | `name` + `devDependencies` 关键依赖 + `scripts` |
| `requirements.txt` / `pyproject.toml` | 前几个核心依赖 |
| `build.gradle` / `pom.xml` | 项目名 + Spring Boot / Gradle 版本 |
| `Cargo.toml` | `[package]` name + `[dependencies]` 核心依赖 |
| `Makefile` / `CMakeLists.txt` | 仅标注构建系统类型 |

### Step A5: 组装 XMindMark

```
中心主题 = 项目名 (从 README 提取)

主分支：
  - 📖 项目简介
      * (README 提取的 1-2 句简介)
      * (一句话总结项目定位)

  - 🏗️ 核心架构
      * 源码结构: (tree 识别的主源码目录)
      * 模块划分: (用关键词概括，如 "core" / "server" / "client" / "api")
      * 构建系统: (Go modules / Maven / npm / etc.)
      * 项目布局: (tree -L 1 的目录列表)

  - 🔧 核心功能
      * (README Features 提取，每项一个子节点)

  - 🛠️ 技术栈
      * 语言: (go.mod/package.json 推断)
      * 框架: (pom.xml/package.json 关键依赖)
      * 核心依赖: (前 3-5 个)

  - 🚀 快速开始
      * (README Quick Start 提取的关键命令)

  - 📊 项目规模
      * 文件数: find /tmp/proj -type f ! -path '*/.git/*' | wc -l
      * 代码行数: find /tmp/proj -name "*.py" (或其他) | xargs wc -l | tail -1
      * 测试文件数: find /tmp/proj -name "*test*" -o -name "*spec*" | wc -l

  - 🔗 关键信息 [B] (boundary)
      * 仓库地址: (GitHub URL)
      * 许可证: (从 LICENSE 文件读取前 3 行)
      * 作者: (从 README 或 AUTHORS 文件提取)
```

**节点数控制**：主分支 ≤9 个，总节点 ≤80 个。

---

## 子场景 B：学习资料集 → 主题脑图

输入为包含多个文档文件的目录。

### Step B1: 递归扫描

```bash
# 扫描所有可处理的文件，排除隐藏文件和特殊目录
find /tmp/study/ -type f \
  ! -path '*/.git/*' ! -path '*/node_modules/*' ! -path '*/__pycache__/*' \
  ! -name '.*' \
  \( -name '*.pdf' -o -name '*.md' -o -name '*.docx' -o -name '*.pptx' \
     -o -name '*.xlsx' -o -name '*.csv' -o -name '*.yaml' -o -name '*.yml' \
     -o -name '*.json' -o -name '*.txt' -o -name '*.rst' -o -name '*.ipynb' \) \
  | sort
```

记录每个文件的：文件名、路径、扩展名、父目录名。

### Step B2: 语义分组

按优先级尝试三种策略：

**策略1：按子目录分组（优先）**
```
ch01-intro/ 下所有文件 → 「第一章: Introduction」
ch02-basics/ 下所有文件 → 「第二章: Basics」
```
目录名中的数字/词缀用于生成章节名。如目录名不含语义信息（如 `src/` `data/`），跳过此策略。

**策略2：按文件名前缀分组**
```
"测试报告.pdf" + "测试报告数据.xlsx" + "测试报告图表.png" → 同组
```
规则：去除扩展名后，最长公共前缀 ≥ 60% 或编辑距离 < 3 → 同组。

**策略3：按文件类型分组（兜底）**
```
所有 .pdf → 「PDF 文档」
所有 .md → 「笔记文件」
```
前两个策略都无法覆盖时才用。

### Step B3: 组内文件处理

对每个语义组：
1. **主文档**（PDF/MD/DOCX）：完整提取内容结构，作为组的主子节点
2. **附属文件**（xlsx/csv/yaml/json）：只提取元信息（列名/Sheet 名/顶层 key），作为主文档的子节点，前缀加 📎

### Step B4: 组装 XMindMark

```
中心主题 = 目录名（或目录名 + 一句话描述）

主分支 = 每个语义组：
  ├── 第一章: Introduction
  │   ├── (lecture.pdf 内容提取)
  │   │   ├── 1.1 标题A
  │   │   │   ├── 要点1
  │   │   │   └── 要点2
  │   │   └── 1.2 标题B
  │   └── 📎 数据集: data.csv (1500行, 列: feature1, feature2, label)
  ├── 第二章: Regression
  │   ├── (notes.md 内容提取)
  │   └── 📎 示例数据: examples.xlsx (2 Sheets: Linear, Logistic)
  └── 独立文档
      └── Project Requirements
          └── (project-requirements.docx 提取)
```

---

## 关键约束

- ❌ **不要**遍历每个源码文件并生成摘要
- ❌ **不要**给每个模块写详细的功能说明
- ❌ **不要**把原子目录作为主分支（必须经过语义分组）
- ✅ 脑图应该是「项目 README 的可视化版」或「学习资料的章节地图」
- ✅ 每层控制在 3-7 个子节点
- ✅ 总节点数 ≤80（避免脑图在 XMind 中过于庞大）
- ✅ 行数统计一次性完成：`find /tmp/proj -name "*.{ext}" | xargs wc -l | tail -1`
- ✅ 语义分组优先使用目录结构，其次文件名相似度
- ✅ 附属文件不独立成为主分支，挂在主文档下

---

## 跳过文件统计

处理完后，统计跳过的文件：
```bash
SKIP_EXT="png|jpg|jpeg|gif|webp|svg|bmp|mp4|avi|mov|mkv|webm|mp3|wav|ogg|flac|zip|tar|gz|rar|7z|so|o|a|dll|exe|class|pyc"
SKIPPED=$(find /tmp/proj -type f | grep -E "\.($SKIP_EXT)$" | wc -l)
```

在脑图末尾或生成消息中标注：「已跳过 N 个不支持的文件格式」（N > 0 时才显示）。

---

## 常见问题

### Q: 项目没有 README？
提取 `tree -L 2` 的目录结构 + `go.mod`/`package.json` 等构建文件信息，中心主题用目录名。

### Q: GitHub URL 克隆太慢？
用 `--depth 1` 浅克隆减少时间。如果仍然失败，提示用户直接用 README 的 raw URL 走 URL 场景。

### Q: 文件太多导致脑图爆炸？
严格约束主分支 ≤9 个。源码文件只统计不展开。多个小文件合并为一个「其他文件」节点。

### Q: 学习资料目录结构混乱（无章节目录）？
跳过策略1，用策略2（文件名前缀分组），再不行用策略3（按类型分组）。
