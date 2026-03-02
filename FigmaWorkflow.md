# Figma Workflow

This document explains our visual development workflow, which uses Figma as the visual "Source of Truth" while maintaining completely hand-crafted, semantic HTML/CSS without relying on automated "to-code" generators like Locofy.

## The Rationale

Automated code generators (like Locofy or many Figma plugins) often produce extremely bloated, `div`-heavy, non-semantic code. To build the TinyGnomes static site, we strictly require clean, human-readable, and semantic HTML (e.g., `<article>`, `<nav>`, `<section>`).

Our solution is **Decoupled Extraction**: 
Instead of automatically generating full DOM structures, we use a custom AI-integrated **Figma MCP Server**. This server allows the AI assistant to query the Figma REST API directly to fetch exact tokens (colors, fonts), precise coordinate geometry for complex CSS layouts, and directly export needed SVG graphics—while allowing the AI to write the semantic HTML itself based on our Markdown instructions.

This completely bypasses Figma's paid "Dev Mode" requirement, as we connect securely via the free REST API.

---

## Setup for New Developers

### 1. Generate a Figma Personal Access Token
To allow our local tools to read your Figma files:
1. Open Figma and go to your **Account Settings**.
2. Scroll to the **Personal Access Tokens** section.
3. Generate a new token (e.g., "TinyGnomes MCP").
4. Copy this string; you won't be able to see it again.

### 2. Find the Figma File ID
1. Open the TinyGnomes design file in Figma.
2. Look at the URL. It will look something like: `https://www.figma.com/file/abcdef123456/File-Name?...`
3. The File ID is the alphanumeric string (`abcdef123456`).

### 3. Provide Credentials Locally
Create a `.env` file in the root of the repository (`/var/home/giesse/Dev/TinyGnomes/`) if it doesn't already exist, and add your credentials:
```env
FIGMA_FILE_ID=your_extracted_file_id_here
FIGMA_ACCESS_TOKEN=your_generated_access_token_here
```

---

## Best Practices for Figma Hierarchy

Because the AI will interrogate the Figma document programmatically, the cleaner the Figma structure is, the more efficiently the agent can parse it.
*   **Name Nodes Semantically:** Instead of leaving a frame as "Frame 22", rename it in the Figma left-sidebar to something logical like `HeroImageGroup` or `PrimaryNav`.
*   **Group Logical Elements:** If three images need to overlap with exact CSS absolute positioning, group them in a Frame named `HeroOverlay`. The AI can query this specific Frame and retrieve the relative coordinates of all its children.

---

## Running the Server

If you are using an AI coding assistant (like Claude via an MCP client), you will need the AI to connect to the MCP server.

We use `uv` and `just` to manage and run the server effortlessly.
To run the server, simply use the Justfile command:
```bash
just serve-figma
```
This command automatically loads the `.env` file and executes the `tools/figma-mcp.py` script. The script manages its own dependencies (`mcp`, `requests`) transparently.
