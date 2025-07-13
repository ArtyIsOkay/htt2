from http.server import BaseHTTPRequestHandler, HTTPServer

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<h1>This is my server!</h1><p>Port 8000</p>", "utf-8"))

server = HTTPServer(("localhost", 8000), MyServer)
server.serve_forever()