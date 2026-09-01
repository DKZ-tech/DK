# DK — 张东宽 / Dongkuan Zhang 个人学术主页

基于 [academicpages](https://academicpages.github.io)（Jekyll + GitHub Pages）搭建的个人学术主页，
支持**中英双语切换**（导航栏右侧「中 / EN」按钮），论文成果可从 Google Scholar **一键同步**。

- 线上地址：<https://dkz-tech.github.io/DK/>
- Google Scholar：<https://scholar.google.com/citations?user=_R1WLLgAAAAJ>

## 快速上手

```bash
# 同步 Google Scholar 论文（详见 MAINTENANCE.md）
pip install requests beautifulsoup4
python scripts/update_scholar.py
```

日常维护（发动态、改首页、换头像、加软著条目等）请阅读 **[MAINTENANCE.md](MAINTENANCE.md)**（中文维护手册）。

## 目录速览

| 目录 | 用途 |
|---|---|
| `_pages/` | 首页、论文页、动态页、简历页 |
| `_posts/` | 动态文章（Moments） |
| `_publications/` | 成果条目（`pub-*.md` 为脚本自动生成） |
| `scripts/update_scholar.py` | Google Scholar 一键同步脚本 |
| `images/` | 图片与头像 |
| `_config.yml` | 站点与个人信息主配置 |

## 致谢

站点模板来自 [academicpages/academicpages.github.io](https://github.com/academicpages/academicpages.github.io)（MIT License）。
