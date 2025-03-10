from wsgiref.simple_server import make_server

def sample_app(environ, start_response):
    status = "200 OK"
    hears = [("Content-type", "text/plain")]
    start_response(status, hears)

    return [b"Assalomu alaykum"]

server = make_server("0.0.0.0", 8000, sample_app)
server.serve_forever()