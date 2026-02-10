document.addEventListener('DOMContentLoaded', () => {
  // --- Dark Mode Toggle ---
  const themeToggle = document.getElementById('theme-toggle');
  const darkIcon = document.getElementById('theme-toggle-dark-icon');
  const lightIcon = document.getElementById('theme-toggle-light-icon');

  // Sync icons with current theme
  const updateIcons = () => {
    if (document.documentElement.classList.contains('dark')) {
      darkIcon.classList.add('hidden');
      lightIcon.classList.remove('hidden');
    } else {
      darkIcon.classList.remove('hidden');
      lightIcon.classList.add('hidden');
    }
  };

  updateIcons();

  themeToggle.addEventListener('click', () => {
    document.documentElement.classList.toggle('dark');
    const isDark = document.documentElement.classList.contains('dark');
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
    updateIcons();
  });

  // --- Scroll Progress Bar ---
  const progressBar = document.getElementById('scroll-progress-bar');
  window.addEventListener('scroll', () => {
    const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = (winScroll / height) * 100;
    if (progressBar) {
      progressBar.style.width = scrolled + "%";
    }

    // --- Header Parallax & Fade ---
    const header = document.querySelector('.page-header-v2');
    const animatedBg = document.querySelector('.animated-bg');
    if (header && animatedBg) {
      const headerHeight = header.offsetHeight;
      const scrollFraction = Math.min(winScroll / headerHeight, 1);
      
      // Subtly move the background down as we scroll
      animatedBg.style.transform = `translateY(${winScroll * 0.4}px)`;
      
      // Decrease opacity from 0.8 down to 0.1 as we scroll
      const opacity = 0.8 - (scrollFraction * 0.7);
      animatedBg.style.opacity = opacity;
    }

    // Back to top visibility
    const backToTop = document.getElementById('back-to-top');
    if (backToTop) {
      if (winScroll > 300) {
        backToTop.classList.add('show');
      } else {
        backToTop.classList.remove('show');
      }
    }
  });

  const backToTop = document.getElementById('back-to-top');
  if (backToTop) {
    backToTop.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  // --- Scroll Animations (Intersection Observer) ---
  const observerOptions = {
    threshold: 0.1
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate-fade-in');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // Apply to sections and cards
  document.querySelectorAll('section, .card-item, .content-wrapper > *').forEach(el => {
    el.style.opacity = '0'; // Start hidden
    observer.observe(el);
  });

  // --- Image Lightbox / Zoom ---
  const images = document.querySelectorAll('.content-wrapper img');
  const overlay = document.createElement('div');
  overlay.className = 'img-overlay';
  document.body.appendChild(overlay);

  images.forEach(img => {
    img.addEventListener('click', () => {
      const fullImg = document.createElement('img');
      fullImg.src = img.src;
      overlay.innerHTML = '';
      overlay.appendChild(fullImg);
      overlay.classList.add('show');
    });
  });

  overlay.addEventListener('click', () => {
    overlay.classList.remove('show');
  });

  // --- Original Button Animation (Modernized) ---
  const buttons = document.querySelectorAll('.on-click');
  buttons.forEach(btn => {
    btn.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href && !href.startsWith('#')) {
        e.preventDefault();
        this.classList.add('clicked');
        setTimeout(() => {
          window.location.href = href;
        }, 250);
      }
    });
  });

  // Handle sticky nav transparency on scroll
  const nav = document.querySelector('.sticky-nav');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      nav.style.padding = "0.5rem 0";
      nav.style.boxShadow = "var(--card-shadow)";
    } else {
      nav.style.padding = "0.75rem 0";
      nav.style.boxShadow = "none";
    }
  });
});
