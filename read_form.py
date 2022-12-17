import socketserver
import json
import socket

from http.server import HTTPServer, BaseHTTPRequestHandler

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Read the request body
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        # Parse the request body as JSON
        data = json.loads(body)

        # Get the input text from the request
        input_text = data['input']

        # Send the input text to the Python application
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('localhost', 10000))
            s.sendall(input_text.encode())

        # Send a response to the client
        self.send_response(200)
        self.end_headers()

if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyRequestHandler)
    httpd.serve_forever()
