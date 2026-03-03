- [Table of Contents](README.md)
- [Previous Chapter](Share.md)

# Chat Page

This document defines the structure and logic for the **Chat Page** (`website/features/chat.html`).

## Overview

The chat page is a feature showcase page detailing the capabilities of the Tiny Gnomes chat tool.

## Visual Implementation

The visual structure is derived from the Calendar page layout. We use semantic HTML and custom CSS to recreate this design perfectly.

## Structure

The page uses standard HTML5 boilerplate, sharing the exact same header and footer as the main `index.html` page.

The main body (`<main>`) includes the following sections:
1. **Feature Header**: A centered title "Chat" with a yellow underline.
2. **Hero Section**: A section with a light blue organic background shape, a headline ("Everyone has something to say"), a decorative element showing a chat icon (`chat-icon.png`), and a sticky screenshot of the chat app UI (`chat-screenshot.png`).
3. **Introduction**: Know the phrase ‘give someone enough slack to hang themselves?’  Want to learn how to make each message count?
4. **Feature List (Unordered)**:
    - **Forums** - The discussions service allows you to see what everyone is saying in project forums.
    - **Topics** - A topic is a thread in a forum. A way to keep things organized and people focused. Make new ones as you need them, or rename them to better fit the flow of conversation.
    - **Threads** - Events on the calendar, and tasks, and compliances all of their own thread for each service. This way, you can keep a conversation inside task for example, without annoying everyone else in a project.
    - **Private messages** - Just like every popular social system out there these days, it's easy to send someone a private message. Just click on their photo and select this from the drop-down menu.
    - **Email** - When someone writes a message, it is also sent via Email, so you don't even need to log in to receive or replay to a thread.
    - **Filters** - Filter your message by the poster, project, service, or data ranges, or just search across all messages for anything you like.
5. **Additional Features List (Ordered)**: A block with a title "Power features", followed by a green-outlined box containing a numbered list of features:
    - **Tags** - You can tag any message in a thread whenever you like. Before you post it, while you writing it, or even after you post it. And, you can tag messages other people wrote.
    - **(@) Tag a person** - as long as people use a real name or nickname, it is easy to tag them directly. Just start typing their name, starting with a capital letter, and you will be presented with a list of the people.
    - **Hot** - A special type of tag with several levels of heat. Marking a message hot helps you remember it later, across services and projects.
    - **(?) Track a question** - Simply type two ?? and you will be promoted to mark a message as having a question. you can filter for these 'Standing questions' and clear this flag only when you get the answer you need.

## Logic

Unlike the home page, this feature page contains **no entrance animations**. However, the chat icon and screenshot feature a hover zoom effect. The content should be fully visible on render.
No JavaScript is required for this page's core functionality (the mobile menu logic from `animations.js` can still apply to the shared header).

- [Next Chapter](More.md)
