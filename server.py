from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    # Обработка GET-запросов
    def do_GET(self):
        if self.path == '/':
            self._send_response({'status': 'ok', 'message': 'DevOps HTTP Server is running!'})
        elif self.path == '/health':
            self._send_response({'status': 'healthy'})
        else:
            self._send_response({'error': 'Not Found'}, status=404)

    # Обработка POST-запросов
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length) if content_length > 0 else b''

        try:
            data = json.loads(body.decode('utf-8')) if body else {}
        except json.JSONDecodeError:
            data = {}

        self._send_response({
            'status': 'received',
            'your_data': data
        }, status=201)

    # Вспомогательный метод для отправки JSON-ответов
    def _send_response(self, data, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        response_json = json.dumps(data)
        self.wfile.write(response_json.encode('utf-8'))

def run(port=8080):
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Сервер запущен на 0.0.0.0:{port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nОстановка сервера...")
        httpd.server_close()

if __name__ == '__main__':
    run()