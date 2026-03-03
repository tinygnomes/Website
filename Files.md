- [Table of Contents](README.md)
- [Previous Chapter](Reports.md)

# Files Page

This document defines the structure and logic for the **Files Page** (`website/features/files.html`).

## Overview

The files page is a feature showcase page detailing the capabilities of the Tiny Gnomes files tool.

## Visual Implementation

The visual structure is derived from the Calendar page layout. We use semantic HTML and custom CSS to recreate this design perfectly.

## Structure

The page uses standard HTML5 boilerplate, sharing the exact same header and footer as the main `index.html` page.

The main body (`<main>`) includes the following sections:
1. **Feature Header**: A centered title "Files" with a yellow underline.
2. **Hero Section**: A section with a light blue organic background shape, a headline ("The file system ensures you never lose anything."), a decorative element showing a files icon (`files-icon.png`), and a sticky screenshot of the files app UI (`files-screenshot.png`).
3. **Introduction**: Share and track files and folders.  control who sees what, and know who looked at what.
4. **Feature List (Unordered)**:
    - **Classic vs. Most recent** - The file system offers your classic view with folders and file names and dates, however, much more useful is to instantly view your files by the once most recently touched or uploaded.
    - **Filters** - Imagine being able to find files by "who" uploaded them. Or, to add a comment about the file or tag just the ones you plan to use during a presentation or trial, and filter for them instantly.
    - **View** - Files can be viewed in a list, or by thumbnails to better identify images.
    - **WebDAV** - You can mount Tiny Gnomes such that you can drag and drop files right on your desktop. Learn more.
    - **Zip** - Zipped files can be uploaded and treated as folders, and files and folders can easily be zipped up making downloading groups of files a snap.
    - **Syndication** - All files in Tiny Gnomes are private t the project they are in. However, if you are Lead in the project, you can syndicate a file or even an entire folder and give a link to people outside the system.
5. **Additional Features List (Ordered)**: A block with a title "Great features you won't want to live without", followed by a green-outlined box containing a numbered list of features:
    - **Lock** - Sometimes you just want to remember something, use Notes on the calendar to remind your whole team about something important.
    - **Archive** - Learn everything that ever happened to a file, who uploaded it, who updated it, who looked at.
    - **Check-sum** - Tiny Gnomes offers both MD5 and SHA1 checksums to ensure you know the legitimacy of a file.

## Logic

Unlike the home page, this feature page contains **no entrance animations**. However, the files icon and screenshot feature a hover zoom effect. The content should be fully visible on render.
No JavaScript is required for this page's core functionality (the mobile menu logic from `animations.js` can still apply to the shared header).

- [Next Chapter](Share.md)
