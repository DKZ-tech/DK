---
permalink: /about/
title: '<span class="lang-zh">个人简介 / </span><span class="lang-en">About</span>'
author_profile: true
body_class: paper-page
redirect_from:
  - /about.html
---

<div class="profile-lead">
  <p class="lang-zh">我是<strong>张东宽</strong>，大连理工大学环境学院博士研究生，导师为<a href="https://faculty.dlut.edu.cn/jiguozhao/zh_CN/index.htm">姬国钊教授</a>，预计 2027 年毕业。我的研究聚焦<strong>面向废弃物焚烧技术的智能多相流建模</strong>——把基于物理机理的 CFD 数值模拟与人工智能驱动的流场预测结合起来，解决高盐有机釜残这类难处理燃料"烧不透、喷嘴易堵"的工程难题。</p>
  <p class="lang-en">I am <strong>Dongkuan Zhang</strong>, a PhD candidate at the School of Environmental Science and Engineering, Dalian University of Technology, supervised by <a href="https://faculty.dlut.edu.cn/jiguozhao/zh_CN/index.htm">Prof. Guozhao Ji</a> (expected graduation 2027). My research focuses on <strong>intelligent multiphase flow modeling for waste incineration</strong> — coupling physics-based CFD simulation with AI-driven flow prediction to solve the engineering problem of high-salt organic still residues that burn incompletely and clog spray nozzles.</p>
</div>

<h2><span class="lang-zh">培养经历</span><span class="lang-en">Training</span></h2>

<p class="lang-zh">我的学术训练横跨三个国家的研究组：大连理工大学打下多相流建模与实验的基础；东京科学大学（原东京工业大学）Cross 实验室让我进入过程系统工程与国际合作的环境；卢森堡大学 Ladewig 实验室则延伸到膜材料与表征。三段经历方法互补，指向同一个问题。</p>
<p class="lang-en">My training spans research groups in three countries: Dalian University of Technology built the foundation in multiphase flow modeling and experimentation; the Cross Laboratory at Institute of Science Tokyo (formerly Tokyo Institute of Technology) brought me into process systems engineering and international collaboration; and the Ladewig group at the University of Luxembourg extends that work into membrane materials and characterization. The three stages are methodologically complementary and converge on one question.</p>

<div class="timeline">
  <div class="timeline-item">
    <div class="timeline-mark">
      <span class="timeline-year">2023 –</span>
    </div>
    <div class="timeline-body">
      <h3><span class="lang-zh">大连理工大学 · 环境科学与工程 · 博士</span><span class="lang-en">Dalian University of Technology · Ph.D. in Environmental Science and Engineering</span></h3>
      <p class="lang-zh">导师：姬国钊 教授。研究方向为废弃物焚烧的智能多相流建模，预计 2027 年毕业。</p>
      <p class="lang-en">Supervisor: Prof. Guozhao Ji. Research on intelligent multiphase flow modeling for waste incineration; expected graduation 2027.</p>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-mark">
      <span class="timeline-year">2025 – 2026</span>
    </div>
    <div class="timeline-body">
      <h3><span class="lang-zh">东京科学大学（原东京工业大学）· Cross 实验室 · 联合培养</span><span class="lang-en">Institute of Science Tokyo (formerly Tokyo Tech) · Cross Laboratory · Joint PhD</span></h3>
      <p class="lang-zh">导师：<a href="https://zh.clab-tokyotech.org/">Jeffrey S. Cross 教授</a>。为期一年的联合培养，由国家公派留学基金（CSC）资助。</p>
      <p class="lang-en">Supervisor: <a href="https://zh.clab-tokyotech.org/">Prof. Jeffrey S. Cross</a>. One-year joint PhD training funded by the China Scholarship Council (CSC).</p>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-mark">
      <span class="timeline-year">2026.09 – 2027.03</span>
    </div>
    <div class="timeline-body">
      <h3><span class="lang-zh">卢森堡大学 · 联合培养</span><span class="lang-en">University of Luxembourg · Joint PhD Visit</span></h3>
      <p class="lang-zh">导师：Bradley P. Ladewig 教授。为期 6 个月，获大连理工大学"连理全球"留学专项资助。</p>
      <p class="lang-en">Supervisor: Prof. Bradley P. Ladewig. Six-month research visit funded by the DUT Global Vision Project.</p>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-mark">
      <span class="timeline-year">2020 – 2023</span>
    </div>
    <div class="timeline-body">
      <h3><span class="lang-zh">中央民族大学 · 环境科学与工程 · 硕士</span><span class="lang-en">Minzu University of China · M.S. in Environmental Science and Engineering</span></h3>
      <p class="lang-zh">研究方向为深海多金属结核流态化采集的流场参数匹配。</p>
      <p class="lang-en">Research on flow-field parameter matching for fluidized collection of deep-sea polymetallic nodules.</p>
    </div>
  </div>
