---
permalink: /
layout: splash
title: '<span class="lang-zh">首页</span><span class="lang-en">Home</span>'
author_profile: false
---

{% include base_path %}

{% assign selected = site.publications | where: 'selected', true | sort: 'date' | reverse %}

<div class="landing">

  <section class="landing__hero">
    <img class="landing__avatar" src="{{ '/images/profile1.jpg' | relative_url }}" alt="Dongkuan Zhang — 张东宽" width="128" height="128" loading="eager">

    <div class="landing__intro">
      <h1 class="landing__name">
        <span class="lang-zh">张东宽</span><span class="lang-en">Dongkuan Zhang</span>
      </h1>
      <p class="landing__role">
        <span class="lang-zh">大连理工大学 环境学院 · 博士研究生</span>
        <span class="lang-en">PhD Student, School of Environmental Science &amp; Engineering, Dalian University of Technology</span>
      </p>
      <p class="landing__tagline">
        <span class="lang-zh">工业焚烧炉里的高盐残渣常常烧不透，喷嘴也总是堵。我想用 CFD 加神经网络，让这类劣质燃料的流动与燃烧变得可预测、可预警、可优化。</span>
        <span class="lang-en">High-salt residues inside industrial incinerators often burn incompletely, and the nozzles keep clogging. I use CFD together with neural networks to make the flow and combustion of such difficult fuels predictable, warnable and optimizable.</span>
      </p>

      <ul class="landing__contact">
        <li><i class="fa-solid fa-envelope" aria-hidden="true"></i><a href="mailto:1159571393@qq.com">1159571393@qq.com</a></li>
        <li><i class="fab fa-weixin" aria-hidden="true"></i><span>DK-techie</span></li>
        <li><i class="fa-solid fa-location-dot" aria-hidden="true"></i><span class="lang-zh">中国·大连</span><span class="lang-en">Dalian, China</span></li>
        <li><i class="ai ai-google-scholar" aria-hidden="true"></i><a href="https://scholar.google.com/citations?user=_R1WLLgAAAAJ&amp;hl=en">Google Scholar</a></li>
        <li><i class="ai ai-orcid" aria-hidden="true"></i><a href="https://orcid.org/0009-0000-4584-7246">ORCID</a></li>
      </ul>
    </div>
  </section>

  <section class="landing__section">
    <h2 class="landing__heading">
      <span class="lang-zh">精选成果</span><span class="lang-en">Selected Work</span>
    </h2>

    <ul class="landing__work">
      {% for pub in selected %}
      <li class="landing__work-item">
        <a class="landing__work-title" href="{{ pub.url | relative_url }}">{{ pub.title }}</a>
        <div class="landing__work-meta">
          <span class="landing__journal">{{ pub.venue }}</span>
          {% if pub.citation_count and pub.citation_count > 0 %}
            <span class="landing__cites">
              <span class="lang-zh">被引 {{ pub.citation_count }}</span>
              <span class="lang-en">{{ pub.citation_count }} citations</span>
            </span>
          {% endif %}
        </div>
      </li>
      {% endfor %}
    </ul>

    <p class="landing__more">
      <a href="{{ '/publications/' | relative_url }}">
        <span class="lang-zh">全部论文、专利与软件著作权 →</span>
        <span class="lang-en">All publications, patents and software →</span>
      </a>
    </p>
  </section>

  <figure class="landing__figure">
    <img src="{{ '/images/g0.gif' | relative_url }}" alt="Research animation: CFD coupled with neural networks">
    <figcaption>
      <span class="lang-zh">CFD 与神经网络耦合的智能多相流建模流程</span>
      <span class="lang-en">Intelligent multiphase flow modeling: coupling CFD with neural networks</span>
    </figcaption>
  </figure>

  <nav class="landing__cards" aria-label="Site sections">

    <a class="landing__card" href="{{ '/about/' | relative_url }}">
      <span class="landing__card-icon"><i class="fa-solid fa-user" aria-hidden="true"></i></span>
      <span class="landing__card-title"><span class="lang-zh">个人简介</span><span class="lang-en">About</span></span>
      <span class="landing__card-desc">
        <span class="lang-zh">研究兴趣、教育经历与近期动态。</span>
        <span class="lang-en">Research interests, education and recent news.</span>
      </span>
    </a>

    <a class="landing__card" href="{{ '/publications/' | relative_url }}">
      <span class="landing__card-icon"><i class="fa-solid fa-book-open" aria-hidden="true"></i></span>
      <span class="landing__card-title"><span class="lang-zh">论文成果</span><span class="lang-en">Publications</span></span>
      <span class="landing__card-desc">
        <span class="lang-zh">期刊论文、授权专利、软著与标准。</span>
        <span class="lang-en">Journal articles, granted patents, software and standards.</span>
      </span>
    </a>

    <a class="landing__card" href="{{ '/cv/' | relative_url }}">
      <span class="landing__card-icon"><i class="fa-solid fa-file-lines" aria-hidden="true"></i></span>
      <span class="landing__card-title"><span class="lang-zh">简历</span><span class="lang-en">Curriculum Vitae</span></span>
      <span class="landing__card-desc">
        <span class="lang-zh">完整学术简历，可下载中英文 PDF。</span>
        <span class="lang-en">Full academic CV, with Chinese and English PDFs.</span>
      </span>
    </a>

    <a class="landing__card" href="{{ '/year-archive/' | relative_url }}">
      <span class="landing__card-icon"><i class="fa-solid fa-clock-rotate-left" aria-hidden="true"></i></span>
      <span class="landing__card-title"><span class="lang-zh">动态</span><span class="lang-en">Moments</span></span>
      <span class="landing__card-desc">
        <span class="lang-zh">获奖、会议与学术交流记录。</span>
        <span class="lang-en">Awards, conferences and academic exchanges.</span>
      </span>
    </a>

  </nav>

  <footer class="landing__footer">
    <span class="lang-zh">欢迎就多相流建模、CFD 与 AI 交叉方向交流合作。</span>
    <span class="lang-en">Open to collaboration on multiphase flow modeling, CFD and AI.</span>
  </footer>

</div>
