from izzati import Backend, file_return

def pr(form, files):
    print(form)
    print(files)
    for x in files:
        x.save('/tmp/testing.jpg')
    #return file_return('/home/kusti8/Pictures/italian-landscape-mountains-nature.jpg')
    return {'hello': 'successsssssssssssssss'}

back = Backend(pr)
back.run()