</div>

<h2><span class="lang-zh">成果概览</span><span class="lang-en">Output at a Glance</span></h2>

<div class="metrics">
  <div class="metric">
    <div class="metric-value">{{ site.publications | where: "category", "manuscripts" | size }}</div>
    <div class="metric-label"><span class="lang-zh">期刊论文</span><span class="lang-en">Journal articles</span></div>
    <div class="metric-note"><span class="lang-zh">其中第一作者 5 篇</span><span class="lang-en">5 as first author</span></div>
  </div>

  <div class="metric">
    <div class="metric-value">{{ site.publications | where: "category", "patents" | size }}</div>
    <div class="metric-label"><span class="lang-zh">授权专利</span><span class="lang-en">Patents</span></div>
    <div class="metric-note"><span class="lang-zh">发明、实用新型与申请公布</span><span class="lang-en">Invention, utility model and published</span></div>
  </div>

  <div class="metric">
    <div class="metric-value">{{ site.publications | where: "category", "software" | size }}</div>
    <div class="metric-label"><span class="lang-zh">软件著作权</span><span class="lang-en">Software copyrights</span></div>
    <div class="metric-note"><span class="lang-zh">燃烧与流场仿真工具</span><span class="lang-en">Combustion and flow simulation tools</span></div>
  </div>

  <div class="metric">
    <div class="metric-value">{{ site.data.scholar.total_citations }}</div>
    <div class="metric-label"><span class="lang-zh">总被引</span><span class="lang-en">Citations</span></div>
    <div class="metric-note">h-index {{ site.data.scholar.h_index }} · i10 {{ site.data.scholar.i10_index }}</div>
  </div>

  <div class="metric">
    <div class="metric-value">5</div>
    <div class="metric-label"><span class="lang-zh">科研项目</span><span class="lang-en">Projects</span></div>
    <div class="metric-note"><span class="lang-zh">含国家重点研发计划</span><span class="lang-en">Incl. National Key R&amp;D Program</span></div>
  </div>
</div>

<p class="metrics-foot">
  <span class="lang-zh">另有团体标准 1 项（参编）、科技成果转化 1 项（转让金额 40 万元）。引用数据更新于 {{ site.data.scholar.updated_at | date: "%Y-%m" }}，来源 Google Scholar。</span>
  <span class="lang-en">Additionally: one group standard (participating drafter) and one technology transfer (RMB 400,000). Citation data as of {{ site.data.scholar.updated_at | date: "%Y-%m" }}, via Google Scholar.</span>
</p>

<h2><span class="lang-zh">研究方向</span><span class="lang-en">Research Interests</span></h2>

<p class="lang-zh">我的研究围绕一条主线展开：<strong>如何让难处理的工业废弃物流在焚烧过程中变得可预测、可控制。</strong>具体分为三个相互支撑的层面。</p>
<p class="lang-en">My research follows one central thread: <strong>how to make difficult industrial waste streams predictable and controllable during incineration.</strong> It divides into three mutually supporting layers.</p>

<div class="home-grid">
  <div class="home-card">
    <h3><i class="fa-solid fa-wind" aria-hidden="true"></i> <span class="lang-zh">CFD 数值模拟</span><span class="lang-en">CFD Simulation</span></h3>
    <p class="lang-zh">多相流、燃烧与传热过程的欧拉-拉格朗日建模，覆盖实验室规模到工业规模。</p>
    <p class="lang-en">Eulerian-Lagrangian modeling of multiphase flow, combustion and heat transfer, from lab scale to industrial scale.</p>
  </div>
  <div class="home-card">
    <h3><i class="fa-solid fa-brain" aria-hidden="true"></i> <span class="lang-zh">AI 流场预测</span><span class="lang-en">AI Flow Prediction</span></h3>
    <p class="lang-zh">机器学习与神经网络代理模型（如输入凸神经网络）用于流场快速预测与非牛顿流体建模。</p>
    <p class="lang-en">Machine learning and neural network surrogates (e.g. input-convex neural networks) for fast flow prediction and non-Newtonian fluid modeling.</p>
  </div>
  <div class="home-card">
    <h3><i class="fa-solid fa-industry" aria-hidden="true"></i> <span class="lang-zh">设备设计与优化</span><span class="lang-en">Equipment Design</span></h3>
    <p class="lang-zh">焚烧炉、循环流化床、双流体喷嘴等装备的流场设计、防堵与运行优化。</p>
    <p class="lang-en">Flow field design, anti-clogging and operational optimization of incinerators, circulating fluidized beds and twin-fluid nozzles.</p>
  </div>
