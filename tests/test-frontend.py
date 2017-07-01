from izzati import Frontend

f = Frontend('http://localhost:5020/')
out = f.send(js={'test': ['123', '456'], 'me': 'hi'}, f=open('/home/kusti8/Pictures/sprite.jpg', 'rb'))
with open('/home/kusti8/test.jpg', 'wb') as p:
    p.write(out)
