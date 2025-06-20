# Website Migration TODO List - website.tinygnomes.com

This document outlines the tasks required to migrate website.tinygnomes.com from Framer to our own servers, addressing identified issues and potential improvements.

## High Priority Tasks

*   **Cookie Dialog Functionality:**
    *   **Issue:** The "Accept" and "Decline" buttons on the cookie dialog at the bottom of the home page are non-functional. Framer likely handled analytics, which is no longer needed.
    *   **Proposed Solution:** Replace the existing cookie dialog with a static notice stating that the website only uses technical cookies (for logged-in users).
    *   **Affected File:** [`website.tinygnomes.com/index.html`](website.tinygnomes.com/index.html) (specifically the `data-framer-name="Policy"` div and its child buttons).

[COMPLETED] *   **Login Button Link:**
    *   **Issue:** The "Login" button currently does not perform any action.
    *   **Proposed Solution:** Update the login button to link directly to `https://www.tinygnomes.com/quilt.fcgi`.
    *   **Affected File:** [`website.tinygnomes.com/index.html`](website.tinygnomes.com/index.html) (specifically the `a` tag with `data-framer-name="Log in"`).

## Migration & Cleanup Tasks

*   **Remove Framer-Specific Code:**
    *   Remove Framer comments: `<!-- ✨ Built with Framer • https://www.framer.com/ -->`
    *   Remove Framer meta tags: `<meta name="generator" content="Framer bdd6aa1">`, `<meta name="framer-search-index" content="...">`
    *   Remove Framer analytics script: `<script async="" src="https://events.framer.com/script" data-fid="..."></script>`
    *   Remove Framer bundle script: `<script type="module" data-framer-bundle="" src="https://framerusercontent.com/sites/5Srf3Dbch4UEGrdXvNsvvG/_script0.QNOT6H27.mjs"></script>`
    *   Remove Framer-specific attributes from HTML elements (e.g., `data-framer-hydrate-v2`, `data-framer-ssr-released-at`, `data-framer-page-optimized-at`, `data-framer-component-type`, `data-framer-name`, `data-framer-page-link-current`, `data-framer-background-image-wrapper`, `data-framer-original-sizes`, `data-styles-preset`, `data-highlight`, `data-border`).
    *   Clean up Framer-generated CSS classes (e.g., `framer-F9XXV`, `framer-body-augiA20Il`, `framer-lux5qc`, `framer-72rtr7`, etc.) and inline styles. This will likely require a complete rewrite of the CSS.
    *   **Affected File:** [`website.tinygnomes.com/index.html`](website.tinygnomes.com/index.html) and potentially other HTML files if they contain similar Framer code.

*   **Localize External Resources:**
    *   **Favicon:** Download `https://framerusercontent.com/modules/kEhTYu6Pq8ZWd9mFhVZ7/fVXX3guvCSC1Ydl6IR68/assets/znbthOUlla2NmfdKVSgcE2SqRyg.png` and host it locally. Update the `<link rel="icon">` tag.
    *   **Fonts:** Download and self-host Google Fonts (Inter, Raleway, Fragment Mono) or link them from a reliable CDN.
    *   **Images:** Download all images from `https://framerusercontent.com/images/...` and host them locally. Update all `<img>` `src` and `srcset` attributes accordingly.
    *   **SVG Templates:** Extract the SVG definitions from the `<div id="svg-templates">` block and either inline them where used or save them as separate SVG files and reference them.
    *   **Affected File:** [`website.tinygnomes.com/index.html`](website.tinygnomes.com/index.html) and potentially other HTML files.

*   **Review and Develop Placeholder Pages:**
    *   The following pages are currently placeholders and need to be reviewed for content and functionality. Decide whether to remove them, populate them with relevant content, or redirect them.
        *   [`website.tinygnomes.com/about.html`](website.tinygnomes.com/about.html)
        *   [`website.tinygnomes.com/api.html`](website.tinygnomes.com/api.html)
        *   [`website.tinygnomes.com/contact.html`](website.tinygnomes.com/contact.html)
        *   [`website.tinygnomes.com/faq.html`](website.tinygnomes.com/faq.html)
        *   [`website.tinygnomes.com/integration.html`](website.tinygnomes.com/integration.html)
        *   [`website.tinygnomes.com/pricing.html`](website.tinygnomes.com/pricing.html)
        *   [`website.tinygnomes.com/security..html`](website.tinygnomes.com/security..html) (Note: Typo in filename, should be `security.html`)
        *   [`website.tinygnomes.com/terms.html`](website.tinygnomes.com/terms.html)
        *   [`website.tinygnomes.com/testimonials.html`](website.tinygnomes.com/testimonials.html)
        *   [`website.tinygnomes.com/white-label.html`](website.tinygnomes.com/white-label.html)
        *   `website.tinygnomes.com/features/` (all HTML files within this directory)
        *   `website.tinygnomes.com/new-misc/` (all HTML files within this directory)

*   **Review `robots.txt`:**
    *   Ensure the [`website.tinygnomes.com/robots.txt`](website.tinygnomes.com/robots.txt) file is appropriate for the new hosting environment and SEO strategy.

## General Improvements

*   **Code Structure and Readability:** Refactor the HTML and CSS to be more semantic, maintainable, and easier to understand without Framer's generated code.
*   **Responsiveness:** Verify that the website remains fully responsive across different devices after removing Framer's styling.
*   **Performance Optimization:**
    *   Optimize images (compression, appropriate formats).
    *   Minify CSS and JavaScript.
    *   Consider lazy loading for images and other assets.
*   **Accessibility (A11y):** Review the website for accessibility best practices (e.g., proper ARIA attributes, keyboard navigation, color contrast).
*   **SEO:** Ensure meta tags, titles, and content are optimized for search engines.