</div>

<h2><span class="lang-zh">近期动态</span><span class="lang-en">Recent News</span></h2>

<ul class="news-list">
  <li><strong>2026.09</strong><span class="lang-zh">赴卢森堡大学开展为期 6 个月的联合培养（大连理工大学"连理全球"留学专项资助）。</span><span class="lang-en">Started a 6-month joint PhD visit at the University of Luxembourg (DUT Global Vision Project).</span></li>
  <li><strong>2026.09</strong><span class="lang-zh">获得大连理工大学博士生卓越奖学金、研究生单项奖（智育单项）。</span><span class="lang-en">Awarded the Doctoral Excellence Scholarship and the Graduate Individual Scholarship (Academic Excellence) at DUT.</span></li>
  <li><strong>2026.07</strong><span class="lang-zh">参加沈阳"2026 年固体废物绿色发展交流会"（中华环保联合会主办）并作口头报告。</span><span class="lang-en">Delivered an oral presentation at the 2026 Green Development Exchange on Solid Waste in Shenyang.</span></li>
  <li><strong>2026.06</strong><span class="lang-zh">参加首届环境纳米技术国际研讨会（ISEN 2026，大连）并获最佳墙报奖。</span><span class="lang-en">Received the Best Poster Award at ISEN 2026, Dalian.</span></li>
  <li><strong>2026.04</strong><span class="lang-zh">导师的导师 <a href="https://chemeng.uq.edu.au/profile/7851/joe-diniz-da-costa">Joe Diniz da Costa</a> 教授来访大连理工大学并做客 CGTN RADIO 访谈。</span><span class="lang-en"><a href="https://chemeng.uq.edu.au/profile/7851/joe-diniz-da-costa">Prof. Joe Diniz da Costa</a> visited DUT and joined a CGTN RADIO interview.</span></li>
</ul>

<p class="news-more">
  <a href="{{ '/year-archive/' | relative_url }}">
    <span class="lang-zh">全部动态</span><span class="lang-en">All moments</span>
    <span aria-hidden="true">→</span>
  </a>
</p>

<div class="home-figure">
  <img src="{{ '/images/g1.gif' | relative_url }}" loading="lazy" alt="Simulation animation: rotary kiln and neural network">
  <div class="home-figure-caption">
    <span class="lang-zh">回转窑与神经网络的耦合仿真</span>
    <span class="lang-en">Coupled simulation of a rotary kiln and neural network</span>
  </div>
</div>

<h2><span class="lang-zh">联系方式</span><span class="lang-en">Contact</span></h2>

<p class="lang-zh">欢迎就多相流建模、CFD 与人工智能交叉方向交流合作。邮件是最可靠的联系方式，微信同号可加。</p>
<p class="lang-en">I welcome collaboration on multiphase flow modeling, CFD and AI. Email is the most reliable channel; WeChat is also available.</p>

<ul class="contact-list">
  <li><span class="contact-label"><span class="lang-zh">邮箱</span><span class="lang-en">Email</span></span><a href="mailto:dkz@mail.dlut.edu.cn">dkz@mail.dlut.edu.cn</a></li>
  <li>
    <span class="contact-label">WeChat</span>
    <span class="contact-value">
      DK-techie
      <button class="contact-copy-btn" data-copy="DK-techie" type="button" aria-label="Copy WeChat ID">
        <i class="fas fa-copy" aria-hidden="true"></i>
      </button>
      <span class="copy-feedback" role="status" aria-live="polite"></span>
    </span>
  </li>
  <li><span class="contact-label">Google Scholar</span><a href="https://scholar.google.com/citations?user=_R1WLLgAAAAJ&hl=en">Profile</a></li>
  <li><span class="contact-label">ORCID</span><a href="https://orcid.org/0009-0000-4584-7246">0009-0000-4584-7246</a></li>
</ul>
