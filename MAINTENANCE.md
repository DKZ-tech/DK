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
| 改简历 | 编辑 `_pages/cv.md`（章节化结构，新增内容参考 §六） |
| 换头像 | 覆盖 `images/profile1.jpg`（文件名不变最省事） |
| 加一条手工成果（软著 / 标准 / 专利申请号不在 Scholar 的） | 在 `_publications/` 新建一个 `.md`，见 §五 |
| 新增 / 修改科研项目 | 编辑 `_data/projects.yml`，见 §六 |
| 替换/上传简历 PDF | 覆盖 `assets/cv/CV_Dongkuan_Zhang.pdf`（CV 页会自动出现"下载 PDF"按钮） |

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
<div class="post-figure">
  <img src="{{ '/images/example.jpg' | relative_url }}" loading="lazy" alt="图片描述">
</div>
```

要点：

- `permalink` 每篇**必须唯一**（历史遗留的重复 permalink bug 已修复，别再复制错）；
- 图片先放进 `images/` 文件夹；
- 多图并排用 `<div class="post-figure">…</div>` 包裹，单张大图可用 `<div class="post-figure single">…</div>`，系统会自动在手机和电脑上合理缩放；
- 中英文分别放在 `class="lang-zh"` / `class="lang-en"` 的段落里，由页面右上角语言按钮切换；
- **动态列表页现在统一为纯文字 + 时间轴布局**：图片只在点进详情页后显示，列表里不再出现大小不一的缩略图。

图片规格建议（保持站点加载速度）：

| 图片用途 | 建议宽度 | 建议格式 | 说明 |
|---|---|---|---|
| 动态页照片 | ≤720 px | JPEG 82% | 单张控制在 200 KB 以内 |
| 证书 / 截图 | ≤900 px | PNG-8 或 JPEG 90% | 文字较多用 PNG，照片类用 JPEG |
| 头像 | 400 px | JPEG 85% | 侧栏显示尺寸只有 175 px |
| 首页装饰动图 | ≤480 px，≤30 帧 | GIF | 已在 `scripts/optimize_images.py` 中自动处理 |

若批量上传后体积仍大，可运行仓库中的 `scripts/optimize_images.py` 一键压缩（会自动按上表规则处理）。

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
│   ├─ navigation.yml   ← 导航栏菜单
│   └─ projects.yml     ← 科研项目列表（手工维护）
├─ images/            图片与头像（头像为 profile1.jpg）
├─ scripts/
│   └─ update_scholar.py ← Google Scholar 一键同步脚本
├─ _includes/         模板片段（语言按钮、论文条目渲染等）
├─ _config.yml        站点主配置（姓名、邮箱、各类学术主页链接）
```

## 六、手工新增一条成果（专利 / 软著 / 标准）

Google Scholar 同步脚本**只抓 Scholar 上可见的成果**，以下条目需要手工添加：

- 发明专利**申请公开号**（CN...A，公开阶段、未授权）；
- 实用新型专利（Scholar 收录不全）；
- 软件著作权；
- 团体 / 行业标准。

### 在 `_publications/` 新建一个 `.md` 文件

文件名按日期 + 类型 + 简短标题，例如：

```
_publications/2025-08-12-patent-fly-ash.md
```

### 模板（以**发明专利**为例）

```markdown
---
title: '<span class="lang-zh">一种垃圾焚烧炉内自降飞灰的装置</span><span class="lang-en">A device for self-settling fly ash in a waste incinerator</span>'
collection: publications
category: patents
permalink: /publication/patent-CN223137888U
date: 2025-07-22
venue: '<span class="lang-zh">中国实用新型专利，ZL 2024 2 2052228.7</span><span class="lang-en">China Utility Model Patent No. ZL 2024 2 2052228.7</span>'
authors: '<span class="lang-zh">姬国钊, 张东宽</span><span class="lang-en">Guozhao Ji, Dongkuan Zhang</span>'
---

<p class="lang-zh">简短中文描述……</p>
<p class="lang-en">Short English description...</p>
```

### 模板（**软件著作权**）

把 `category: patents` 改成 `category: software`。

### 模板（**标准**）

把 `category: patents` 改成 `category: standards`，`venue` 写标准号 + 名称即可。

### 关键规则

- `permalink` **必须唯一**（同一个分类下不要重复）；
- `date` 用 `YYYY-MM-DD` 或 `YYYY-01-01`（仅知年份时），决定在分类列表中的排序；
- `collection: publications` 不能漏，否则 Jekyll 不会收录到出版物集合；
- 中英文分别用 `<span class="lang-zh">` 和 `<span class="lang-en">` 包裹；
- `scripts/update_scholar.py` **不会动**这类手工文件，可放心反复运行同步。

---

## 六、新增 / 修改科研项目

论文成果页（`/publications/`）右侧现在按分类展示，左侧有 sticky 导航。其中「科研项目」板块读取 `_data/projects.yml`。

### 模板

```yaml
- title_zh: "中文项目名称"
  title_en: "English project title"
  id: "项目编号（没有可留空）"
  funder_zh: "资助来源中文"
  funder_en: "Funding source English"
  role_zh: "参与 / 核心成员 / 数值模拟技术服务"
  role_en: "Participant / Core member / Numerical simulation service"
  period: "2023–2025"
```

