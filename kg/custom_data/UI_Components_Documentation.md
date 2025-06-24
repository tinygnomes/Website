# Custom Data: UI Components Documentation

### Features Section

*   [2025-06-24 09:15:36]

```json
{
  "description": "The features section showcases the core functionalities of Tiny Gnomes, presented as a grid of interactive cards.",
  "structure": [
    {
      "item": "Title",
      "details": "`h1` with \"What are our features?\"."
    },
    {
      "item": "Features Grid",
      "details": "`div` with `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8` for responsive layout."
    },
    {
      "item": "Feature Card",
      "details": "Each feature is an `a` tag with class `feature-card`, linking to a detailed feature page. Image: `img` tag with `src` pointing to the feature icon (e.g., `assets/calendar-icon.png`). Text Content: Feature title: `h5` (e.g., \"Calendar\"). Feature description: `p` (e.g., \"Keep track of events, memos and tasks.\"). \"more\u2026\" link: `p` with `text-light-blue text-xl`."
    }
  ],
  "styling": [
    {
      "item": "Title",
      "details": "`text-6xl font-bold text-dark-blue font-raleway`"
    },
    {
      "item": "Feature Cards",
      "details": "`flex flex-col items-center p-4 rounded-lg`"
    },
    {
      "item": "Feature Images",
      "details": "`zoom-image` class for hover effects, with fixed `width: 120px; height: 120px;`."
    },
    {
      "item": "Feature Titles",
      "details": "`text-2xl font-bold font-raleway`"
    },
    {
      "item": "Feature Descriptions",
      "details": "`text-xl mt-2`"
    },
    {
      "item": "more\u2026 Link",
      "details": "`text-light-blue text-xl`"
    },
    {
      "item": "Transitions",
      "details": "The `#features` section itself has `transition: transform 0.1s linear, opacity 0.1s linear;` for a scroll-based zoom and fade effect."
    }
  ],
  "functionality": [
    "The entire features section scales and fades in as the user scrolls down the page, controlled by JavaScript in the `script` tag at the end of `index.html`.",
    "Each feature card is a clickable link, navigating to a more detailed page for that specific feature (e.g., `features/calendar`).",
    "Feature images have a zoom effect on hover, drawing attention to the individual features."
  ]
}
```

---
### Header

*   [2025-06-24 09:15:27]

```json
{
  "description": "The header component is a sticky navigation bar located at the top of the page.",
  "structure": [
    {
      "item": "Logo",
      "details": "`img` tag with `src=\"assets/tg.svg\"` and `alt=\"TinyGnomes Logo\"`."
    },
    {
      "item": "Desktop Navigation Menu",
      "details": "(Hidden on mobile) Contains links for \"Home\", \"Features\", \"Pricing\", \"Testimonials\", and \"FAQ\". Each link is an `a` tag with specific styling."
    },
    {
      "item": "Authentication Links",
      "details": "(Hidden on mobile) \"Sign up\" and \"Login\" links. \"Login\" has a distinct button style."
    },
    {
      "item": "Mobile Menu Button",
      "details": "(Hidden on desktop) A button with an SVG icon to toggle the mobile navigation menu."
    }
  ],
  "styling": [
    {
      "item": "Sticky Position",
      "details": "`sticky top-0`"
    },
    {
      "item": "Background",
      "details": "`bg-white`"
    },
    {
      "item": "Z-index",
      "details": "`z-50` to ensure it stays above other content."
    },
    {
      "item": "Height",
      "details": "`h-[114px]`"
    },
    {
      "item": "Shadow",
      "details": "`shadow-md`"
    },
    {
      "item": "Navigation Links",
      "details": "Default text color: `text-light-blue`. Hover effects: `hover:text-opacity-90 hover:underline`. \"Home\" link has `bg-brand-orange text-white px-6 py-2 rounded-full font-bold`. \"Login\" link has `bg-brand-green text-white px-6 py-2 rounded-full font-bold`."
    },
    {
      "item": "Transitions",
      "details": "`zoom-button` class for hover effects on buttons."
    }
  ],
  "functionality": [
    "The header remains visible at the top of the viewport when scrolling.",
    "Navigation links allow users to jump to different sections of the website or external pages.",
    "The mobile menu button (SVG icon) is intended to reveal a navigation menu on smaller screens (functionality not fully implemented in provided HTML)."
  ]
}
```

---
### Hero Section

*   [2025-06-24 09:15:32]

```json
{
  "description": "The hero section is the main introductory content area of the landing page, featuring a prominent heading, a call-to-action, and an illustrative graphic.",
  "structure": [
    {
      "item": "Layout",
      "details": "Divided into two main columns for larger screens (`md:flex-row`)."
    },
    {
      "item": "Left Column (Text Content)",
      "details": "Main heading: `h1` with \"For those that must be 100% Accountable\". Sub-heading: `h2` with \"Accountable\". SVG graphic below the headings. Call-to-action button: \"Free sign up\"."
    },
    {
      "item": "Right Column (Illustration)",
      "details": "Contains a background illustration image (`IllustrationBG.png`). Multiple overlay images representing various concepts (e.g., Focus, ValleyOfDroppedBoxes, RiverOfRevisions) positioned absolutely. Small \"Gnome\" and \"Tree\" images with zoom effects."
    }
  ],
  "styling": [
    {
      "item": "Container",
      "details": "`container mx-auto px-6 flex flex-col md:flex-row items-center justify-between`"
    },
    {
      "item": "Width/Padding",
      "details": "`width: 1440px; padding: 50px 60px`"
    },
    {
      "item": "Headings",
      "details": "`h1`: `text-5xl md:text-6xl font-bold text-dark-blue leading-tight font-raleway`. `span` within `h1`: `text-7xl md:text-9xl`. `h2`: `text-5xl md:text-6xl font-raleway font-bold text-brand-green leading-tight mt-4`."
    },
    {
      "item": "Call-to-action Button",
      "details": "`bg-brand-orange text-white px-10 py-4 rounded-full text-2xl font-bold hover:text-light-blue hover:opacity-75 zoom-button`"
    },
    {
      "item": "Illustration Container",
      "details": "`relative hero-illustration` with `width: 888px; height: 587px;`"
    },
    {
      "item": "Overlay Images",
      "details": "`absolute zoom-image` with inline styles for `top`, `left`, `height`, `width` for precise positioning."
    },
    {
      "item": "Gnome/Tree Images",
      "details": "`absolute zoom-gnome` with inline positioning styles."
    },
    {
      "item": "Transitions",
      "details": "`.zoom-button`, `.zoom-image`, `.zoom-gnome`: `transition: transform 0.3s ease-in-out;`. `.hero-illustration`: `transition: transform 0.5s ease-in-out;`. Hover effects for scaling images and buttons, and a 3D rotation for the hero illustration."
    }
  ],
  "functionality": [
    "The \"Free sign up\" button is a call-to-action for users to register.",
    "The various images in the illustration are designed to be interactive, zooming in on hover to draw attention to different features or concepts of the Tiny Gnomes platform.",
    "The entire hero illustration has a subtle 3D rotation effect on hover, adding a dynamic visual element."
  ]
}
```
