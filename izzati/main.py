from flask import Flask, jsonify, request, send_file
from flask.views import View
import json
import multiprocessing

def p(form, files):
    print(form, [x.filename for x in files])
    return {'result': 'success'}

def file_return(path):
    """Provide a method to return a file instead
    of a string"""
    return send_file(path)

def background(target, args=(), kwargs={}):
    q = multiprocessing.Queue()
    args = (q,) + args
    p = multiprocessing.Process(target=target, args=args, kwargs=kwargs, daemon=True)
    p.start()
    return p, q

class FlaskHandle(View):
    methods=['POST']
    def __init__(self, callback=p, queue=None, args=(), kwargs={}):
        self.callback = callback
        self.queue = queue
        self.args = args
        self.kwargs = kwargs

    def run_callback(self, data, files):
        if self.queue:
            return self.callback(self.queue, data, files, *self.args, **self.kwargs)
        else:
            return self.callback(data, files, *self.args, **self.kwargs)

    def dispatch_request(self):
        files = request.files.getlist('file')
        if request.form:
            js = dict(request.form)
            for key, value in js.items():
                if len(value) == 1:
                    js[key] = value[0]
        else:
            js = '{}'

        ret = self.run_callback(js, files)
        try:
            return jsonify(ret)
        except:
            return ret # File is returned


class Backend():
    def __init__(self, callback=p, args=(), kwargs={}, background=False):
        self.app = Flask('backend')
        self.callback = callback
        self.background = background
        if background:
            self.q = multiprocessing.Queue()
            self.app.add_url_rule('/', view_func=FlaskHandle.as_view('backend', callback=callback, queue=self.q, args=args, kwargs=kwargs))
        else:
            self.q = None
            self.app.add_url_rule('/', view_func=FlaskHandle.as_view('backend', callback=callback, args=args, kwargs=kwargs))

    def run(self, host="0.0.0.0", port=5020, use_reloader=False):
        if self.background:
            return self.run_background(host=host, port=port)
        self.app.run(host=host, port=port, debug=True, use_reloader=use_reloader)

    def run_background(self, host="0.0.0.0", port=5020):
        p = multiprocessing.Process(target=self.app.run, kwargs={'host': host, 'port': port, 'debug': True, 'use_reloader': False}, daemon=True)
        p.start()
        return p, self.q
