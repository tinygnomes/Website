import os
import shutil
import signal
import sys
import threading
import webbrowser
from pathlib import Path
from flask import Flask, render_template_string, request, send_from_directory, jsonify
from PIL import Image

# Configuration
ASSETS_DIR = Path("website/assets").resolve()
LOCOFY_ASSETS_DIR = Path("Locofy/public").resolve()
HTML_FILE = Path("website/index.html").resolve()
HOST = "localhost"
PORT = 5000

app = Flask(__name__)

# --- Helper Functions ---

def get_file_list(directory):
    files = []
    if not directory.exists(): return []
    for p in sorted(directory.glob("*")):
        if p.suffix.lower() in ['.png', '.jpg', '.jpeg', '.svg', '.gif']:
            try:
                size_kb = p.stat().st_size / 1024
                dims = "?"
                if p.suffix.lower() != '.svg':
                    with Image.open(p) as img:
                        dims = f"{img.size[0]}x{img.size[1]}"
                
                files.append({
                    "name": p.name,
                    "path": str(p),
                    "size": f"{size_kb:.1f} KB",
                    "dims": dims,
                    "src": f"/file?path={p}"
                })
            except:
                pass
    return files

def update_html(old_name, new_name):
    if not HTML_FILE.exists(): return False
    content = HTML_FILE.read_text()
    if old_name in content:
        HTML_FILE.write_text(content.replace(old_name, new_name))
        return True
    return False

# --- Routes ---

@app.route('/')
def dashboard():
    return render_template_string(DASHBOARD_TEMPLATE)

@app.route('/api/files')
def api_files():
    targets = get_file_list(ASSETS_DIR)
    sources = get_file_list(LOCOFY_ASSETS_DIR)
    return jsonify({"targets": targets, "sources": sources})

@app.route('/file')
def serve_file():
    path_str = request.args.get('path')
    if not path_str: return "Missing path", 400
    p = Path(path_str)
    # Security: strict check
    if not str(p).startswith(str(Path.cwd())):
        return "Access denied", 403
    if not p.exists():
        return "Not found", 404
    return send_from_directory(p.parent, p.name)

@app.route('/api/compare', methods=['POST'])
def api_compare():
    data = request.json
    target_path = Path(data['target'])
    source_path = Path(data['source'])
    
    # Just validation
    if not target_path.exists() or not source_path.exists():
        return jsonify({"error": "File not found"}), 404
        
    return jsonify({"status": "ready"})

@app.route('/api/replace', methods=['POST'])
def api_replace():
    data = request.json
    target_path = Path(data['target'])
    source_path = Path(data['source'])
    
    if not source_path.exists(): return jsonify({"error": "Source missing"}), 404

    try:
        new_ext = source_path.suffix.lower()
        target_name_stem = target_path.stem
        new_target_name = target_name_stem + new_ext
        new_target_path = ASSETS_DIR / new_target_name
        
        # Copy
        shutil.copy2(source_path, new_target_path)
        
        # Update HTML
        updated = False
        if new_target_name != target_path.name:
             updated = update_html(target_path.name, new_target_name)
             if target_path.exists() and target_path != new_target_path:
                 target_path.unlink()
        
        # Delete source if it is in the same dir (deduplication)
        # OR if we just want to treat sources as consumable
        # Let's keep sources in Locofy unless explicitly told, 
        # BUT if source is in ASSETS_DIR (merged), delete it.
        if source_path.parent == ASSETS_DIR and source_path != new_target_path:
            source_path.unlink()

        return jsonify({"success": True, "updated_html": updated, "new_name": new_target_name})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/delete', methods=['POST'])
def api_delete():
    data = request.json
    p = Path(data['path'])
    if not str(p).startswith(str(ASSETS_DIR)) and not str(p).startswith(str(LOCOFY_ASSETS_DIR)):
        return jsonify({"error": "Access denied"}), 403
    
    try:
        p.unlink()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/shutdown', methods=['POST'])
def shutdown():
    os.kill(os.getpid(), signal.SIGINT)
    return "Shutting down..."

# --- Templates ---

