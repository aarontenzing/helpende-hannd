from http.server import HTTPServer, BaseHTTPRequestHandler
import time

HOST = "192.168.56.1"
PORT = 8000

class testserverHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(home.html)

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type","application/json")
        self.end_headers()

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes("time " + date, "utf-8"))

server = HTTPServer((HOST, PORT), testserverHTTP)
print("server running...")
server.serve_forever()
server.server_close()
print("server stopped")