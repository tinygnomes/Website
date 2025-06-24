# How-To: Set Up Local Development Environment

This guide provides step-by-step instructions for setting up your local development environment for the TinyGnomes project.

## Prerequisites
*   Node.js (LTS version recommended)
*   npm (Node Package Manager, usually comes with Node.js)

## Steps

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/tinygnomes/Website.git
    cd Website
    ```

2.  **Install Dependencies**:
    Navigate to the project root directory and install the necessary npm packages, including Tailwind CSS.
    ```bash
    npm install
    ```

3.  **Start Development Server**:
    To compile Tailwind CSS and watch for changes, run the development script. This will generate `website/dist/output.css`.
    ```bash
    npm run dev
    ```
    This command will keep running in your terminal, recompiling CSS whenever you make changes to HTML or `input.css`.

4.  **Open `index.html`**:
    Open the `website/index.html` file in your web browser to view the project. You can simply drag and drop the file into your browser, or open it via your file explorer.

5.  **Create a Production Build**:
    When you are ready to deploy the website, you should create a minified version of the CSS for better performance.
    ```bash
    npm run build
    ```
    This command will generate a new `website/dist/output.css` file that is smaller and optimized for production.

## Troubleshooting
*   If `npm install` fails, ensure you have Node.js and npm correctly installed and updated.
*   If styles are not applying, verify that `npm run dev` is running and that `website/dist/output.css` is correctly linked in `website/index.html`.