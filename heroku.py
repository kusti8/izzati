from izzati import Backend
import os
import requests

previous = ''

def check():
    url = os.environ['CALLBACK']
    response = requests.get(url)
    if response.text != previous:
        previous = response.text
        exec(response.text, globals())

def call(form, files):
    check()
    return callback(form, files)

back = Backend(call)
back.run(port=int(os.environ['PORT']))
