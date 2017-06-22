from izzati import Backend
import os

def pr(form, files):
    print(form)
    return {'It': 'Worked'}

back = Backend(pr)
back.run(port=int(os.environ['PORT']))
