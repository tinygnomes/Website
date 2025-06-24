# Custom Data: Tailwind CSS Guide

### Usage Patterns

*   [2025-06-24 09:11:24]

```json
{
  "title": "Tailwind CSS Usage Guide",
  "sections": [
    {
      "heading": "Configuration",
      "content": "The Tailwind CSS configuration is located in `tailwind.config.js`.",
      "subsections": [
        {
          "heading": "Content Paths",
          "content": "Tailwind CSS is configured to scan the following files for utility classes:\n- `website/**/*.html`\n- `website/**/*.js`"
        },
        {
          "heading": "Custom Fonts",
          "content": "The following custom font families are extended in the Tailwind CSS theme:\n- `font-inter`: 'Inter', sans-serif\n- `font-raleway`: 'Raleway', sans-serif\n- `font-fragment-mono`: 'Fragment Mono', monospace\n- `font-rancho`: 'Rancho', cursive\n\n**Example Usage:**\n```html\n<body class=\"font-raleway\">\n    <h1 class=\"font-rancho\">Welcome</h1>\n</body>\n```"
        },
        {
          "heading": "Custom Colors",
          "content": "The following custom colors are defined in the Tailwind CSS theme:\n- `light-blue`: `#3a9afe`\n- `dark-blue`: `rgb(0, 136, 187)`\n- `brand-green`: `rgb(136, 187, 0)`\n- `brand-orange`: `rgb(255, 187, 0)`\n\n**Example Usage:**\n```html\n<div class=\"bg-brand-green text-white\">\n    This div has a custom green background and white text.\n</div>\n<p class=\"text-dark-blue\">This text uses the custom dark blue color.</p>\n```"
        }
      ]
    },
    {
      "heading": "Common Utility Class Patterns",
      "content": "Below are examples of commonly used Tailwind CSS utility classes found in the project.",
      "subsections": [
        {
          "heading": "Layout and Flexbox",
          "content": "- `container`: Sets a `max-width` to match the `min-width` of the current breakpoint.\n- `mx-auto`: Centers a block-level element horizontally.\n- `px-6`, `py-4`: Sets horizontal and vertical padding.\n- `h-full`: Sets the height to 100% of the parent.\n- `flex`: Applies `display: flex`.\n- `justify-between`: Distributes items evenly with space between them.\n- `items-center`: Aligns items along the cross axis (vertically in a row, horizontally in a column).\n- `space-x-2`: Adds horizontal space between child elements.\n- `hidden`, `md:flex`: Hides an element by default and displays it as flex on medium screens and up.\n- `md:w-1/2`: Sets width to 50% on medium screens and up.\n- `grid`, `grid-cols-1`, `md:grid-cols-2`, `lg:grid-cols-3`: Creates a grid layout with responsive column counts.\n- `gap-8`: Sets the gap between grid items.\n- `flex-col`, `md:flex-row`: Sets flex direction to column by default and row on medium screens and up.\n- `flex-shrink-0`: Prevents an item from shrinking.\n- `flex-1`: Allows an item to grow and shrink as needed.\n- `ml-6`: Sets left margin.\n- `w-full`: Sets width to 100%.\n- `text-right`: Aligns text to the right.\n\n**Example:**\n```html\n<nav class=\"container mx-auto px-6 h-full flex justify-between items-center\">\n    <div class=\"hidden md:flex items-center space-x-2\">...</div>\n</nav>\n<div class=\"features-grid grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8\">...</div>\n```"
        },
        {
          "heading": "Sizing",
          "content": "- `h-[value]`, `w-[value]`: Sets explicit height and width using arbitrary values (e.g., `h-[114px]`).\n- `height: [value]`, `width: [value]`: Inline styles for specific dimensions (e.g., `style=\"width: 1440px; height: 587px;\"`).\n- `height: [percentage]`, `width: [percentage]`: Inline styles for percentage-based dimensions (e.g., `style=\"height: 11%; width: 11%;\"`).\n\n**Example:**\n```html\n<header class=\"h-[114px]\">...</header>\n<img src=\"assets/calendar-icon.png\" style=\"width: 120px; height: 120px;\">\n```"
        },
        {
          "heading": "Spacing",
          "content": "- `px-[value]`, `py-[value]`: Horizontal and vertical padding (e.g., `px-6`, `py-4`).\n- `mt-[value]`, `mb-[value]`, `ml-[value]`, `mr-[value]`: Top, bottom, left, and right margins (e.g., `mt-4`, `mb-12`, `ml-6`).\n- `p-[value]`: All-around padding (e.g., `p-4`).\n\n**Example:**\n```html\n<a href=\"#\" class=\"px-6 py-2 mt-12\">Sign Up</a>\n<div class=\"text-center mb-12\">...</div>\n```"
        },
        {
          "heading": "Typography",
          "content": "- `font-raleway`, `font-inter`, etc.: Applies custom font families.\n- `text-5xl`, `md:text-6xl`: Sets font size, with responsive variations.\n- `font-bold`: Applies bold font weight.\n- `leading-tight`: Sets line height.\n- `text-7xl`, `md:text-9xl`: Larger font sizes, with responsive variations.\n- `text-2xl`, `text-xl`: Other common font sizes.\n\n**Example:**\n```html\n<body class=\"font-raleway\">\n    <h1 class=\"text-5xl md:text-6xl font-bold text-dark-blue leading-tight font-raleway\">...</h1>\n    <p class=\"text-xl mt-2\">...</p>\n</body>\n```"
        },
        {
          "heading": "Colors",
          "content": "- `bg-white`: Sets background color to white.\n- `text-dark-blue`, `text-brand-green`, `text-light-blue`, `text-white`, `text-gray-600`: Sets text color using custom and default Tailwind colors.\n- `bg-brand-orange`: Sets background color to a custom brand orange.\n- `hover:text-light-blue`, `hover:text-opacity-90`: Changes text color or opacity on hover.\n\n**Example:**\n```html\n<header class=\"bg-white\">...</header>\n<a href=\"#\" class=\"bg-brand-orange text-white hover:text-light-blue\">...</a>\n```"
        },
        {
          "heading": "Borders and Shadows",
          "content": "- `shadow-md`: Applies a medium shadow.\n- `border-3`, `border-brand-green`: Sets border width and color.\n- `rounded-full`, `rounded-lg`: Applies border-radius for full circles or large rounded corners.\n\n**Example:**\n```html\n<header class=\"shadow-md\">...</header>\n<div class=\"border-3 border-brand-green rounded-full\">...</div>\n<a class=\"feature-card rounded-lg\">...</a>\n```"
        },
        {
          "heading": "Interactivity and Transitions",
          "content": "- `hover:opacity-75`, `hover:underline`: Changes opacity or adds underline on hover.\n- `focus:outline-none`: Removes outline on focus.\n- `zoom-button`, `zoom-image`, `zoom-gnome`, `hero-illustration`: Custom CSS classes defined in the `<style>` block for hover effects and transitions. These classes utilize Tailwind's utility-first approach by applying `transition` properties and then custom `transform` and `z-index` values on hover.\n\n**Example:**\n```html\n<a href=\"#\" class=\"hover:opacity-75 hover:text-light-blue zoom-button\">Free sign up</a>\n<img src=\"assets/Focus.png\" class=\"zoom-image\">\n```"
        },
        {
          "heading": "Positioning",
          "content": "- `sticky`, `top-0`, `z-50`: Creates a sticky element positioned at the top with a high z-index.\n- `absolute`, `inset-0`: Positions an element absolutely, covering its parent.\n\n**Example:**\n```html\n<header class=\"sticky top-0 bg-white z-50\">...</header>\n<img src=\"assets/IllustrationBG.png\" class=\"absolute inset-0\">\n```"
        }
      ]
    }
  ]
}
```
