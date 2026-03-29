/**
 * Hexavara Language Switcher
 * -------------------------------------------------------
 * Uses data-i18n attribute to mark translatable elements.
 * Each translatable element has data-en and data-id attributes.
 * Works with textContent by default; use data-i18n="html" for innerHTML.
 */
(function () {
    function applyLanguage(lang) {
        localStorage.setItem('hex-lang', lang);
        document.documentElement.lang = lang === 'id' ? 'id' : 'en';

        // Swap text content
        document.querySelectorAll('[data-i18n]').forEach(function (el) {
            var text = el.getAttribute('data-' + lang);
            if (!text) return;
            if (el.getAttribute('data-i18n') === 'html') {
                el.innerHTML = text;
            } else {
                el.textContent = text;
            }
        });

        // Update switcher button states
        var switcher = document.getElementById('lang-switcher');
        if (switcher) {
            switcher.querySelectorAll('button').forEach(function (btn) {
                if (btn.dataset.lang === lang) {
                    btn.classList.add('active', 'bg-white', 'shadow-sm');
                    btn.classList.remove('text-gray-500');
                } else {
                    btn.classList.remove('active', 'bg-white', 'shadow-sm');
                    btn.classList.add('text-gray-500');
                }
            });
        }

        // Trigger a custom event for other scripts to listen to
        window.dispatchEvent(new CustomEvent('languageChanged', { detail: { lang: lang } }));
    }

    // Expose globally
    window.hexLanguage = {
        apply: applyLanguage,
        get: function() { return localStorage.getItem('hex-lang') || 'en'; }
    };

    // Bind click events
    var switcher = document.getElementById('lang-switcher');
    if (switcher) {
        switcher.querySelectorAll('button').forEach(function (btn) {
            btn.addEventListener('click', function () {
                applyLanguage(btn.dataset.lang);
            });
        });
    }

    // Init on load
    var saved = localStorage.getItem('hex-lang') || 'en';
    applyLanguage(saved);
})();
