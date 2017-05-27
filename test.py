from izzati import Backend, file_return

def pr(form, files):
    print(form)
    for x in files:
        print(x.filename)
    o = file_return('/tmp/test.jpg')
    return o
back = Backend(pr)
back.run()
