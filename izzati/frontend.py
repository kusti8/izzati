import requests
import json

class Frontend():
    def __init__(self, url):
        self.url = url

    def send(self, js=None, f=None):
        if f: # There is a file to send
            if json: # There is also json
                files = {'file': f}
                r = requests.post(self.url, data={'json': json.dumps(js)}, files=files)
            else: # There is only a file
                files = {'file': f}
                r = requests.post(self.url, files=files)
        else:
            r = requests.post(self.url, data={'json': json.dumps(js)})

        if r.headers['Content-Type'] == 'application/json':
            return r.json()
        else:
            return r.content
