import http.server
import socketserver
import os
import re

PORT = 3000
DIRECTORY = "."

# Get the LaunchDarkly client-side SDK key
ld_client_key = os.getenv('LAUNCHDARKLY_CLIENT_KEY')
if not ld_client_key:
    print("Warning: LAUNCHDARKLY_CLIENT_KEY environment variable is not set")
    ld_client_key = 'YOUR-CLIENT-SIDE-SDK-KEY'

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        # Serve the file
        super().do_GET()

        # If we're serving script.js, inject the environment variable
        if self.path.endswith('script.js'):
            try:
                with open(os.path.join(DIRECTORY, 'script.js'), 'r') as f:
                    content = f.read()
                    # Replace the placeholder with the actual key
                    content = content.replace('YOUR-SDK-KEY', ld_client_key)
                    self.wfile.write(content.encode())
            except Exception as e:
                print(f"Error serving script.js: {e}")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    print("Make sure to set LAUNCHDARKLY_CLIENT_KEY environment variable")
    httpd.serve_forever()
