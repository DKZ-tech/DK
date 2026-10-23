---
permalink: /
layout: splash
title: '<span class="lang-zh">首页</span><span class="lang-en">Home</span>'
author_profile: false
body_class: paper-page
---

{% include base_path %}

{% assign selected = site.publications | where: 'selected', true | sort: 'date' | reverse %}

<div class="landing">

  <header class="landing__hero">
    <div class="landing__hero-text">
      <p class="landing__eyebrow">
        <span class="lang-zh">环境工程 · 多相流建模</span>
        <span class="lang-en">Environmental Engineering · Multiphase Flow Modeling</span>
      </p>

      <h1 class="landing__name">
        <span class="lang-zh">张东宽</span><span class="lang-en">Dongkuan Zhang</span>
      </h1>

      <p class="landing__role">
        <span class="lang-zh">大连理工大学 环境学院 · 博士研究生</span>
        <span class="lang-en">PhD Student · School of Environmental Science &amp; Engineering<br>Dalian University of Technology</span>
      </p>

      <p class="landing__tagline">
        <span class="lang-zh">工业焚烧炉里的高盐残渣常常烧不透，喷嘴也总是堵。我用 CFD 与神经网络，让这类劣质燃料的流动与燃烧变得可预测、可预警、可优化。</span>
        <span class="lang-en">High-salt residues in industrial incinerators often burn incompletely, and the nozzles keep clogging. I combine CFD with neural networks to make the flow and combustion of such difficult fuels predictable, warnable and optimizable.</span>
      </p>

      <ul class="landing__contact">
        <li><a href="mailto:1159571393@qq.com">1159571393@qq.com</a></li>
        <li><span>WeChat · DK-techie</span></li>
        <li><a href="https://scholar.google.com/citations?user=_R1WLLgAAAAJ&amp;hl=en">Google Scholar</a></li>
        <li><a href="https://orcid.org/0009-0000-4584-7246">ORCID</a></li>
      </ul>
    </div>

    <figure class="landing__portrait">
      <img src="{{ '/images/profile1.jpg' | relative_url }}" alt="Dongkuan Zhang — 张东宽" width="400" height="533" loading="eager">
    </figure>
  </header>

  <section class="landing__section">
    <h2 class="landing__heading">
      <span class="lang-zh">精选成果</span><span class="lang-en">Selected Work</span>
    </h2>

    <ol class="landing__index">
      {% for pub in selected %}
      <li class="landing__entry">
        <div class="landing__entry-head">
          <a class="landing__entry-title" href="{{ pub.url | relative_url }}">{{ pub.title }}</a>
        </div>
        <p class="landing__entry-meta">
          <span class="landing__venue">{{ pub.venue }}</span>
          {% if pub.citation_count and pub.citation_count > 0 %}
          <span class="landing__dot" aria-hidden="true">·</span>
          <span class="lang-zh">被引 {{ pub.citation_count }}</span>
          <span class="lang-en">cited {{ pub.citation_count }} times</span>
          {% endif %}
        </p>
      </li>
      {% endfor %}
    </ol>

    <p class="landing__more">
      <a href="{{ '/publications/' | relative_url }}">
        <span class="lang-zh">全部论文、专利与软件著作权</span>
        <span class="lang-en">All publications, patents and software</span>
        <span class="landing__arrow" aria-hidden="true">→</span>
      </a>
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
      <span class="landing__row-desc"><span class="lang-zh">研究兴趣、教育经历与近期动态</span><span class="lang-en">Research interests, education and recent news</span></span>
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
