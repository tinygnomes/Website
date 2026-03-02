# Home Page

This document defines the structure and logic for the **Home Page** (`website/index.html`).

## Overview

The home page is the main landing page for the marketing website. It includes:
*   Header with navigation.
*   Hero section with "Accountable" slogan and illustration.
*   Features grid.
*   Testimonials.
*   Footer.

> Note: Header and footer are shared with all the other pages.

## Visual Implementation

The visual structure is derived from the Locofy export.
We generally trust the structure below but may inject dynamic logic (like the mobile menu or scroll animations) into it.

## Structure

The page uses a standard HTML5 boilerplate. It includes meta tags for social media sharing. They include:
- Description: "Tiny Gnomes is a secure cloud-based suite of tools for project management. Finally, get your team on the same page."
- Icon: `assets/favicon.png`
- Open Graph / Facebook:
    - Title: "Tiny Gnomes"
    - Type: "website"
    - Description: "Tiny Gnomes is a secure cloud-based suite of tools for project management. Finally, get your team on the same page."
    - Image: `assets/social-share.png`
- Twitter:
    - Card: "summary_large_image"
    - Title: "Tiny Gnomes"
    - Description: "Tiny Gnomes is a secure cloud-based suite of tools for project management. Finally, get your team on the same page."
    - Image: `assets/social-share.png`

Additionally, we include the canonical URL: `https://website.tinygnomes.com/`

And, obviously, all the links to the CSS and JS files, as well as the Google Fonts we use.

The body is divided into the following sections:

- Header with logo, navigation links, and login link
- Hero section
- Features section
- Trusted by section
- Testimonials section
- Misc section with cards for use cases, faq, API, security
- Schedule demo section
- Footer (with cookie policy dialog)

## Logic

### Scroll Animations

Each section of the page (Features, Trusted By, Testimonials, Misc, Schedule Demo) should animate into view as the user scrolls down.

```pseudo-code
// CSS
.animated-section {
  opacity: 0
  transform: scale(0.7)
  transition: all 0.6s ease-out
}

.animated-section.is-visible {
  opacity: 1
  transform: scale(1)
}

// Logic
initialize IntersectionObserver with callback:
  for each [entry] in [entries]:
    if [entry] is intersecting:
      add class "is-visible" to [entry.target]
      stop observing [entry.target] // Run animation only once

for each [section] in [animatedSections]:
  start observing [section]
```

### Hero Animation
The hero illustration has a 3D hover effect:
*   Initial state: `perspective(1200px)`
*   Hover state: `perspective(1200px) rotateY(-4deg)`
*   Transition: ~0.5s ease

### Hero Image Interactions
Individual images in the hero section zoom on hover:
*   **Global**: Scale 1.3x
*   **Gnome** & **Trees**: Scale 1.6x
*   **Slogans** ("Stay on path", "Get sh*t done", "Focus"): No zoom


### Interactions
*   Hover effects are handled by CSS (`global.css` has hover states).
*   Mobile menu: TODO
*   Active nav link: The page parses the URL hash (e.g., `#features`) on load and on `hashchange` to highlight the corresponding navigation link in the header. For the root path or empty hash, it defaults to the "Home" link.