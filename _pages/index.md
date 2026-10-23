---
permalink: /
layout: splash
title: '<span class="lang-zh">首页</span><span class="lang-en">Home</span>'
author_profile: false
body_class: paper-page
---

{% include base_path %}

{% assign manuscripts = site.publications | where: "category", "manuscripts" | size %}
{% assign patents     = site.publications | where: "category", "patents" | size %}
{% assign software    = site.publications | where: "category", "software" | size %}

<div class="landing">

  <header class="landing__hero">
    <div class="landing__hero-text">
      <p class="landing__eyebrow">
        <span class="lang-zh">环境工程 · 智能多相流建模</span>
        <span class="lang-en">Environmental Engineering · Intelligent Multiphase Flow Modeling</span>
      </p>

      <h1 class="landing__name">
        <span class="lang-zh">张东宽</span><span class="lang-en">Dongkuan Zhang</span>
      </h1>

      <p class="landing__role">
        <span class="lang-zh">大连理工大学 环境学院 · 博士研究生</span>
        <span class="lang-en">PhD Candidate · School of Environmental Science &amp; Engineering<br>Dalian University of Technology</span>
      </p>

      <p class="landing__tagline">
        <span class="lang-zh">焚烧炉内部是一千度、不透明的黑箱：气固液多相湍流与热化学反应交织，几乎无法测量。我以 CFD 还原这场看不见的反应，再用神经网络把它压缩成毫秒级的预测——让废弃物焚烧从凭经验操作，走向可计算、可预警、可优化。</span>
        <span class="lang-en">Inside an incinerator is a thousand-degree black box: gas–solid–liquid turbulence entangled with thermochemical reaction, almost impossible to measure. I reconstruct that invisible chemistry with CFD, then compress it with neural networks into millisecond-scale prediction — moving waste incineration from rule-of-thumb operation toward something computable, anticipatory and optimizable.</span>
      </p>

      <ul class="landing__contact">
        <li><a href="mailto:dkz@mail.dlut.edu.cn">dkz@mail.dlut.edu.cn</a></li>
        <li><span>WeChat · DK-techie</span></li>
        <li><a href="https://scholar.google.com/citations?user=_R1WLLgAAAAJ&amp;hl=en">Google Scholar</a></li>
        <li><a href="https://orcid.org/0009-0000-4584-7246">ORCID</a></li>
      </ul>
    </div>

    <figure class="landing__portrait">
      <img src="{{ '/images/profile1.jpg' | relative_url }}" alt="Dongkuan Zhang — 张东宽" width="400" height="533" loading="eager">
    </figure>
  </header>

  <section class="landing__band">
    <div class="landing__metrics">
      <div class="landing__metric">
        <span class="landing__metric-value">{{ manuscripts }}</span>
        <span class="landing__metric-label"><span class="lang-zh">期刊论文</span><span class="lang-en">Papers</span></span>
      </div>
      <div class="landing__metric">
        <span class="landing__metric-value">{{ patents }}</span>
        <span class="landing__metric-label"><span class="lang-zh">授权专利</span><span class="lang-en">Patents</span></span>
      </div>
      <div class="landing__metric">
        <span class="landing__metric-value">{{ software }}</span>
        <span class="landing__metric-label"><span class="lang-zh">软件著作权</span><span class="lang-en">Software</span></span>
      </div>
      <div class="landing__metric">
        <span class="landing__metric-value">{{ site.data.scholar.total_citations }}</span>
        <span class="landing__metric-label"><span class="lang-zh">总被引</span><span class="lang-en">Citations</span></span>
      </div>
      <div class="landing__metric">
        <span class="landing__metric-value">{{ site.data.scholar.h_index }}</span>
        <span class="landing__metric-label">h-index</span>
      </div>
    </div>

    <p class="landing__band-note">
      <span class="lang-zh">三段联合培养：大连理工大学 · 东京科学大学（CSC 国家公派）· 卢森堡大学（连理全球专项）</span>
      <span class="lang-en">Joint training at Dalian University of Technology · Institute of Science Tokyo (CSC) · University of Luxembourg (DUT Global Vision)</span>
    </p>
  </section>

  <figure class="landing__figure">
    <img src="{{ '/images/g0.gif' | relative_url }}" alt="CFD coupled with neural networks">
    <figcaption>
      <span class="lang-zh">图 1　CFD 与神经网络耦合的智能多相流建模流程</span>
      <span class="lang-en">Fig. 1　Coupling CFD with neural networks for intelligent multiphase flow modeling</span>
    </figcaption>
  </figure>

  <nav class="landing__sections" aria-label="Site sections">
    <a class="landing__row" href="{{ '/about/' | relative_url }}">
      <span class="landing__row-title"><span class="lang-zh">个人简介</span><span class="lang-en">About</span></span>
      <span class="landing__row-desc"><span class="lang-zh">培养经历、成果概览与研究兴趣</span><span class="lang-en">Training, output overview and research interests</span></span>
      <span class="landing__arrow" aria-hidden="true">→</span>
    </a>
    <a class="landing__row" href="{{ '/publications/' | relative_url }}">
      <span class="landing__row-title"><span class="lang-zh">论文成果</span><span class="lang-en">Publications</span></span>
      <span class="landing__row-desc"><span class="lang-zh">期刊论文、授权专利、软著与标准</span><span class="lang-en">Journal articles, granted patents, software and standards</span></span>
      <span class="landing__arrow" aria-hidden="true">→</span>
    </a>
    <a class="landing__row" href="{{ '/cv/' | relative_url }}">
      <span class="landing__row-title"><span class="lang-zh">简历</span><span class="lang-en">Curriculum Vitae</span></span>
      <span class="landing__row-desc"><span class="lang-zh">完整学术简历，可下载中英文 PDF</span><span class="lang-en">Full academic CV, with Chinese and English PDFs</span></span>
      <span class="landing__arrow" aria-hidden="true">→</span>
    </a>
    <a class="landing__row" href="{{ '/year-archive/' | relative_url }}">
      <span class="landing__row-title"><span class="lang-zh">动态</span><span class="lang-en">Moments</span></span>
      <span class="landing__row-desc"><span class="lang-zh">获奖、会议与学术交流记录</span><span class="lang-en">Awards, conferences and academic exchanges</span></span>
      <span class="landing__arrow" aria-hidden="true">→</span>
    </a>
  </nav>

  <footer class="landing__footer">
    <span class="lang-zh">欢迎就多相流建模、CFD 与 AI 交叉方向交流合作</span>
    <span class="lang-en">Open to collaboration on multiphase flow modeling, CFD and AI</span>
  </footer>

</div>
