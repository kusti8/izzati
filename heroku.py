from izzati import Backend

def pr(form, files):
    print(form)
    return {'It': 'Worked'}

back = Backend(pr)
back.run()
