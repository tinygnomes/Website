- [Table of Contents](README.md)
- [Previous Chapter](Files.md)

# Share Page

This document defines the structure and logic for the **Share Page** (`website/features/share.html`).

## Overview

The share page is a feature showcase page detailing the capabilities of the Tiny Gnomes share tool.

## Visual Implementation

The visual structure is derived from the Calendar page layout. We use semantic HTML and custom CSS to recreate this design perfectly.

## Structure

The page uses standard HTML5 boilerplate, sharing the exact same header and footer as the main `index.html` page.

The main body (`<main>`) includes the following sections:
1. **Feature Header**: A centered title "Share" with a yellow underline.
2. **Hero Section**: A section with a light blue organic background shape, a headline ("Sometimes we need to share"), a decorative element showing a share icon (`share-icon.png`), and a sticky screenshot of the share app UI (`share-screenshot.png`).
3. **Introduction**: Syndication simply means to share with the world, whether it's a file, a wiki, an event on a calendar, syndication allows you to share content as simple links.  A great example of syndication would be sharing wikis and files with multiple clients. Each client gets their own link with a password. You have the power to rescind a given link at your will.  You may also update the content that a syndicated link points to, and the next time the recipient clicks on the link they will see the new content. This makes it very easy to fix typos, or provide fresh lists of data.
4. **Feature List (Unordered)**:
    - **Syndicate files for downloads** - Share files Tiny Gomes securely as a clickable link.
    - **Syndicate wikis** - Wikis can be shared as a link or as an iframe embedded into a website.
    - **Password protection** - Further protect your content by password protecting your outgoing feeds.
    - **List view** - View all your syndication in one convenient list.
    - **Content tracking** - Track your syndication through the archive function to see who is accessing your content (including their IP addess).
    - **Multiple feeds** - Creates multiple links for one item.
    - **Stop sharing** - Syndicated items can be turned off so the generated link no longer allows outside access to your content.
5. **Additional Features List (Ordered)**: A block with a title "Great features you won't want to live without", followed by a green-outlined box containing a numbered list of features:
    1. **Syndicate files for downloads** - Share files Tiny Gomes securely as a clickable link.
    2. **Syndicate wikis** - Wikis can be shared as a link or as an iframe embedded into a website.
    3. **Password protection** - Further protect your content by password protecting your outgoing feeds.
    4. **List view** - View all your syndication in one convenient list.
    5. **Content tracking** - Track your syndication through the archive function to see who is accessing your content (including their IP addess).
    6. **Multiple feeds** - Creates multiple links for one item.
    7. **Stop sharing** - Syndicated items can be turned off so the generated link no longer allows outside access to your content.

## Logic

Unlike the home page, this feature page contains **no entrance animations**. However, the share icon and screenshot feature a hover zoom effect. The content should be fully visible on render.
No JavaScript is required for this page's core functionality (the mobile menu logic from `animations.js` can still apply to the shared header).

- [Next Chapter](Chat.md)
