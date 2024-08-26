import http.server
import socketserver
import os
import argparse
class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        # Get the length of the data
        content_length = int(self.headers['Content-Length'])
        file_name = os.path.basename(self.path)
        # Read the POST data
        post_data = self.rfile.read(content_length)

        with open(file_name, 'w+') as file:
            file.write(post_data.decode('utf-8'))

        # Send a 200 OK response
        self.send_response(200)
        self.end_headers()

        # Respond with a message
        self.wfile.write(b"POST request received successfully")

def main(args):
    # Define the server address and port
    server_address = (args.lip, args.port)

    # Create the HTTP server
    with socketserver.TCPServer(server_address, MyHTTPRequestHandler) as httpd:
        print(f"Serving at http://{args.lip}:{args.port}/")
        httpd.serve_forever()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", '--lip', type=str, help="Local Host IP, Default: 0.0.0.0", default="0.0.0.0")
    parser.add_argument("-p", "--port", type=int, help="Local Host Port, Default: 8080", default='8080')
    args = parser.parse_args()
    main(args)