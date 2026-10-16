import http.server, functools, sys
class H(http.server.SimpleHTTPRequestHandler):
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map, '.txt':'text/plain; charset=utf-8', '.html':'text/html; charset=utf-8', '.xml':'application/xml; charset=utf-8', '':'application/octet-stream'}
http.server.ThreadingHTTPServer(('127.0.0.1', int(sys.argv[1])), functools.partial(H, directory=sys.argv[2])).serve_forever()
