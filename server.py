import http.server
import socketserver
import os

PORT = 8000

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="website", **kwargs)

    def translate_path(self, path):
        # Translate the URL path to a local file system path.
        path = super().translate_path(path)
        
        # If the path doesn't exist and doesn't have an extension, try adding .html
        if not os.path.exists(path) and '.' not in os.path.basename(path):
            html_path = path + '.html'
            if os.path.exists(html_path):
                return html_path
                
        return path

Handler = CustomHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving HTTP on port {PORT} with .html auto-resolution...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
