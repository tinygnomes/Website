- [Table of Contents](README.md)
- [Previous Chapter](ALP.md)

# Agent Instructions (GEMINI.md)

You are an intelligent agent helping to maintain the TinyGnomes website.

## Core Directives

1.  **Source of Truth**: The Markdown files in this directory are the specification. The code in `website/` is a generated artifact.
2.  **No Node.js**: This is a static site. Do not introduce npm build steps or bundlers.
3.  **Visual Implementation**:
    *   Use the **Figma MCP Server** tools to interrogate the Figma file as your visual source of truth.
    *   Write **clean, semantic HTML** and **structured CSS**. Avoid `div` nesting where semantic tags like `<nav>` or `<article>` apply.
    *   Extract design tokens (colors, fonts, layout specs) directly from the Figma API via the MCP server and place them in `website/css/style.css`.
    *   Export SVGs precisely using the MCP server.

## Pseudo-code Standards

*   `[conceptual brackets]`: High-level intent for HTML.
*   `<conceptual brackets>`: High-level intent for JS/CSS.
*   `Literal Code`: Specific implementation details (loops, conditionals).

## Workflows

### 1. Standard Update (Content & Logic)
1.  **Identify**: Find the Markdown chapter controlling the feature.
2.  **Specify**: Update the Markdown to describe the change or logic.
3.  **Implement**: Update `website/` code to match the new specification.

### 2. Design Update (Visuals)
1.  **Analyze**: Run `list_figma_hierarchy` to find the relevant frames or components updated in Figma.
2.  **Extract Tokens/Metrics**: Use `get_figma_styles` or `get_node_details` to accurately pull new values, spacing, or CSS references and update `website/css/style.css`.
3.  **Assets**: Use `export_figma_asset` if new vector or raster graphics were added.
4.  **Rebuild**: Update HTML/CSS in `website/` to match the visual reference using semantic tags.

- [Next Chapter](Home.md)