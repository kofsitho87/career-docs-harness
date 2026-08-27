(() => {
  const slides = Array.from(document.querySelectorAll('.slide'));
  const current = document.getElementById('current-slide');

  const go = (index) => {
    const bounded = Math.max(0, Math.min(slides.length - 1, index));
    slides[bounded]?.scrollIntoView({ behavior: 'smooth', block: 'start' });
  };

  const activeIndex = () => {
    const viewportMiddle = window.scrollY + window.innerHeight / 2;
    return Math.max(0, slides.findIndex((slide) => slide.offsetTop + slide.offsetHeight > viewportMiddle));
  };

  const update = () => {
    if (current) current.textContent = String(activeIndex() + 1);
  };

  document.addEventListener('keydown', (event) => {
    const index = activeIndex();
    if (['ArrowRight', 'ArrowDown', 'PageDown', ' '].includes(event.key)) {
      event.preventDefault();
      go(index + 1);
    } else if (['ArrowLeft', 'ArrowUp', 'PageUp'].includes(event.key)) {
      event.preventDefault();
      go(index - 1);
    } else if (event.key === 'Home') {
      event.preventDefault();
      go(0);
    } else if (event.key === 'End') {
      event.preventDefault();
      go(slides.length - 1);
    }
  });

  window.addEventListener('scroll', update, { passive: true });
  update();
})();
