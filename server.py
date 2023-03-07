from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs,urlparse

import client
import param

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _set_response1(self):  # plain text
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

    def do_GET(self):
        # logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        print("p1="+str(self.path))
        parsed_url = urlparse(str(self.path))
        values = parse_qs(parsed_url.query)
        print("p2=", values)
        if str(self.path).endswith("start?"):  # session begin
            self._set_response1()
            a=client.start()
            self.wfile.write(bytes(a,'UTF-8'))
        elif str(self.path).endswith("stop?"):   # session end
            self._set_response1()
            a = client.stop()
            self.wfile.write(a.encode('utf-8'))
        elif "cs" in values:   # select diferent folder
            self._set_response1()
            a = values["cs"][0]
            res=param.load_param(a)
            self.wfile.write(res.encode('utf-8'))
            self.wfile.write(a.encode('utf-8'))
        else:
            self._set_response()                  # load initial html page
            content = open("a1.html", 'rb').read()
            self.wfile.write(content)


    def do_POST(self):
        # processing of the client text
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data1 = self.rfile.read(content_length)  # <--- Gets the data itself
        post_data2 = post_data1.decode('utf-8')
        post_data = parse_qs(post_data2)
        self._set_response1()
        s=post_data.get("fname")[0]
        s=s.strip()
        a = client.request_answer(s)
        self.wfile.write(a.encode('utf-8'))


def run(server_class=HTTPServer, handler_class=S, port=8080):
    # logging.basicConfig(level=logging.INFO)
    ip=''
    server_address = (ip, port)
    httpd = server_class(server_address, handler_class)
    # logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


# logging.info('Stopping httpd...\n')


if __name__ == '__main__':
    from sys import argv
    param.load_param("default")
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
# <input id="submit" type="submit" value="Submit" >
