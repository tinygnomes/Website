- [Table of Contents](README.md)
- [Previous Chapter](Chat.md)

# More Page

This document defines the structure and logic for the **More Page** (`website/features/more.html`).

## Overview

The more page is a feature showcase page detailing the capabilities of the Tiny Gnomes more tool.

## Visual Implementation

The visual structure is derived from the Calendar page layout. We use semantic HTML and custom CSS to recreate this design perfectly.

## Structure

The page uses standard HTML5 boilerplate, sharing the exact same header and footer as the main `index.html` page.

The main body (`<main>`) includes the following sections:
1. **Feature Header**: A centered title "More" with a yellow underline.
2. **Hero Section**: A section with a light blue organic background shape, a headline ("Search, Private conversation, Scratch pad, and many more."), a decorative element showing a more icon (`more-icon.png`), and a sticky screenshot of the more app UI (`generic-screenshot.png`).
3. **Introduction**: A short text block describing the More feature.
4. **Feature List (Unordered)**: A bulleted list of key points for More.
5. **Additional Features List (Ordered)**: A block with a title "Great features you won't want to live without", followed by a green-outlined box containing a numbered list of features.

## Logic

Unlike the home page, this feature page contains **no entrance animations**. However, the more icon and screenshot feature a hover zoom effect. The content should be fully visible on render.
No JavaScript is required for this page's core functionality (the mobile menu logic from `animations.js` can still apply to the shared header).

- [Next Chapter](UseCases.md)
