- [Table of Contents](README.md)
- [Previous Chapter](FAQ.md)

# Calendar Page

This document defines the structure and logic for the **Calendar Page** (`website/features/calendar.html`).

## Overview

The calendar page is a feature showcase page detailing the capabilities of the Tiny Gnomes calendar tool.

## Visual Implementation

The visual structure is derived directly from the Figma export (`Figma/2026, 14_47_32 CET.svg`). We use semantic HTML and custom CSS to recreate this design perfectly, without relying on Tailwind CSS or Locofy exports.

## Structure

The page uses standard HTML5 boilerplate, sharing the exact same header and footer as the main `index.html` page.

The main body (`<main>`) includes the following sections:
1. **Feature Header**: A centered title "Calendar" with a yellow underline.
2. **Hero Section**: A section with a light blue organic background shape, a headline ("View the big picture / Or, laser focus on just one project."), a decorative element showing a calendar icon, and a sticky screenshot of the calendar app UI.
3. **Introduction**: A short text block starting with "The most powerful Calendar you've ever used."
4. **Feature List (Unordered)**: A bulleted list of 5 key points (Share your schedule, Never forget an event again, Invite others, Access from cell phone, Sync).
5. **Additional Features List (Ordered)**: A block with a title "Great features you won't want to live without", followed by a green-outlined box containing a numbered list of 8 features (Map, Memos, Tasks, Compliance, Feeds, Avoid it, Auto-links, SMS).

## Logic

Unlike the home page, the Calendar feature page contains **no animations**. The content should be fully visible on render.
No JavaScript is required for this page's core functionality (the mobile menu logic from `animations.js` can still apply to the shared header).

- [Next Chapter](Compliance.md)
