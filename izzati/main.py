from flask import Flask, jsonify, request, send_file
from flask.views import View
import json

def p(form, files):
    print(form, [x.filename for x in files])
    return {'result': 'success'}

def file_return(path):
    """Provide a method to return a file instead
    of a string"""
    return send_file(path)

class FlaskHandle(View):
    methods=['POST']
    def __init__(self, callback=p):
        self.app = Flask('backend')
        self.callback = callback

    def dispatch_request(self):
        files = request.files.getlist('file')
        if request.form:
            js = dict(request.form)
            for key, value in js.items():
                if len(value) == 1:
                    js[key] = value[0]
        else:
            js = '{}'
        try:
            return jsonify(self.callback(js, files))
        except:
            return self.callback(js, files) # File is returned

    def run(self, host="0.0.0.0", port=5020):
        self.app.run(host=host, port=port)

class Backend():
    def __init__(self, callback=p):
        self.app = Flask('backend')
        self.callback = callback
        self.app.add_url_rule('/', view_func=FlaskHandle.as_view('backend', callback=callback))

    def run(self, host="0.0.0.0", port=5020):
        self.app.run(host=host, port=port, debug=True)
