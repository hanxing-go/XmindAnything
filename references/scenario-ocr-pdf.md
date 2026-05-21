# 扫描版/OCR PDF 场景模板

## 适用
扫描版 PDF、图片型 PDF（文字不可直接提取，需要 OCR 识别）

## 前置依赖

```bash
# 安装 tesseract OCR 引擎 + 中英文语言包
apt-get install -y tesseract-ocr tesseract-ocr-chi-sim poppler-utils
```

验证：
```bash
tesseract --list-langs  # 应包含 eng + chi_sim
```

## 处理流程

1. **检测 PDF 类型**：先用 `pdftotext` 测试是否可直接提取文字
   ```bash
   pdftotext input.pdf /tmp/test.txt && wc -c /tmp/test.txt
   ```
   如果输出 < 100 字节 → 扫描版，需要 OCR

2. **PDF 转图片**：
   ```bash
   pdftoppm -png -r 150 input.pdf /tmp/ocr_pages/pg
   ```
   分辨率：150 DPI 足够（300 DPI 太慢，26 页约需 10 分钟）

3. **逐页 OCR**：
   ```bash
   cd /tmp/ocr_pages
   for f in pg-*.png; do
     tesseract "$f" stdout -l chi_sim+eng --psm 6 >> result.txt
   done
   ```
   双语言模式 `chi_sim+eng` 对中英文混排论文效果好

4. **阅读 OCR 结果**：用 `read` 工具读取 `/tmp/result.txt`，提取论文结构

5. **结构化 → XMindMark**：忽略 OCR 识别的公式、表格噪声，只提取关键概念

## 已知局限

- OCR 对公式、代码块、复杂表格识别效果差（不影响思维导图，因为只需要概念）
- 双栏排版可能导致阅读顺序混乱，需要人工判断段落归属
- 150 DPI 下英文字母可能部分识别错误，关键术语要交叉验证
- 扫描质量差的远古论文可能需要 200 DPI
- 26 页论文 OCR 约需 3-5 分钟

## 实战案例：TRELLIS 论文

输入：`trellis.pdf`（15MB，26 页扫描版，微软 3D 生成论文）

流程：
```
pdftotext → 26 字节（确认扫描版）
pdftoppm -r 150 → 26 张 PNG
tesseract chi_sim+eng → 111KB 文字
read OCR text → AI 理解结构
XMindMark 生成 → 7 主分支（基本信息/问题/方法/生成/编辑/实验/结论）
xmindmark -f xmind → .xmind ✅
```

效果：中英文混排识别良好，论文核心概念完整保留，公式表格未影响思维导图质量。
