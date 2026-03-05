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

### Trusted by logos
The logos in the trusted by section should scroll horizontally, and fade out at the edges. The scroll should be continuous and smooth, and the logos should be duplicated to create the illusion of an infinite scroll. The fade should be linear, with the logos at the edges being fully transparent and the logos in the center being fully opaque. The visible area needs to adapt to the screen size to achieve a responsive design.
The first row of logos should scroll towards the left, the second towards the right, and the third again towards the left.

### Testimonial Carousel Dots

On mobile viewports only one testimonial card is visible at a time. To let users know there are more cards and navigate between them, we use **CSS scroll-snap** combined with **dot indicators** (à la apple.com).

#### CSS

*   `.testimonials-scroll` gets `scroll-snap-type: x mandatory` so the scroll position snaps to each card.
*   `.testimonial-card` gets `scroll-snap-align: center`.
*   On mobile the card width becomes `100%` (instead of the fixed `420px` used on desktop).

#### Dot Indicators

A `<div class="testimonials-dots">` is placed after `.testimonials-scroll` in the HTML, containing one `<button>` per card.

```pseudo-code
// On DOMContentLoaded
[cards]  = all .testimonial-card elements
[dots]   = all .testimonials-dots button elements
[scroll] = .testimonials-scroll container

// Find which card's center is closest to the container's center
function getActiveDotIndex():
  [containerCenter] = horizontal midpoint of [scroll]
  for each [card] at [index] in [cards]:
    [cardCenter] = horizontal midpoint of [card]
    track the [index] with smallest |cardCenter - containerCenter|
  return closest index

function updateDots():
  set active class on dot at getActiveDotIndex(), remove from all others

listen to scroll event on [scroll] -> updateDots()
call updateDots() on load

// Clicking a dot scrolls that card to the center of the container
for each [dot] at [index] in [dots]:
  on click: calculate scrollLeft offset to center [cards][index], then scrollTo({ left, behavior: 'smooth' })
```

#### Visibility

The dots are always visible, since the cards can overflow at many viewport sizes — not just mobile.

### Interactions
*   Hover effects are handled by CSS (`global.css` has hover states).
*   Mobile menu: TODO
*   Active nav link: The page parses the URL hash (e.g., `#features`) on load and on `hashchange` to highlight the corresponding navigation link in the header. For the root path or empty hash, it defaults to the "Home" link.