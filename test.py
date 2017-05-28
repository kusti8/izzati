from izzati import Backend, file_return

def pr(form, files):
    print(form)
    for x in files:
        x.save('/tmp/test.jpg')
    return {'It': 'Worked'}

back = Backend(pr)
back.run()
