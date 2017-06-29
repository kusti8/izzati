from izzati import Frontend

f = Frontend('https://peaceful-hamlet-29609.herokuapp.com/')
out = f.send(js={'test': ['123', '456'], 'me': 'hi'})
print(out)
