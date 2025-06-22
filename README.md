# TinyGnomes Website

This repository contains the source code for the TinyGnomes website.

## Features

*   Simple and clean design.
*   Responsive layout for various devices.
*   Built with modern web technologies.

## Technologies Used

*   HTML5
*   CSS3 (with Tailwind CSS)
*   JavaScript

## Installation

To set up the project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/tinygnomes/Website.git
    cd Website
    ```
2.  **Install dependencies (if any, for Tailwind CSS compilation):**
    ```bash
    npm install
    ```

## Usage

To view the website:

### Development

1.  **Start Tailwind CSS compilation in watch mode:**
    This command watches for changes in `website/src/input.css` and compiles the output to `website/dist/output.css`.
    ```bash
    npm run dev
    ```

### Production Build

1.  **Compile Tailwind CSS for production:**
    This command compiles and minifies the CSS from `website/src/input.css` to `website/dist/output.css`.
    ```bash
    npm run build
    ```

### Viewing the Website

1.  **Open `website/index.html` in your web browser.****