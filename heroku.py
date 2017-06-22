from izzati import Backend
import os
import requests

url = os.environ['CALLBACK']
response = requests.get(url)
with open('callback.py', 'wb') as f:
    f.write(response.content)

import callback

def pr(form, files):
    print(form)
    return {'It': 'Worked'}

back = Backend(callback.callback)
back.run(port=int(os.environ['PORT']))
