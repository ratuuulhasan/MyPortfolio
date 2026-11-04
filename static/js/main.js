// ============ THEME TOGGLE ============
(function () {
    const html = document.documentElement;
    const saved = localStorage.getItem('theme') || 'light';
    html.setAttribute('data-theme', saved);
})();

function toggleTheme() {
    const html = document.documentElement;
    const next = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    html.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    updateThemeIcon();
    // re-init AOS after theme change (colors)
    if (window.AOS) setTimeout(() => AOS.refresh(), 100);
}

function updateThemeIcon() {
    const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
    document.querySelectorAll('.theme-toggle i').forEach(i => {
        i.className = isDark ? 'bi bi-sun-fill' : 'bi bi-moon-stars-fill';
    });
}

// ============ SCROLL PROGRESS + NAVBAR ============
window.addEventListener('scroll', () => {
    const doc = document.documentElement;
    const scrolled = (doc.scrollTop / (doc.scrollHeight - doc.clientHeight)) * 100;
    const bar = document.getElementById('scroll-progress');
    if (bar) bar.style.width = scrolled + '%';

    const nav = document.querySelector('.navbar-custom');
    if (nav) nav.classList.toggle('scrolled', window.scrollY > 50);
});

// ============ TYPING EFFECT ============
function initTyping() {
    const el = document.getElementById('typed');
    if (!el) return;
    const words = (el.dataset.words || '').split('|').filter(Boolean);
    if (!words.length) return;

    let wordIndex = 0, charIndex = 0, deleting = false;

    function tick() {
        const word = words[wordIndex];
        el.textContent = word.substring(0, charIndex);

        if (!deleting) {
            if (charIndex < word.length) { charIndex++; setTimeout(tick, 100); }
            else { deleting = true; setTimeout(tick, 1500); }
        } else {
            if (charIndex > 0) { charIndex--; setTimeout(tick, 50); }
            else { deleting = false; wordIndex = (wordIndex + 1) % words.length; setTimeout(tick, 300); }
        }
    }
    tick();
}

// ============ INIT ============
document.addEventListener('DOMContentLoaded', () => {
    updateThemeIcon();
    initTyping();

    // AOS
    if (window.AOS) {
        AOS.init({
            duration: 800,
            once: true,
            offset: 80,
            easing: 'ease-out-cubic',
        });
    }

    // Auto-dismiss alerts
    setTimeout(() => {
        document.querySelectorAll('.alert-dismissible').forEach(el => {
            const btn = el.querySelector('.btn-close');
            if (btn) btn.click();
        });
    }, 5000);

    // Animate skill progress bars when visible
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(e => {
            if (e.isIntersecting) {
                const bar = e.target;
                bar.style.width = bar.dataset.level + '%';
                observer.unobserve(bar);
            }
        });
    }, { threshold: 0.3 });

    document.querySelectorAll('.progress-bar[data-level]').forEach(b => {
        b.style.width = '0%';
        observer.observe(b);
    });
});

// ============ SMOOTH SCROLL & REMOVE HASH ============
document.addEventListener('DOMContentLoaded', () => {
    const links = document.querySelectorAll('a[href^="/#"], a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            const targetId = href.replace('/#', '').replace('#', '');
            
            if (!targetId) return; 

            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                e.preventDefault(); 
                const offset = 80; 
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - offset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });

                history.pushState("", document.title, window.location.pathname + window.location.search);
            }
        });
    });

    if (window.location.hash) {
        setTimeout(() => {
            history.replaceState(null, null, window.location.pathname + window.location.search);
        }, 100);
    }
});

window.addEventListener('load', () => {
    const preloader = document.getElementById('preloader');
    if(preloader) {
        preloader.style.opacity = '0';
        setTimeout(() => preloader.style.display = 'none', 500);
    }
});