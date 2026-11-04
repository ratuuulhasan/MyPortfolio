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
                const offset = 100; 
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

// ============ PREMIUM: 3D TILT EFFECT ON CARDS ============
document.addEventListener('DOMContentLoaded', () => {
    const tiltCards = document.querySelectorAll('.project-card, .blog-card, .cert-card');
    
    if (window.matchMedia("(pointer: fine)").matches) {
        tiltCards.forEach(card => {
            card.addEventListener('mousemove', (e) => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                const centerX = rect.width / 2;
                const centerY = rect.height / 2;
                
                const rotateX = ((y - centerY) / centerY) * -5;
                const rotateY = ((x - centerX) / centerX) * 5;
                
                card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
                card.style.transition = 'transform 0.1s ease';
            });
            
            card.addEventListener('mouseleave', () => {
                card.style.transform = `perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)`;
                card.style.transition = 'transform 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275)';
            });
        });
    }
});

// ============ PREMIUM: BACK TO TOP BUTTON ============
document.addEventListener('DOMContentLoaded', () => {
    const backToTopBtn = document.createElement('button');
    backToTopBtn.innerHTML = '<i class="bi bi-arrow-up"></i>';
    backToTopBtn.id = 'back-to-top';
    
    backToTopBtn.style.cssText = `
        position: fixed; bottom: 30px; right: 30px; width: 50px; height: 50px; border-radius: 50%;
        background: var(--gradient); color: #fff; border: none; font-size: 1.5rem; cursor: pointer;
        z-index: 9999; opacity: 0; visibility: hidden; transform: translateY(20px);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4); display: flex; align-items: center; justify-content: center;
    `;
    document.body.appendChild(backToTopBtn);

    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            backToTopBtn.style.opacity = '1'; backToTopBtn.style.visibility = 'visible'; backToTopBtn.style.transform = 'translateY(0)';
        } else {
            backToTopBtn.style.opacity = '0'; backToTopBtn.style.visibility = 'hidden'; backToTopBtn.style.transform = 'translateY(20px)';
        }
    });

    backToTopBtn.addEventListener('click', () => { window.scrollTo({ top: 0, behavior: 'smooth' }); });
    backToTopBtn.addEventListener('mouseenter', () => { backToTopBtn.style.transform = 'translateY(-5px) scale(1.1)'; });
    backToTopBtn.addEventListener('mouseleave', () => { backToTopBtn.style.transform = 'translateY(0) scale(1)'; });
});

// ============ INITIALIZATION ============
document.addEventListener('DOMContentLoaded', () => {
    updateThemeIcon();
    initTyping();

    if (window.AOS) {
        AOS.init({ duration: 800, once: true, offset: 100, easing: 'ease-out-cubic' });
    }

    setTimeout(() => {
        document.querySelectorAll('.alert-dismissible').forEach(el => {
            const btn = el.querySelector('.btn-close');
            if (btn) btn.click();
        });
    }, 5000);

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(e => {
            if (e.isIntersecting) {
                const bar = e.target; bar.style.width = bar.dataset.level + '%'; observer.unobserve(bar);
            }
        });
    }, { threshold: 0.3 });

    document.querySelectorAll('.progress-bar[data-level]').forEach(b => {
        b.style.width = '0%'; observer.observe(b);
    });
});

// ============ HIDE PRELOADER ============
window.addEventListener('load', () => {
    const preloader = document.getElementById('preloader');
    if(preloader) { preloader.style.opacity = '0'; setTimeout(() => preloader.style.display = 'none', 500); }
});