# ADR 002: Adopt Two-Column Layout for Hero Section

## Status
Accepted

## Context
The design mockups for the hero section clearly depict a separation of content: main call-to-action and heading on the left, and a detailed illustration on the right. A decision is needed on the most appropriate layout strategy.

## Decision
We have decided to implement a two-column layout for the hero section using Flexbox or CSS Grid.

## Consequences
*   **Pros**:
    *   Directly aligns with the visual design, ensuring accurate implementation.
    *   Provides clear structural separation for content elements.
    *   Easily adaptable for responsiveness across different screen sizes.
    *   Utilizes standard CSS layout techniques, making it maintainable.
*   **Cons**:
    *   Requires careful consideration of responsive breakpoints to ensure optimal display on smaller devices.
    *   May require specific ordering of HTML elements to achieve desired visual flow, especially for accessibility.