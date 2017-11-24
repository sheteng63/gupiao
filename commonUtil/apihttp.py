import requests
import json
import json
class apicommonhttp:
    def __init__(self, url):
        self.url = url
        self.bodys = {}
        self.headers = {}
        pass

    def addHeaders(self, k, v):
        self.headers[k] = v
        return self

    def addBody(self, k, v):
        self.bodys[k] = v
        return self

    def get(self):
        r = requests.get(self.url, self.bodys, headers=self.headers)
        return json.loads(r.text)

    def post(self):
        r = requests.post(self.url, self.bodys, headers=self.headers)
        return json.loads(r.text)
