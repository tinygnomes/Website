# Custom Data: Interactive Animations

### Mouse-over Animations

*   [2025-06-24 09:06:07]

```json
{
  "description": "This section documents the CSS and JavaScript used for interactive mouse-over animations on various elements within the website.",
  "css_properties": {
    "zoom-button": "Applies a scale transform (1.1x) on hover for buttons.",
    "zoom-image": "Applies a scale transform (1.2x) and increases z-index on hover for images.",
    "zoom-gnome": "Applies a scale transform (1.5x) and increases z-index on hover for gnome illustrations.",
    "hero-illustration": "Applies a 3D perspective transform (rotateY(-5deg)) on hover for the main hero illustration.",
    "#features": "Applies a linear transition for transform and opacity, used for the scroll-based animation."
  },
  "javascript_details": {
    "function_name": "handleScroll",
    "event_listener": "window.addEventListener('scroll', handleScroll)",
    "description": "The `handleScroll` function calculates the visibility of the `#features` section based on scroll position. It then applies a dynamic `scale` and `opacity` to create a zoom-in and fade-in effect as the section becomes visible in the viewport. The scale ranges from 0.7 to 1, and opacity from 0 to 1.",
    "relevant_lines": "Lines 243-265 in website/index.html"
  }
}
```
