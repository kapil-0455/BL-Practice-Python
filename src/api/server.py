import json
from http.server import BaseHTTPRequestHandler, HTTPServer

results = []

class APIHandler(BaseHTTPRequestHandler):

    def send_json(self , status_code , data ):
        response = json.dumps(data).encode("utf-8")

        self.send_response(status_code)
        self.send_header("Content-Type" , "application/json")

        self.send_header("Content-Length" , str(len(response)))

        self.end_headers()
        self.wfile.write(response)


    def do_GET(self):

        if self.path == "/health":
            self.send_json(200 , {"status" : "ok"})

        elif self.path =="/results":
            self.send_json(200 , {"results" : results})
        else :
            self.self.send_json(404 , {"error" : "Not Found"})

    def do_POST(self):

        if self.path != "/crawl":

            self.send_json(404 , {"error" : "Not Found"})
            return 

        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)
        data = json.loads(body)
        urls = data.get("urls" , [])

        results.clear()

        for url in urls:

            results.append({"url" : url , "status" : "pending"})

        self.send_json(200 , {"message" : "URLs received" , "count" : len(urls)})



server = HTTPServer(("localhost" , 8000) , APIHandler)
print("Server running on http://localhost:8000")

server.serve_forever()
