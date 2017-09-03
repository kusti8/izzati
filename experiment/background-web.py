from izzati import Backend

def callback(q, text, data):
    q.put(text)
    return {'status': 'OK'}

b = Backend(callback, background=True)
p, q = b.run()

while True:
    print("yes", q.get())
