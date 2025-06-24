# Pattern: Utility-First CSS with Tailwind CSS

## Context

The project requires a consistent and efficient way to apply styling across the website. The goal is to enable rapid development, ensure visual consistency, and make the styling easy to maintain and update.

## Decision

We use **Tailwind CSS**, a utility-first CSS framework, as the primary method for styling all components and pages. Instead of writing custom CSS classes for every element, we apply pre-existing utility classes directly in the HTML.

This approach is configured in [`tailwind.config.js`](../../tailwind.config.js), which defines the project's color palette, fonts, and other design tokens. The core styles and Tailwind utilities are imported in [`website/src/input.css`](../../website/src/input.css).

## Rationale

*   **Speed:** Building complex responsive layouts without leaving your HTML is significantly faster.
*   **Consistency:** Using a predefined set of utilities ensures that spacing, colors, and typography are consistent throughout the application.
*   **Maintainability:** Because styles are co-located with the HTML, it's easier to understand and modify the styling of a component without searching through separate CSS files.

## Implementation Example

Here is an example from the navigation bar in [`website/index.html`](../../website/index.html:33):

```html
<div class="hidden md:flex items-center space-x-2 border-3 border-brand-green rounded-full px-6 py-4 text-[28px]">
    <a href="#" class="bg-brand-orange text-white px-6 py-2 rounded-full hover:opacity-75 hover:text-light-blue font-bold">Home</a>
    <a href="#features" class="text-light-blue hover:text-opacity-90 hover:underline px-2">Features</a>
    ...
</div>
```

In this snippet:
*   `hidden md:flex` creates a responsive container that is hidden on small screens and a flex container on medium screens and up.
*   `items-center`, `space-x-2`, `px-6`, `py-4` control the layout and spacing.
*   `border-3`, `border-brand-green`, `rounded-full` define the border and shape.
*   `bg-brand-orange`, `text-white`, `font-bold` apply colors and font weight.
*   `hover:opacity-75` is a state variant that changes the opacity on hover.

## Consequences

*   Developers need a basic understanding of Tailwind CSS classes.
*   The initial HTML markup can look more verbose. However, this is offset by the reduced need for custom CSS.
*   For highly specific or complex styles not covered by utilities, custom CSS classes can be added in [`website/src/input.css`](../../website/src/input.css).