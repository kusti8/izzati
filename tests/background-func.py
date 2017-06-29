from izzati import Backend, background

def callback(webq, text, data, q):
    print(text, [x.filename for x in data])
    q.put(text['name'])
    webq.put(text['test'])
    return {'status': 'OK'}

def background_process(q, greeting):
    while True:
        name = q.get()
        print(greeting + ", " + name)

p, q = background(background_process, args=("Hello",))
# Also supports default arguments with kwargs:
# p, q = background(background_process, kwargs={"greeting": "Hello"})

b = Backend(callback, args=(q,), background=True)
# Also supports default arguments with kwargs:
# b = Backend(callback, kwargs={'q': q})

p, webq = b.run()
while True:
    print(webq.get())
