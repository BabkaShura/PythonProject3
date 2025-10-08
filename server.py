from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """На любой GET-запрос возвращаем contacts.html"""
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        with open("contacts.html", "r", encoding="utf-8") as f:
            self.wfile.write(f.read().encode("utf-8"))

    def do_POST(self):
        """Обрабатываем POST-запрос, выводим данные в консоль"""
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length).decode("utf-8")

        # данные формы
        parsed_data = urllib.parse.parse_qs(post_data)
        print("📩 Получены данные от пользователя:", parsed_data)

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"<h1>Данные получены!</h1>")

if __name__ == "__main__":
    server_address = ("", 8000)  # http://localhost:8000
    httpd = HTTPServer(server_address, MyHandler)
    print("🚀 Сервер запущен на http://localhost:8000")
    httpd.serve_forever()