### 关键规则

- 所有字段都支持中英双语；
- `id` 为空时项目编号行会自动隐藏；
- 保存后无需额外配置，论文成果页会自动渲染；
- CV 页如需同步引用科研项目，可直接链接到 `/publications/#projects`。

---

## 七、修改 / 扩展简历页（`cv.md`）

`_pages/cv.md` 的结构（直接编辑 markdown）：

```
├─ 顶部：标题 + "下载 PDF" 按钮（引用 assets/cv/CV_Dongkuan_Zhang.pdf）
├─ 基本信息    ← 新增联系方式在这里
├─ 教育经历
├─ 工作经历    ← 工业界经历
├─ 联合培养 / 访学经历  ← CSC、连理全球等
├─ 研究方向
├─ 学术成果概览  ← 显示 Scholar 统计徽章（自动）
├─ 期刊论文     ← 表格由 Jekyll 从 _publications 分类 = manuscripts 自动生成
├─ 专利         ← 表格由 Jekyll 从 _publications 分类 = patents 自动生成
├─ 软件著作权   ← 同上，category: software
├─ 标准         ← 同上，category: standards
├─ 科研项目与科技成果转化
├─ 荣誉与获奖   ← 手写维护
├─ 技术服务与学术兼职
└─ 技术技能
```

**新增 / 修改注意事项**：

- 论文、专利、软著、标准的列表项**不要在 cv.md 里手写**——它们由 Jekyll 根据 `_publications/` 自动渲染。你只要新增 / 修改对应的 `pub-*.md` 或手工 `*.md`，CV 页会自动更新。
- 「荣誉与获奖」「科研项目与转化」需要手工写，因为它们是离散事件，没有标准化字段。建议使用统一表格样式以保持视觉一致：

```markdown
<tr><td class="year">2025.09</td><td><strong>奖项名称</strong><br>一句中文或英文注释。</td></tr>
```

- 改完 CV 页内容后，运行下面的脚本即可一键生成最新 PDF 并自动覆盖到 `assets/cv/CV_Dongkuan_Zhang.pdf`（「下载 PDF」按钮指向的文件）。

  ```bash
  python scripts/generate_cv_pdf.py
  ```

  脚本流程：① `jekyll build` 构建站点；② 提取 `_site/cv/index.html` 中的 CV 内容区；③ 用无头 Edge/Chrome 按 A4 尺寸打印成 PDF；④ 输出到 `assets/cv/CV_Dongkuan_Zhang.pdf`。

  若 `_site` 已经是最新，可加 `--skip-build` 仅重出 PDF：

  ```bash
  python scripts/generate_cv_pdf.py --skip-build
  ```

  环境要求：已安装 Ruby/Jekyll（`E:\Ruby`）、Microsoft Edge 或 Google Chrome。

- CV 页使用的样式（`.cv-table` / `.cv-section`）定义在文件顶部的 `<style>` 块内，要调整字号、改色或加图标直接在那里改。

---

## 八、修改个人信息

`_config.yml` 顶部 `author:` 一节集中管理：头像、姓名、简介、所在地、单位、邮箱、
Google Scholar / ORCID / GitHub 等链接——想加 ResearchGate、领英等，填上对应字段即可，侧栏会自动出现图标。

### 修改微信二维码 / 微信号

- 微信二维码图片：`images/weixin-qr.jpg`（建议用微信「我 → 二维码名片」截图，替换此文件即可，保持不倾斜、二维码居中）。
- 微信号：修改 `_config.yml` 中 `author.wechat` 的值，并同步修改 `_pages/about.md` 中两处 `DK-techie`（图片下方的大字和复制按钮的 `data-clipboard-text`）。
- 首页的联系卡片和左侧边栏都会自动使用新微信号。

## 九、本地预览（已配置好）

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

## 十、常见问题

- **推送后网站没更新**：等 1–2 分钟；若仍不行，到仓库 Settings → Pages 查看构建错误，或 Actions/Pages 构建日志。
- **某篇论文信息不对**：先去 Google Scholar 修正资料，再跑一次同步脚本。
- **语言切换按钮没反应**：清浏览器缓存；确认 `assets/js/language-toggle.js` 存在且 `_includes/scripts.html` 中有引用。

---

## 十一、图片上传与压缩建议

本站所有图片已经过响应式处理：

- 桌面端：动态页照片默认 320 px 宽、证书默认 420 px 宽；
- 手机端（≤480 px）：图片会自动占满容器宽度，避免左右滑动；
- 非首屏图片全部启用 `loading="lazy"`，滚动到附近才加载；
- 全局 `max-width: 100%; height: auto` 兜底，防止任何图片撑破布局。

你后续上传图片时，遵循 §三「图片规格建议」即可。若嫌手动压缩麻烦，把原图丢进 `images/` 后运行：

```bash
python scripts/optimize_images.py
```

该脚本会按用途自动压缩 GIF/JPEG/PNG，并尽量保留透明度/文字清晰度。
