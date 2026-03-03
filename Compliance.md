- [Table of Contents](README.md)
- [Previous Chapter](FAQ.md)

# Compliance Page

This document defines the structure and logic for the **Compliance Page** (`website/features/compliance.html`).

## Overview

The compliance page is a feature showcase page detailing the capabilities of the Tiny Gnomes compliance tool.

## Visual Implementation

The visual structure is derived from the Calendar page layout. We use semantic HTML and custom CSS to recreate this design perfectly.

## Structure

The page uses standard HTML5 boilerplate, sharing the exact same header and footer as the main `index.html` page.

The main body (`<main>`) includes the following sections:
1. **Feature Header**: A centered title "Compliance" with a yellow underline.
2. **Hero Section**: A section with a light blue organic background shape, a headline ("Ask your team important questions"), a decorative element showing a compliance icon (`compliance-icon.png`), and a sticky screenshot of the compliance app UI (`generic-screenshot.png` since we don't have one yet).
3. **Introduction**: (empty)
4. **Feature List (Unordered)**: 
    - Asking the right questions of your team, on a regular schedule, can help you stay on course, and prevent failure.
    - **View Compliances on the calendar** - Turn Compliance option on for your calendar, and they will appear automatically, giving you time to complete them.
    - **Review a report** - View your own answers, as well as your teams.
5. **Additional Features List (Ordered)**: A block with a title "Examples", followed by a green-outlined box containing a numbered list of features:
    - Will we be on time, and on budget?
    - Is everyone Happy?
    - Do we have the resources we need to get our job done?

## Logic

Unlike the home page, this feature page contains **no entrance animations**. However, the compliance icon and screenshot feature a hover zoom effect. The content should be fully visible on render.
No JavaScript is required for this page's core functionality (the mobile menu logic from `animations.js` can still apply to the shared header).

- [Next Chapter](Tasks.md)
