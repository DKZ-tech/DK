/* ==========================================================================
 * Language toggle (zh / en)
 * Works together with the inline <script> in _includes/head.html which sets
 * the initial `lang-zh` / `lang-en` class on <html> before first paint.
 * Visible text is wrapped in <span class="lang-zh">…</span> /
 * <span class="lang-en">…</span>; CSS hides the inactive language.
 * ========================================================================== */
(function () {
  'use strict';

  var STORAGE_KEY = 'dk-site-lang';

  function detect() {
    var saved = null;
    try { saved = window.localStorage.getItem(STORAGE_KEY); } catch (e) { /* private mode */ }
    if (saved === 'zh' || saved === 'en') return saved;
    var nav = (navigator.language || navigator.userLanguage || 'en').toLowerCase();
    return nav.indexOf('zh') === 0 ? 'zh' : 'en';
  }

  function apply(lang) {
    var root = document.documentElement;
    root.classList.remove('lang-zh', 'lang-en');
    root.classList.add('lang-' + lang);
    root.setAttribute('lang', lang === 'zh' ? 'zh-CN' : 'en');
  }

  // Set the language as early as possible (also done inline in head.html to
  // avoid a flash of both languages before this deferred script runs).
  apply(detect());

  document.addEventListener('DOMContentLoaded', function () {
    var buttons = document.querySelectorAll('[data-lang-toggle]');
    Array.prototype.forEach.call(buttons, function (btn) {
      btn.addEventListener('click', function (evt) {
        evt.preventDefault();
        var current = document.documentElement.classList.contains('lang-zh') ? 'zh' : 'en';
        var next = current === 'zh' ? 'en' : 'zh';
        try { window.localStorage.setItem(STORAGE_KEY, next); } catch (e) { /* ignore */ }
        apply(next);
      });
    });

    // Copy WeChat ID to clipboard on the homepage contact card
    var copyBtn = document.querySelector('.copy-wechat-btn');
    var feedback = document.getElementById('copy-feedback');
    if (copyBtn) {
      copyBtn.addEventListener('click', function () {
        var text = copyBtn.getAttribute('data-clipboard-text') || '';
        function show(ok) {
          if (!feedback) return;
          var isZh = document.documentElement.classList.contains('lang-zh');
          feedback.textContent = ok
            ? (isZh ? '已复制到剪贴板' : 'Copied to clipboard')
            : (isZh ? '复制失败，请手动选中复制' : 'Copy failed; please select and copy manually');
          feedback.className = 'copy-feedback ' + (ok ? 'copy-success' : 'copy-error');
          setTimeout(function () {
            feedback.textContent = '';
            feedback.className = 'copy-feedback';
          }, 2500);
        }
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(text).then(function () { show(true); }, function () { show(false); });
        } else {
          // Fallback for older browsers / non-secure contexts
          try {
            var ta = document.createElement('textarea');
            ta.value = text;
            ta.setAttribute('readonly', '');
            ta.style.position = 'absolute';
            ta.style.left = '-9999px';
            document.body.appendChild(ta);
            ta.select();
            document.execCommand('copy');
            document.body.removeChild(ta);
            show(true);
          } catch (e) {
            show(false);
          }
        }
      });
    }
  });
})();
