- [Table of Contents](README.md)
- [Previous Chapter](Tasks.md)

# Wikis Page

This document defines the structure and logic for the **Wikis Page** (`website/features/wikis.html`).

## Overview

The wikis page is a feature showcase page detailing the capabilities of the Tiny Gnomes wikis tool.

## Visual Implementation

The visual structure is derived from the Calendar page layout. We use semantic HTML and custom CSS to recreate this design perfectly.

## Structure

The page uses standard HTML5 boilerplate, sharing the exact same header and footer as the main `index.html` page.

The main body (`<main>`) includes the following sections:
1. **Feature Header**: A centered title "Wikis" with a yellow underline.
2. **Hero Section**: A section with a light blue organic background shape, a headline ("Capture knowledge and share it with your team"), a decorative element showing a wikis icon (`wikis-icon.png`), and a sticky screenshot of the wikis app UI (`wikis-screenshot.png`).
3. **Introduction**: Write and publish articles, capture knowledge, find everything easily later.
4. **Feature List (Unordered)**:
    - **Create and edit** - A wiki is like a web-page you can edit as often as you like.
    - **Insert images** - Upload images from your computer, or grab URLs from other places on the web (*these may change on you).
    - **Insert links** - Convert any word or sentence into a link, even link to another wiki.
5. **Additional Features List (Ordered)**: A block with a title "Great features you won't want to live without", followed by a green-outlined box containing a numbered list of features:
    - **Share** - Share you wiki with people outside of Tiny Gnomes.
    - **Archive** - See who made changes.
    - **Compare** - See what people added or removed.

## Logic

Unlike the home page, this feature page contains **no entrance animations**. However, the wikis icon and screenshot feature a hover zoom effect. The content should be fully visible on render.
No JavaScript is required for this page's core functionality (the mobile menu logic from `animations.js` can still apply to the shared header).

- [Next Chapter](Reports.md)
