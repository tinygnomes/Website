- [Table of Contents](README.md)
- [Previous Chapter](Wikis.md)

# Reports Page

This document defines the structure and logic for the **Reports Page** (`website/features/reports.html`).

## Overview

The reports page is a feature showcase page detailing the capabilities of the Tiny Gnomes reports tool.

## Visual Implementation

The visual structure is derived from the Calendar page layout. We use semantic HTML and custom CSS to recreate this design perfectly.

## Structure

The page uses standard HTML5 boilerplate, sharing the exact same header and footer as the main `index.html` page.

The main body (`<main>`) includes the following sections:
1. **Feature Header**: A centered title "Reports" with a yellow underline.
2. **Hero Section**: A section with a light blue organic background shape, a headline ("30K foot view, invoices, timelines"), a decorative element showing a reports icon (`reports-icon.png`), and a sticky screenshot of the reports app UI (`reports-screenshot.png`).
3. **Introduction**: Imagine if invoices wrote themselves.  Tiny Gnomes calculates and reports all your meetings and tasks with a single click.
4. **Feature List (Unordered)**:
    - **Customize** - Build reports with exactly who you want included, which projects, and over what time frame.
    - **Remember** - Once you build a report, save it with a unique name so you can pull it up again.
    - **Pick the right report for you** - Reports share data, so once you create a report, you can switch the report type without filling in the information again.
    - **Invoices** - A very fast way to generate an invoice. Grouped by Task or Event on the calendar.
    - **Timesheet** - Similar to an invoice but grouped by day.
    - **Members overview** - See at a glance who is late, who has the largest work load.
    - **Project open tasks** - See what needs to be done across projects.
    - **Project status** - Similar to Member overview, but rolled up into projects.
    - **Resource manager** - See how much time people have to get things done, and compare with other team members, to balance the load.
5. **Additional Features List (Ordered)**: A block with a title "Great features you won't want to live without", followed by a green-outlined box containing a numbered list of features:
    - **Print** - Use your browser to print a report, or save as a PDF (* you may need to configure this on your computer).
    - **Share** - Generate a Report that you can share with people outside of the system.

## Logic

Unlike the home page, this feature page contains **no entrance animations**. However, the reports icon and screenshot feature a hover zoom effect. The content should be fully visible on render.
No JavaScript is required for this page's core functionality (the mobile menu logic from `animations.js` can still apply to the shared header).

- [Next Chapter](Files.md)
