# 网站维护指南（维护手册）

本站基于 [academicpages](https://academicpages.github.io)（Jekyll）搭建，托管在 GitHub Pages。
本文件面向站点所有者，说明日常更新操作。**所有改动 `git push` 后约 1–2 分钟自动发布。**

---

## 一、日常更新速查

| 我想做什么 | 怎么做 |
|---|---|
| 同步 Google Scholar 论文 | 仓库根目录运行 `python scripts/update_scholar.py`，然后提交推送 |
| 发一条新动态 | 在 `_posts/` 复制任意现有文件，改文件名/日期/内容 |
| 改首页介绍 | 编辑 `_pages/about.md` |
| 改简历 | 编辑 `_pages/cv.md` |
| 换头像 | 覆盖 `images/profile1.jpg`（文件名不变最省事） |
| 加一条手工成果（软著/标准） | 在 `_publications/` 新建一个 `.md`（参考现有软件著作权条目） |

---

## 二、同步 Google Scholar（论文自动更新）

```bash
# 首次使用先装依赖（只需一次）
pip install requests beautifulsoup4

# 一键同步（仓库根目录运行）
python scripts/update_scholar.py
```

脚本行为：

1. 抓取 Google Scholar 主页（用户 ID 已内置：`_R1WLLgAAAAJ`）；
2. 为每条成果生成/更新 `_publications/pub-<编号>.md`，含标题、作者、期刊、年份、**实时引用数**和 Scholar 链接；
3. 把总被引 / h-index / i10 写入 `_data/scholar.yml`（论文页顶部的统计徽章）；
4. **幂等**：重复运行只更新数字，不会重复建文件；
5. 不会动手工维护的文件（软件著作权、标准等非 `pub-` 开头的文件）。

常用参数：

```bash
python scripts/update_scholar.py --dry-run   # 只预览不写文件
python scripts/update_scholar.py --user XXXX # 换一个 Scholar 账号
```

注意事项：

- **若提示触发验证码**（HTTP 429/403 或解析不到成果）：Google 对频繁抓取有限制，等几小时再跑即可；平时 1–2 个月跑一次完全没问题。
- 想给某篇论文补充中文译名或 DOI：直接编辑对应的 `pub-*.md`，在 front matter 中加一行
  `title_zh: '中文标题'` 或 `doi: '10.xxxx/xxxxx'`——脚本更新时会**保留**这些手工字段。

---

## 三、发布一条新动态（Moments）

在 `_posts/` 新建文件，**文件名必须是 `年-月-日-英文小写短横线.md`**，例如：

```
_posts/2026-05-20-new-award.md
```

内容模板（复制现有动态改即可）：

```markdown
---
title: "中文标题 / English Title"
date: 2026-05-20
permalink: /posts/2026/05/new-award/
---
<p class="lang-zh">中文正文……</p>
<p class="lang-en">English body...</p>
<div style="display:flex; justify-content:center; gap:12px; flex-wrap:wrap;">
  <img src="{{ '/images/图片名.jpg' | relative_url }}" style="max-width:320px; height:auto; border-radius:8px;">
</div>
```

要点：

- `permalink` 每篇**必须唯一**（历史遗留的重复 permalink bug 已修复，别再复制错）；
- 图片先放进 `images/` 文件夹；
- 中英文分别放在 `class="lang-zh"` / `class="lang-en"` 的段落里，由页面右上角语言按钮切换。

---

## 四、双语机制说明（写内容时必读）

整站通过导航栏右侧的 **中 / EN 按钮**切换语言，规则：

- 中文内容包在 `<span class="lang-zh">…</span>` 或 `<p class="lang-zh">…</p>` 里；
- 英文内容包在 `<span class="lang-en">…</span>` 或 `<p class="lang-en">…</p>` 里；
- 首次访问自动跟随浏览器语言，选择会记忆在浏览器本地；
- 涉及代码文件：`_includes/head.html`（首屏防闪烁）、`assets/js/language-toggle.js`（切换逻辑）、`assets/css/main.scss`（样式，已内置 `.home-grid`/`.home-card` 卡片样式可复用）。

论文标题保持原文（中文论文就显示中文，英文论文就显示英文），不强行翻译。

---

## 五、目录结构

```
├─ _pages/            页面：首页 about.md、论文 publications.html、动态 year-archive.html、简历 cv.md、404
├─ _posts/            动态（Moments）文章
├─ _publications/     成果条目
│   ├─ pub-*.md         ← scripts/update_scholar.py 自动生成，勿手工改名
│   └─ 2025-*-*.md      ← 手工维护（软著、标准）
├─ _data/
│   ├─ scholar.yml      ← 脚本生成的引用统计，勿手工编辑
│   └─ navigation.yml   ← 导航栏菜单
├─ images/            图片与头像（头像为 profile1.jpg）
├─ scripts/
│   └─ update_scholar.py ← Google Scholar 一键同步脚本
├─ _includes/         模板片段（语言按钮、论文条目渲染等）
├─ _config.yml        站点主配置（姓名、邮箱、各类学术主页链接）
```

## 六、修改个人信息

`_config.yml` 顶部 `author:` 一节集中管理：头像、姓名、简介、所在地、单位、邮箱、
Google Scholar / ORCID / GitHub 等链接——想加 ResearchGate、领英等，填上对应字段即可，侧栏会自动出现图标。

## 七、本地预览（已配置好）

本机已安装 Ruby 3.1.4 + DevKit 到 **`E:\Ruby`**，依赖也已装好。两种方式：

**方式一（最简单）**：双击仓库根目录的 `serve_local.bat`，浏览器打开
<http://127.0.0.1:4000/DK/>，Ctrl+C 关闭。

**方式二（命令行）**：打开 "Start Command Prompt with Ruby"（开始菜单，装 Ruby 时自带）：

```bat
cd /d D:\Github_projects\DK
bundle exec jekyll serve
```

改文件保存后会自动刷新（增量构建），关掉窗口即停。
不本地预览也可以：直接 push，用线上站点检查。

> 技术备注：原生扩展（racc/sassc 等）编译依赖 MSYS2 工具链（`E:\Ruby\msys64`）。
> 若以后新增 gem 需要编译，务必通过 `ridk enable` 环境执行 `bundle install`，
> 否则会报 `ruby.h: No such file or directory` 或临时目录权限错误。

## 八、常见问题

- **推送后网站没更新**：等 1–2 分钟；若仍不行，到仓库 Settings → Pages 查看构建错误，或 Actions/Pages 构建日志。
- **某篇论文信息不对**：先去 Google Scholar 修正资料，再跑一次同步脚本。
- **语言切换按钮没反应**：清浏览器缓存；确认 `assets/js/language-toggle.js` 存在且 `_includes/scripts.html` 中有引用。