DASHBOARD_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Asset Dashboard</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; margin: 0; display: flex; flex-direction: column; height: 100vh; background: #222; color: #eee; }
        header { padding: 15px; background: #333; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #444; }
        .main { display: flex; flex: 1; overflow: hidden; }
        
        .panel { flex: 1; display: flex; flex-direction: column; border-right: 1px solid #444; min-width: 0; }
        .panel:last-child { border-right: none; }
        
        .panel-header { padding: 10px; background: #2a2a2a; font-weight: bold; text-align: center; border-bottom: 1px solid #444; }
        
        .grid { flex: 1; overflow-y: auto; padding: 10px; display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 10px; align-content: start; }
        
        .card { background: #333; border-radius: 6px; padding: 10px; text-align: center; cursor: grab; transition: transform 0.1s; position: relative; }
        .card:hover { background: #444; }
        .card img { max-width: 100%; height: 100px; object-fit: contain; background: #ccc; border-radius: 4px; }
        .name { font-size: 0.85em; margin-top: 8px; word-break: break-all; color: #fff; }
        .meta { font-size: 0.75em; color: #aaa; margin-top: 4px; }
        
        /* Dragging */
        .card.dragging { opacity: 0.5; }
        .card.drag-over { border: 2px dashed #4caf50; background: #2e3e30; }

        /* Modal */
        .modal-overlay { display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.8); z-index: 100; align-items: center; justify-content: center; }
        .modal { background: #222; padding: 30px; border-radius: 12px; border: 1px solid #555; max-width: 90%; max-height: 90%; display: flex; flex-direction: column; }
        .compare-row { display: flex; gap: 30px; margin-bottom: 30px; justify-content: center; }
        .compare-item { text-align: center; min-width: 300px; }
        .compare-img-box { width: 300px; height: 300px; background: #333; display: flex; align-items: center; justify-content: center; border: 1px solid #555; }
        .compare-img-box img { max-width: 100%; max-height: 100%; }
        
        .actions { display: flex; justify-content: center; gap: 20px; }
        button { padding: 12px 24px; font-size: 1.1em; border-radius: 6px; border: none; cursor: pointer; }
        .btn-replace { background: #4caf50; color: white; }
        .btn-cancel { background: #666; color: white; }
        .btn-delete { background: #d9534f; color: white; font-size: 0.8em; margin-top: 5px;}

    </style>
</head>
<body>
    <header>
        <div><strong>TinyGnomes</strong> Asset Dashboard</div>
        <button class="btn-cancel" onclick="shutdown()" style="font-size: 0.9em; padding: 8px 16px;">Finish & Exit</button>
    </header>
    
    <div class="main">
        <div class="panel">
            <div class="panel-header">🎯 Target (website/assets)</div>
            <div class="grid" id="grid-targets"></div>
        </div>
        <div class="panel">
            <div class="panel-header">📦 Source (Locofy/public)</div>
            <div class="grid" id="grid-sources"></div>
        </div>
    </div>

    <!-- Comparison Modal -->
    <div class="modal-overlay" id="modal">
        <div class="modal">
            <h2 style="text-align:center; margin-top:0;">Confirm Replacement</h2>
            <div class="compare-row">
                <div class="compare-item">
                    <h3>Keep / Target</h3>
                    <div class="compare-img-box"><img id="img-target"></div>
                    <div class="meta" id="meta-target"></div>
                </div>
                <div style="display:flex; align-items:center; font-size: 2em;">&larr;</div>
                <div class="compare-item">
                    <h3>Replace With</h3>
                    <div class="compare-img-box"><img id="img-source"></div>
                    <div class="meta" id="meta-source"></div>
                </div>
            </div>
            <div class="actions">
                <button class="btn-cancel" onclick="closeModal()">Cancel</button>
                <button class="btn-replace" onclick="executeReplace()">Confirm Replace</button>
            </div>
        </div>
    </div>

    <script>
        let pendingReplace = null;

        function loadFiles() {
            fetch('/api/files').then(r => r.json()).then(data => {
                renderGrid('grid-targets', data.targets, true);
                renderGrid('grid-sources', data.sources, false);
            });
        }

        function renderGrid(id, files, isTarget) {
            const container = document.getElementById(id);
            container.innerHTML = '';
            files.forEach(f => {
                const el = document.createElement('div');
                el.className = 'card';
                el.draggable = !isTarget; // Only sources are draggable
                el.innerHTML = `
                    <img src="${f.src}">
                    <div class="name">${f.name}</div>
                    <div class="meta">${f.dims} | ${f.size}</div>
                    ${ !isTarget ? '<button class="btn-delete" onclick="deleteFile(\\'' + f.path.replace(/\\\\/g, '\\\\\\\\') + '\\')">Del</button>' : ''}
                `;
                
                // Data
                el.dataset.path = f.path;
                el.dataset.src = f.src;
                el.dataset.name = f.name;
                el.dataset.meta = `${f.dims} | ${f.size}`;

                // Drag Events
                if (!isTarget) {
                    el.addEventListener('dragstart', e => {
                        e.dataTransfer.setData('application/json', JSON.stringify(f));
                        el.classList.add('dragging');
                    });
                    el.addEventListener('dragend', () => el.classList.remove('dragging'));
                    
                    // Click to delete logic handled by button
                } else {
                    el.addEventListener('dragover', e => {
                        e.preventDefault();
                        el.classList.add('drag-over');
                    });
                    el.addEventListener('dragleave', () => el.classList.remove('drag-over'));
                    el.addEventListener('drop', e => {
                        e.preventDefault();
                        el.classList.remove('drag-over');
                        const srcData = JSON.parse(e.dataTransfer.getData('application/json'));
                        openCompare(f, srcData);
                    });
                }
                container.appendChild(el);
            });
        }

        function openCompare(target, source) {
            pendingReplace = { target, source };
            document.getElementById('img-target').src = target.src;
            document.getElementById('meta-target').innerText = `${target.name} (${target.dims} | ${target.size})`;
            
            document.getElementById('img-source').src = source.src;
            document.getElementById('meta-source').innerText = `${source.name} (${source.dims} | ${source.size})`;
            
            document.getElementById('modal').style.display = 'flex';
        }

        function closeModal() {
            document.getElementById('modal').style.display = 'none';
            pendingReplace = null;
        }

        function executeReplace() {
            if (!pendingReplace) return;
            const { target, source } = pendingReplace;
            
            fetch('/api/replace', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ target: target.path, source: source.path })
            }).then(r => r.json()).then(res => {
                if (res.success) {
                    closeModal();
                    loadFiles(); // Reload
                } else {
                    alert('Error: ' + res.error);
                }
            });
        }

        function deleteFile(path) {
            if(confirm("Delete this file permanently?")) {
                fetch('/api/delete', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({path})
                }).then(() => loadFiles());
            }
        }

        function shutdown() {
            fetch('/shutdown', {method: 'POST'});
            document.body.innerHTML = "<h1 style='text-align:center;color:#fff;margin-top:50px;'>Done. Tab closed.</h1>";
            window.close();
        }

        loadFiles();
    </script>
</body>
</html>
"""

def main():
    print(f"Starting Asset Dashboard at http://{HOST}:{PORT}")
    threading.Timer(1.0, lambda: webbrowser.open(f"http://{HOST}:{PORT}")).start()
    app.run(host=HOST, port=PORT, debug=False)

if __name__ == "__main__":
    main()
