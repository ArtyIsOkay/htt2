import http.server
import socketserver

with socketserver.TCPServer(("", 8000), http.server.SimpleHTTPRequestHandler) as httpd:
    print("Server running at http://0.0.0.0:8000")
    httpd.serve_forever()
    