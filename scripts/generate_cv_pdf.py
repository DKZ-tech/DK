# -*- coding: utf-8 -*-
"""
generate_cv_pdf.py — 根据网页 CV 界面一键生成最新简历 PDF
============================================================
原理：用 Jekyll 构建站点 -> 提取构建产物 _site/cv/index.html 中的内容区
(<div class="archive">) -> 套用打印样式 -> 无头 Edge/Chrome 打印为 A4 PDF，
输出到 assets/cv/CV_Dongkuan_Zhang.pdf（即网页「下载 PDF」按钮指向的文件）。

用法：
    python scripts/generate_cv_pdf.py             # 完整流程：构建 + 生成 + 校验
    python scripts/generate_cv_pdf.py --skip-build  # 跳过 jekyll build（_site 已是最新时）

依赖：Ruby/Jekyll（构建）、Microsoft Edge 或 Chrome（打印）、
      PyMuPDF（可选，用于校验页数）。
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SITE_CV = REPO / "_site" / "cv" / "index.html"
PRINT_HTML = REPO / "_site" / "cv" / "cv_print.html"
OUT_PDF = REPO / "assets" / "cv" / "CV_Dongkuan_Zhang.pdf"

RUBY_CANDIDATES = [
    Path(r"E:\Ruby\bin\ruby.exe"),
    Path(r"C:\Ruby31-x64\bin\ruby.exe"),
]
EDGE_CANDIDATES = [
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"),
]

PRINT_CSS = """
<style>
@page { size: A4; margin: 15mm 14mm; }
body {
  font-family: "Microsoft YaHei", "Segoe UI", "PingFang SC", "Helvetica Neue", Arial, sans-serif;
  font-size: 10.5pt; color: #111; line-height: 1.55; margin: 0; padding: 0;
}
h1 { font-size: 17pt; margin: 0 0 0.35em; }
h2 { font-size: 12.5pt; margin: 1.0em 0 0.35em; padding-bottom: 2px;
     border-bottom: 1.5px solid #bbb; page-break-after: avoid; }
p { margin: 0.35em 0; }
ul { margin: 0.3em 0 0.6em; padding-left: 1.4em; }
li { margin: 0.15em 0; }
a { color: #111; text-decoration: none; }
strong { color: #000; }
.cv-section { margin: 0.55em 0; }
.cv-table { width: 100%; border-collapse: collapse; margin: 0.4em 0; font-size: 9.5pt; }
.cv-table th, .cv-table td { padding: 3.5px 6px; border-bottom: 1px solid #ddd;
                            vertical-align: top; text-align: left; }
.cv-table td.year { white-space: nowrap; width: 6em; color: #333; font-weight: 600; }
.cv-table td.type { white-space: nowrap; width: 7em; color: #555; }
.cv-table tr { page-break-inside: avoid; }
.cv-meta { color: #444; font-size: 8.5pt; }
.btn { display: none !important; }
</style>
"""


class ArchiveExtractor(HTMLParser):
    """提取 <div class="archive"> ... </div> 平衡块（保留原始标签文本）。"""

    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.depth = 0
        self.in_target = False
        self.parts = []

    def _enter(self):
        self.in_target = True
        self.depth = 1
        self.parts.append(self.get_starttag_text())

    def handle_starttag(self, tag, attrs):
        classes = dict(attrs).get("class", "").split()
        if tag == "div" and not self.in_target and "archive" in classes:
            self._enter()
            return
        if self.in_target:
            if tag == "div":
                self.depth += 1
            self.parts.append(self.get_starttag_text())

    def handle_endtag(self, tag):
        if not self.in_target:
            return
        self.parts.append(f"</{tag}>")
        if tag == "div":
            self.depth -= 1
            if self.depth == 0:
                self.in_target = False

    def handle_data(self, data):
        if self.in_target:
            self.parts.append(data)

    def handle_comment(self, data):
        if self.in_target:
            self.parts.append(f"<!--{data}-->")

    def handle_entityref(self, name):
        if self.in_target:
            self.parts.append(f"&{name};")

    def handle_charref(self, name):
        if self.in_target:
            self.parts.append(f"&#{name};")


def find_tool(candidates, name):
    for c in candidates:
        if c.exists():
            return c
    which = shutil.which(name)
    if which:
        return Path(which)
    return None


def run_jekyll_build():
    ruby = find_tool(RUBY_CANDIDATES, "ruby")
    if not ruby:
        print("[x] 未找到 ruby，无法构建站点。", file=sys.stderr)
        sys.exit(1)
    bundle = ruby.parent / "bundle"
    env = os.environ.copy()
    env.pop("ACC_PRODUCT_CONFIG_V3", None)  # 该环境变量会导致 bundler 崩溃
    # bundle exec 在 Windows 上通过 PATH 解析 gem 可执行文件，必须把 Ruby bin
    # 及 MSYS2 工具链目录放到 PATH 最前面（否则报 "command not found: jekyll"）
    ruby_root = ruby.parent.parent
    msys_paths = [
        str(ruby.parent),
        str(ruby_root / "msys64" / "ucrt64" / "bin"),
        str(ruby_root / "msys64" / "usr" / "bin"),
    ]
    env["PATH"] = os.pathsep.join(msys_paths + [env.get("PATH", "")])
    print("[1/4] jekyll build ...")
    proc = subprocess.run(
        [str(ruby), str(bundle), "exec", "jekyll", "build"],
        cwd=str(REPO), env=env, capture_output=True,
    )
    if proc.returncode != 0:
        print(proc.stdout.decode("utf-8", errors="replace")[-2000:], file=sys.stderr)
        print(proc.stderr.decode("utf-8", errors="replace")[-3000:], file=sys.stderr)
        print("[x] jekyll build 失败。", file=sys.stderr)
        sys.exit(1)


def extract_archive(html_text):
    parser = ArchiveExtractor()
    parser.feed(html_text)
    content = "".join(parser.parts)
    if not content.strip():
        print("[x] 未在构建产物中找到 <div class=\"archive\">，CV 页面结构可能变了。",
              file=sys.stderr)
        sys.exit(1)
    return content


def build_print_html(content):
    # 去掉「下载 PDF」按钮（顶部 flex 容器里的 <a class="btn"> 和底部段落）
    content = re.sub(
        r"<a\b[^>]*class=\"[^\"]*\bbtn\b[^\"]*\"[^>]*>.*?</a>",
        "", content, flags=re.S,
    )
    content = re.sub(
        r"<p[^>]*>\s*(?:<a\b[^>]*class=\"[^\"]*\bbtn\b[^\"]*\"[^>]*>.*?</a>)\s*</p>",
        "", content, flags=re.S,
    )
    doc = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<title>CV — Dongkuan Zhang</title>
{PRINT_CSS}
</head>
<body>
{content}
{PRINT_CSS}
</body>
</html>"""
    PRINT_HTML.write_text(doc, encoding="utf-8")
    print(f"    打印版 HTML: {PRINT_HTML}")


def print_to_pdf(browser):
    out_dir = Path(tempfile.mkdtemp(prefix="edge_cv_"))
    url = PRINT_HTML.resolve().as_uri()
    cmd = [
        str(browser), "--headless=new", "--disable-gpu", "--no-sandbox",
        "--disable-extensions",
        f"--user-data-dir={out_dir}",
        "--no-pdf-header-footer",
        "--virtual-time-budget=8000",
        f"--print-to-pdf={OUT_PDF}",
        url,
    ]
    print(f"[3/4] 无头浏览器打印 PDF -> {OUT_PDF}")
    proc = subprocess.run(cmd, capture_output=True)
    shutil.rmtree(out_dir, ignore_errors=True)
    if not OUT_PDF.exists() or OUT_PDF.stat().st_size == 0:
        print(proc.stdout.decode("utf-8", errors="replace")[-1500:], file=sys.stderr)
        print(proc.stderr.decode("utf-8", errors="replace")[-1500:], file=sys.stderr)
        print("[x] PDF 生成失败。", file=sys.stderr)
        sys.exit(1)


def verify_pdf():
    try:
        import fitz  # PyMuPDF
    except ImportError:
        print("    (未安装 PyMuPDF，跳过页数校验)")
        return
    doc = fitz.open(str(OUT_PDF))
    n = doc.page_count
    first = doc[0].get_text().strip().replace("\n", " ")[:60]
    print(f"[4/4] 校验：共 {n} 页，首页开头：{first}")
    doc.close()
    if n < 1:
        sys.exit(1)


def main():
    ap = argparse.ArgumentParser(description="根据网页 CV 一键生成简历 PDF")
    ap.add_argument("--skip-build", action="store_true", help="跳过 jekyll build")
    args = ap.parse_args()

    if not args.skip_build:
        run_jekyll_build()
    else:
        print("[1/4] 跳过构建（--skip-build）")

    if not SITE_CV.exists():
        print("[x] 缺少 _site/cv/index.html，请先运行完整流程。", file=sys.stderr)
        sys.exit(1)

    print("[2/4] 提取 CV 内容区并套用打印样式 ...")
    html_text = SITE_CV.read_text(encoding="utf-8")
    build_print_html(extract_archive(html_text))

    browser = find_tool(EDGE_CANDIDATES, "msedge") or find_tool(EDGE_CANDIDATES, "chrome")
    if not browser:
        print("[x] 未找到 Edge/Chrome，无法打印 PDF。", file=sys.stderr)
        sys.exit(1)
    print(f"    使用浏览器: {browser}")

    print_to_pdf(browser)
    verify_pdf()
    size_kb = OUT_PDF.stat().st_size / 1024
    print(f"\n完成 ✅ {OUT_PDF}（{size_kb:.0f} KB）")
    print("推送到 GitHub 后，网页上的「下载 PDF」即指向这份最新简历。")


if __name__ == "__main__":
    main()
