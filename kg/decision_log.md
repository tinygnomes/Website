# Decision Log

---
## Decision
*   [2025-06-24 08:59:24] Updated assets_directory_contents in product context to include all current assets.

## Rationale
*   The previous list of assets was incomplete. This update ensures the knowledge graph accurately reflects all image and icon files present in the 'website/assets/' directory, providing a more comprehensive overview of project resources.

---
## Decision
*   [2025-06-24 08:59:16] Removed outdated PLAN.md, TAILWIND_PLAN.md, and TODO.md from product context.

## Rationale
*   These files no longer exist in the project directory and were causing discrepancies in the knowledge graph. Removing them ensures the product context accurately reflects the current project state.

---
## Decision
*   [2025-06-22 13:23:15] Adopt a two-column layout for the hero section

## Rationale
*   The design clearly separates the main call-to-action and heading on the left from the detailed illustration on the right. A two-column layout (using Flexbox or CSS Grid) is the most direct and maintainable way to implement this structure.

## Implementation Details
*   The main page body will contain a primary container. Inside this container, two divs will be created, one for the left-side content (headings, button) and one for the right-side illustration. The right-side will likely use relative positioning for its container and absolute positioning for its internal elements to match the design precisely.

---
## Decision
*   [2025-06-22 12:20:22] Decision to use Tailwind CSS for styling.

## Rationale
*   To simplify styling and accelerate development.

---
## Decision
*   [2025-06-22 12:20:12] Decision to use Tailwind CSS for styling.

## Rationale
*   To simplify styling and accelerate development.
