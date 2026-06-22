#!/usr/bin/env python3
import http.server
import socketserver
import webbrowser
import threading
import os
import json
import glob

PORT = 8080

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/games':
            files = sorted(glob.glob('*.json'))
            body = json.dumps(files).encode()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', len(body))
            self.end_headers()
            self.wfile.write(body)
        else:
            super().do_GET()

    def log_message(self, format, *args):
        pass  # suppress request noise

print(f"Jeopardy running at http://localhost:{PORT}")
print("Press Ctrl+C to stop.\n")

threading.Thread(target=lambda: (
    __import__('time').sleep(0.5),
    webbrowser.open(f"http://localhost:{PORT}")
), daemon=True).start()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
