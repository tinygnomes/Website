# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "mcp",
#     "requests"
# ]
# ///

import os
import requests
import json
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("Figma MCP Server")

BASE_URL = "https://api.figma.com/v1"

def _headers():
    token = os.environ.get("FIGMA_ACCESS_TOKEN")
    file_id = os.environ.get("FIGMA_FILE_ID")
    if not token:
        raise ValueError("FIGMA_ACCESS_TOKEN environment variable is required")
    if not file_id:
        raise ValueError("FIGMA_FILE_ID environment variable is required")
    return {"X-Figma-Token": token}

def _get_file_id():
    file_id = os.environ.get("FIGMA_FILE_ID")
    if not file_id:
        raise ValueError("FIGMA_FILE_ID environment variable is required")
    return file_id

@mcp.tool()
def list_figma_hierarchy(depth: int = 2) -> str:
    """
    Traverses the Figma file structure to list names and IDs of pages, frames, and groups.
    Depth specifies how deep to query the document tree.
    """
    file_id = _get_file_id()
    response = requests.get(f"{BASE_URL}/files/{file_id}?depth={depth}", headers=_headers())
    response.raise_for_status()
    data = response.json()
    
    output = []
    def traverse(node, current_depth, max_depth):
        indent = "  " * current_depth
        node_type = node.get("type", "UNKNOWN")
        node_name = node.get("name", "Unnamed")
        node_id = node.get("id", "Unknown ID")
        output.append(f"{indent}- [{node_type}] {node_name} (ID: {node_id})")
        
        if current_depth < max_depth and "children" in node:
            for child in node.get("children", []):
                traverse(child, current_depth + 1, max_depth)
                
    if "document" in data:
        traverse(data["document"], 0, depth)
    return "\n".join(output)

@mcp.tool()
def get_figma_styles() -> str:
    """
    Queries the file to extract local design tokens (colors, text styles) metadata.
    Note: For definitive values, you may need to use get_node_details on the nodes using these styles.
    """
    file_id = _get_file_id()
    response = requests.get(f"{BASE_URL}/files/{file_id}?depth=1", headers=_headers())
    response.raise_for_status()
    data = response.json()
    return json.dumps(data.get("styles", {}), indent=2)

@mcp.tool()
def get_node_details(node_ids: list[str]) -> str:
    """
    Searches the document tree to return detailed data for specific components by their exact IDs.
    Returns absoluteBoundingBox, padding, gap, and children details.
    """
    if not node_ids:
        return "{}"
    file_id = _get_file_id()
    ids_str = ",".join(node_ids)
    response = requests.get(f"{BASE_URL}/files/{file_id}/nodes?ids={ids_str}", headers=_headers())
    response.raise_for_status()
    data = response.json()
    return json.dumps(data.get("nodes", {}), indent=2)

@mcp.tool()
def export_figma_asset(node_id: str, format: str = "svg") -> str:
    """
    Calls Figma's image export API to generate a temporary URL for an SVG or PNG/JPG.
    Downloads the resulting file directly to the website/images directory.
    Format must be one of: svg, png, jpg, pdf.
    """
    if format.lower() not in ["svg", "png", "jpg", "pdf"]:
        raise ValueError("format must be svg, png, jpg, or pdf")
    
    file_id = _get_file_id()
    response = requests.get(f"{BASE_URL}/images/{file_id}?ids={node_id}&format={format.lower()}", headers=_headers())
    response.raise_for_status()
    data = response.json()
    
    images = data.get("images", {})
    url = images.get(node_id)
    if not url:
        return f"Failed to export asset for node {node_id}: No URL returned from Figma."
        
    image_response = requests.get(url)
    image_response.raise_for_status()
    
    output_dir = "website/images"
    os.makedirs(output_dir, exist_ok=True)
    
    safe_node_id = node_id.replace(':', '_')
    file_path = os.path.join(output_dir, f"{safe_node_id}.{format.lower()}")
    
    if format.lower() == "svg":
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(image_response.text)
    else:
        with open(file_path, "wb") as f:
            f.write(image_response.content)
            
    return f"Asset downloaded successfully to {file_path}"

if __name__ == "__main__":
    mcp.run()
