
  document.addEventListener("DOMContentLoaded", () => {
    const animatedElements = document.querySelectorAll(".animate-on-scroll");

    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add("active");
        }
      });
    }, {
      threshold: 0.2,
    });

    animatedElements.forEach(el => observer.observe(el));
  });

