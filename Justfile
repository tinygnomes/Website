set dotenv-load := true

serve:
    python3 server.py

serve-locofy:
    python3 -m http.server --directory Locofy 8001

serve-figma:
    uv run tools/figma-mcp.py
