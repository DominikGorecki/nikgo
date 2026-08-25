document.addEventListener('DOMContentLoaded', () => {
  const themeToggle = document.getElementById('theme-toggle');
  const darkIcon = document.getElementById('theme-toggle-dark-icon');
  const lightIcon = document.getElementById('theme-toggle-light-icon');
  const updateIcons = () => {
    if (!themeToggle || !darkIcon || !lightIcon) return;
    const dark = document.documentElement.classList.contains('dark');
    darkIcon.classList.toggle('hidden', dark);
    lightIcon.classList.toggle('hidden', !dark);
    themeToggle.setAttribute('aria-pressed', String(dark));
  };
  updateIcons();
  themeToggle?.addEventListener('click', () => {
    document.documentElement.classList.toggle('dark');
    try { localStorage.setItem('theme', document.documentElement.classList.contains('dark') ? 'dark' : 'light'); } catch (_) {}
    updateIcons();
  });

  const progressBar = document.getElementById('scroll-progress-bar');
  const backToTop = document.getElementById('back-to-top');
  const nav = document.querySelector('.sticky-nav');
  let queued = false;
  const updateScrollUi = () => {
    const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    if (progressBar) progressBar.style.width = `${height > 0 ? (scrollTop / height) * 100 : 0}%`;
    backToTop?.classList.toggle('show', scrollTop > 300);
    nav?.classList.toggle('scrolled', scrollTop > 50);
    queued = false;
  };
  window.addEventListener('scroll', () => {
    if (!queued) { queued = true; window.requestAnimationFrame(updateScrollUi); }
  }, { passive: true });
  updateScrollUi();
  backToTop?.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
});
