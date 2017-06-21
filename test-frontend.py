from izzati import Frontend

f = Frontend('http://localhost:5020/')
out = f.send(js={'test': ['123', '456'], 'me': 'hi'}, f=open('/tmp/test.jpg', 'rb'))
print(out)
