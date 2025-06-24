# Pattern: Component-Based Structure in HTML

## Context

To keep the project's HTML organized and maintainable, we need a consistent structure that is easy to understand and build upon. Even without a formal frontend framework, we can still benefit from a component-based approach.

## Decision

We structure our HTML in a component-like manner. Each distinct section of the user interface is contained within its own `<section>` or other appropriate semantic HTML element. These sections are self-contained and represent a specific part of the page, such as the header, the hero section, or the features grid.

## Rationale

*   **Readability:** Organizing the page into logical sections makes the code easier to read and understand.
*   **Maintainability:** When a change is needed, it's easier to locate the relevant section of HTML. This modularity also makes it easier to add, remove, or reorder sections of the page.
*   **Reusability:** While not as straightforward as with a JS framework, self-contained HTML sections can be more easily copied and adapted for use elsewhere if needed.

## Implementation Example

In [`website/index.html`](../../website/index.html), the page is divided into several key sections:

```html
<body>
    <header class="sticky top-0 ...">
        <!-- Header content -->
    </header>

    <main>
        <section class="hero ...">
            <!-- Hero section content -->
        </section>

        <section id="features" class="features-section ...">
            <!-- Features section content -->
        </section>

        <section id="trusted-by" class="... ">
            <!-- "Trusted By" section content -->
        </section>
    </main>
</body>
```

Each `<section>` has a clear purpose and contains all the HTML and Tailwind CSS classes related to that specific UI component.

## Consequences

*   This pattern encourages developers to think about the UI in terms of modular components, even in a static HTML environment.
*   It helps to prevent a monolithic, hard-to-manage `index.html` file as the project grows.