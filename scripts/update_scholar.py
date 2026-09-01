#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update_scholar.py — 一键将 Google Scholar 学术成果同步到本站 _publications/ 目录。

用法（在仓库根目录运行）:
    python scripts/update_scholar.py                # 使用默认账号
    python scripts/update_scholar.py --user XXXX    # 指定其他 Scholar 用户 ID
    python scripts/update_scholar.py --dry-run      # 只预览，不写文件

依赖:
    pip install requests beautifulsoup4

说明:
    * 每条 Scholar 成果生成一个 _publications/pub-<cluster_id>.md 文件，
      文件名由 Scholar 的 cluster ID 决定，重复运行只会更新内容（幂等）。
    * 脚本只管理自己生成的 pub-*.md 文件；手工添加的其他文件
      （如软件著作权、标准）不会被修改或删除。
    * front matter 中手动添加的额外字段（如 doi、title_zh）会被保留。
    * 引用统计写入 _data/scholar.yml，供 publications 页面展示。
    * 如果 Google 弹出验证码（频繁运行时可能发生），请等待几小时再试，
      或在浏览器打开同一链接后重试。
"""

import argparse
import re
import sys
import time
from datetime import date
from pathlib import Path

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit("缺少依赖，请先运行: pip install requests beautifulsoup4")

# ---------------------------------------------------------------------------
# 配置
# ---------------------------------------------------------------------------
DEFAULT_USER = "_R1WLLgAAAAJ"          # 张东宽的 Google Scholar 用户 ID
ROOT = Path(__file__).resolve().parent.parent
PUB_DIR = ROOT / "_publications"
DATA_DIR = ROOT / "_data"
STATS_FILE = DATA_DIR / "scholar.yml"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

# 手工维护的分类规则：venue（期刊/专利号）匹配到正则即归入对应类别
PATENT_RE = re.compile(r"\bCN\d{9,}(?:\.\d|[A-Z]\d?)?", re.IGNORECASE)

# front matter 中由脚本管理的字段（手工添加的其他字段会被保留）
MANAGED_FIELDS = [
    "title", "collection", "category", "permalink", "date",
    "venue", "authors", "paperurl", "citation_count", "scholar_id",
]

# ---------------------------------------------------------------------------
# 抓取
# ---------------------------------------------------------------------------

def fetch_profile(user: str) -> str:
    """抓取 Google Scholar 成果列表页（每页 100 条）。"""
    url = (
        f"https://scholar.google.com/citations?user={user}"
        f"&hl=en&pagesize=100&view_op=list_works&sortby=pubdate"
    )
    resp = requests.get(url, headers=HEADERS, timeout=30)
    if resp.status_code != 200:
        sys.exit(f"请求失败 HTTP {resp.status_code}，若为 429/403 请稍后再试（反爬限制）。")
    if "gsc_a_tr" not in resp.text:
        sys.exit("未解析到成果列表：可能触发了 Google 验证码，请稍后再试或换个网络。")
    return resp.text


def fetch_stats_page(user: str) -> str:
    """抓取学者主页（含右侧引用统计表）。"""
    url = f"https://scholar.google.com/citations?user={user}&hl=en"
    resp = requests.get(url, headers=HEADERS, timeout=30)
    time.sleep(1)  # 轻微间隔，降低触发反爬的概率
    return resp.text if resp.status_code == 200 else ""


def parse_publications(html_text: str, user: str):
    """解析成果表格，返回 dict 列表。"""
    soup = BeautifulSoup(html_text, "html.parser")
    pubs = []
    for row in soup.select("tr.gsc_a_tr"):
        title_el = row.select_one("td.gsc_a_t a.gsc_a_at")
        if not title_el:
            continue
        title = title_el.get_text(strip=True)
        title = re.sub(r"\s*[①②③④⑤⑥⑦⑧⑨⑩]$", "", title)  # 去掉 Scholar 脚注标记
        href = title_el.get("href", "")
        m = re.search(r"citation_for_view=([^:]+):(.+)", href)
        cluster_id = m.group(2) if m else None

        gray = row.select("td.gsc_a_t div.gs_gray")
        authors = gray[0].get_text(strip=True) if len(gray) > 0 else ""
        venue_line = gray[1].get_text(strip=True) if len(gray) > 1 else ""
        # venue 行形如 "Journal Name, 12(3), 45-52, 2025"；截掉尾部年份
        venue = re.sub(r",?\s*\d{4}\s*$", "", venue_line).strip().rstrip(",")

        year_el = row.select_one("td.gsc_a_y span.gsc_a_h")
        year = year_el.get_text(strip=True) if year_el else ""

        cited_el = row.select_one("td.gsc_a_c a")
        cited = cited_el.get_text(strip=True) if cited_el else ""
        cited_num = int(cited) if cited.isdigit() else 0

        if PATENT_RE.search(venue_line):
            category = "patents"
        else:
            category = "manuscripts"

        paperurl = (
            f"https://scholar.google.com/citations?view_op=view_citation&hl=en"
            f"&user={user}&citation_for_view={user}:{cluster_id}"
        ) if cluster_id else ""

        pubs.append({
            "title": title,
            "cluster_id": cluster_id or "",
            "authors": authors,
            "venue": venue,
            "year": year,
            "citation_count": cited_num,
            "category": category,
            "paperurl": paperurl,
        })
    return pubs


def parse_stats(html_text: str):
    """解析主页上的引用统计（总被引 / h 指数 / i10 指数）。"""
    soup = BeautifulSoup(html_text, "html.parser")
    stats = {}
    for row in soup.select("#gsc_rsb_st tr"):
        cells = row.select("td")
        if len(cells) < 2:
            continue
        key = cells[0].get_text(strip=True).lower()
        val = cells[1].get_text(strip=True)
        if "citation" in key:
            stats["total_citations"] = val
        elif "h-index" in key:
            stats["h_index"] = val
        elif "i10" in key:
            stats["i10_index"] = val
    return stats


# ---------------------------------------------------------------------------
# 生成 markdown
# ---------------------------------------------------------------------------

def yaml_escape(value: str) -> str:
    """给 YAML 单引号字符串转义。"""
    return str(value).replace("'", "''")


def build_front_matter(pub: dict, extra: dict) -> str:
    lines = [
        "---",
        f'title: "{yaml_escape(pub["title"])}"',
        "collection: publications",
        f'category: {pub["category"]}',
        f'permalink: /publication/{pub["cluster_id"]}',
        f'date: {pub["year"] or "2025"}-01-01',
        f'venue: \'{yaml_escape(pub["venue"])}\'',
        f'authors: \'{yaml_escape(pub["authors"])}\'',
        f'paperurl: "{pub["paperurl"]}"',
        f'citation_count: {pub["citation_count"]}',
        f'scholar_id: "{pub["cluster_id"]}"',
    ]
    # 保留手工维护的额外字段（doi / title_zh / excerpt 等）
    for key in ("title_zh", "doi", "excerpt"):
        if key in extra:
            lines.append(f"{key}: '{yaml_escape(extra[key])}'")
    lines.append("---")
    return "\n".join(lines) + "\n"


BODY_TEMPLATE = """\
<p class="lang-zh">本条目由 Google Scholar 自动同步生成，详细信息请访问
<a href="{paperurl}">Google Scholar 页面</a>。</p>
<p class="lang-en">This entry is auto-synced from Google Scholar. See the
<a href="{paperurl}">Google Scholar page</a> for details.</p>
"""


def parse_existing(path: Path) -> dict:
    """读取已有文件的 front matter，返回额外（非托管）字段。"""
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    extra = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if kv and kv.group(1) not in MANAGED_FIELDS:
            extra[kv.group(1)] = kv.group(2).strip().strip("'\"")
    return extra


def write_publication(pub: dict, dry_run: bool) -> bool:
    fname = f"pub-{pub['cluster_id']}.md"
    path = PUB_DIR / fname
    extra = parse_existing(path)
    content = build_front_matter(pub, extra) + "\n" + BODY_TEMPLATE.format(paperurl=pub["paperurl"])
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    if not dry_run:
        PUB_DIR.mkdir(exist_ok=True)
        path.write_text(content, encoding="utf-8")
    return True


def write_stats(stats: dict, dry_run: bool):
    if not stats:
        return
    lines = [
        "# 由 scripts/update_scholar.py 自动生成，请勿手工编辑",
        f"updated_at: '{date.today().isoformat()}'",
        f"total_citations: {stats.get('total_citations', 0)}",
        f"h_index: {stats.get('h_index', 0)}",
        f"i10_index: {stats.get('i10_index', 0)}",
    ]
    content = "\n".join(lines) + "\n"
    target = STATS_FILE
    if not dry_run:
        DATA_DIR.mkdir(exist_ok=True)
        target.write_text(content, encoding="utf-8")
    print(f"  统计: 被引 {stats.get('total_citations')} · h-index {stats.get('h_index')} · i10 {stats.get('i10_index')}")


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="同步 Google Scholar 成果到本站")
    parser.add_argument("--user", default=DEFAULT_USER, help="Google Scholar 用户 ID")
    parser.add_argument("--dry-run", action="store_true", help="只预览不写文件")
    args = parser.parse_args()

    print(f"[1/3] 抓取 Google Scholar（user={args.user}）...")
    html_text = fetch_profile(args.user)
    stats_html = fetch_stats_page(args.user)

    print("[2/3] 解析成果列表...")
    pubs = parse_publications(html_text, args.user)
    if not pubs:
        sys.exit("未解析到任何成果，页面结构可能已变化，请检查脚本。")

    print(f"[3/3] 生成/更新 {len(pubs)} 个成果文件 -> _publications/")
    changed = 0
    for pub in pubs:
        fname = f"pub-{pub['cluster_id']}.md"
        existed = (PUB_DIR / fname).exists()
        if write_publication(pub, args.dry_run):
            changed += 1
            flag = "[更新]" if existed else "[新增]"
            year = pub["year"] or "????"
            print(f"  {flag} {year} {pub['title'][:60]}{'…' if len(pub['title']) > 60 else ''}")
    print(f"共 {changed} 个文件有变化（其余无变化，保持原样）。")

    write_stats(parse_stats(stats_html), args.dry_run)

    # 提示未被 Scholar 覆盖的手工文件
    scholar_ids = {p["cluster_id"] for p in pubs}
    manual = [f for f in PUB_DIR.glob("*.md") if not f.name.startswith("pub-")]
    if manual:
        print(f"\n提示: {len(manual)} 个手工维护的成果文件未受影响: "
              + ", ".join(f.name for f in manual))

    if args.dry_run:
        print("\n(dry-run 模式，未写入任何文件)")
    else:
        print("\n完成！请检查 git diff 后提交并推送即可发布。")


if __name__ == "__main__":
    main()
