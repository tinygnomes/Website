- [Table of Contents](README.md)
- [Previous Chapter](Compliance.md)

# Tasks Page

This document defines the structure and logic for the **Tasks Page** (`website/features/tasks.html`).

## Overview

The tasks page is a feature showcase page detailing the capabilities of the Tiny Gnomes tasks tool.

## Visual Implementation

The visual structure is derived from the Calendar page layout. We use semantic HTML and custom CSS to recreate this design perfectly.

## Structure

The page uses standard HTML5 boilerplate, sharing the exact same header and footer as the main `index.html` page.

The main body (`<main>`) includes the following sections:
1. **Feature Header**: A centered title "Tasks" with a yellow underline.
2. **Hero Section**: A section with a light blue organic background shape, a headline ("View the big picture Or, laser focus on just one project."), a decorative element showing a tasks icon (`tasks-icon.png`), and a sticky screenshot of the tasks app UI (`tasks-screenshot.png`).
3. **Introduction**: Never drop the ball, and keep your team laser focused.  There are no tricks.  Decades of Project Management has taught us it’s all about communication.  Meet with your team, review, review, review.
4. **Feature List (Unordered)**:
    - **Roles** - There are three roles:
        1. **Lead** - The person who double checks the work being done, and closes out the task eventually.
        2. **Doer** - A single Doer, who accepts responsibility for the task, and marks it done.
        3. **Watcher**(s) (optional) - People you want to see all conversations in the task. People can add/remove themselves to a task if they want to get notifications about it.
    - **Filters** - It is easy to filter down to just the tasks you care about. Always start with Ticklers, which default to showing you your own tasks you need to accept. Change this to "All" and see all tasks.
    - **Import/Export** - Tasks can be exported and imported from popular Spreadsheet applications. This allows you to work offline, building or changing complex task lists and import them back in quickly.
5. **Additional Features List (Ordered)**: A block with a title "Great features you won't want to live without", followed by a green-outlined box containing a numbered list of features:
    - **Start or end date** - If set, the day before the task will turn dark red. On the date and after, it will be bright red.
    - **Time** - Set the estimated time, as a metric for reports. Track exactly when and for how long you worked on a task.
    - **Priority** - The magic of staying on top of things.
        a. A priority of 1 (!1) means do this now. 
        b. !2 means do this if you have no !1. 
        c. !3 means, don't do this now until we review it again. No priority  means no one cares enough about this task yet.
    - **Milestones** - Milestones are treated in a very simple way. It is a single date, that you give a label, like "200 days out" or "Beta". When you give a task a milestone, it will turn dark red. On the date and after, it will be bright red. Compare this to a "deadline" set for an entire project, which when passed, ALL tasks will turn red.
    - **Private** - Only Leads in the project, and people invited to the task directly will be able to see the task, or the conversations in it.
    - **Calendar** - Put the task on your calendar. This has many options such as having the task follow you from day to day, or simply place the task on a specific day.
    - **Remind** - Want to remind yourself with an email, or even the whole team? Easy!
    - **Recurring** - Do you need to make sure someone does something every week, or every month? Never let the ball drop.
    - **Category** - Group like tasks together, and if you need even finer resolution, there is a sub-category as well.
    - **History** - Quickly see everything that ever happened on a task.

## Logic

Unlike the home page, this feature page contains **no entrance animations**. However, the tasks icon and screenshot feature a hover zoom effect. The content should be fully visible on render.
No JavaScript is required for this page's core functionality (the mobile menu logic from `animations.js` can still apply to the shared header).

- [Next Chapter](Wikis.md)
