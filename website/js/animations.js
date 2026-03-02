
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

  // 4. Active Nav Link Logic
  const navLinks = document.querySelectorAll(".nav-link, .nav-link-mobile");

  function updateActiveLink() {
    const isHomePage = document.getElementById("features") !== null;

    if (isHomePage) {
      const currentHash = window.location.hash || "#";

      navLinks.forEach((link) => {
        const href = link.getAttribute("href");
        if (
          href === currentHash ||
          (currentHash === "#" && (href === "#" || href === "./"))
        ) {
          const parent = link.closest(".main-nav, .mobile-nav-links");
          if (parent) {
            parent
              .querySelectorAll(".active")
              .forEach((el) => el.classList.remove("active"));
            link.classList.add("active");
          }
        }
      });
    }
  }

  // Run on load and hash change
  updateActiveLink();
  window.addEventListener("hashchange", updateActiveLink);
});
