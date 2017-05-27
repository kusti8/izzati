from izzati import Frontend

f = Frontend('http://localhost:5020/')
out = f.send(js={'test': '123'}, f=open('/tmp/test.jpg', 'rb'))
print("done")
open('/tmp/t.jpg', 'wb').write(out)
