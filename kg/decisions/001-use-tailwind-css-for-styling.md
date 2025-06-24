# ADR 001: Use Tailwind CSS for Styling

## Status
Accepted

## Context
The project requires a modern, efficient, and maintainable approach to styling the static website. Traditional CSS or other frameworks were considered.

## Decision
We have decided to use Tailwind CSS for all styling within the TinyGnomes project.

## Consequences
*   **Pros**:
    *   Accelerated development due to utility-first approach.
    *   Consistent UI across the project with predefined design system constraints.
    *   Smaller CSS bundle size in production due to purging unused styles.
    *   Improved maintainability as styles are co-located with HTML.
*   **Cons**:
    *   Initial learning curve for developers unfamiliar with utility-first CSS.
    *   HTML can become verbose with many utility classes, though this is mitigated by componentization.
    *   Requires a build step (npm scripts) to compile and purge CSS.