
document.addEventListener("DOMContentLoaded", function () {
  // 1. Scroll Animations (IntersectionObserver)
  const animatedSections = document.querySelectorAll(".animated-section");

  const observerOptions = {
    root: null, // Use the viewport as the root
    rootMargin: "0px",
    threshold: 0.15, // Trigger when 15% of the element is visible
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target); // Run animation only once
      }
    });
  }, observerOptions);

  animatedSections.forEach((section) => {
    observer.observe(section);
  });

  // 2. Cookie Banner Logic
  const cookieBanner = document.querySelector(".cookie-banner");
  const acceptButton = document.querySelector(".btn-accept");

  if (cookieBanner && acceptButton) {
    if (!localStorage.getItem("cookieConsent")) {
      cookieBanner.style.display = "flex";
    }

    acceptButton.addEventListener("click", function () {
      localStorage.setItem("cookieConsent", "true");
      cookieBanner.style.display = "none";
    });
  }

  // 3. Mobile Menu Logic
  const mobileMenuBtn = document.querySelector(".mobile-menu-btn");
  const mobileMenuOverlay = document.querySelector(".mobile-menu-overlay");
  const mobileMenuClose = document.querySelector(".mobile-menu-close");
  const mobileLinks = document.querySelectorAll(".nav-link-mobile");

  function toggleMenu() {
    const isHidden = mobileMenuOverlay.style.display === "none" || !mobileMenuOverlay.style.display;
    mobileMenuOverlay.style.display = isHidden ? "flex" : "none";
    document.body.style.overflow = isHidden ? "hidden" : "";
  }

  if (mobileMenuBtn && mobileMenuOverlay && mobileMenuClose) {
    mobileMenuBtn.addEventListener("click", toggleMenu);
    mobileMenuClose.addEventListener("click", toggleMenu);

    // Close menu when clicking a link
    mobileLinks.forEach(link => {
      link.addEventListener("click", toggleMenu);
    });
  }
});
