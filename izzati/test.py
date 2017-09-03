from . import Backend, Frontend
from time import sleep

def test_simple_return():
    def call(q, text, file):
        assert text == {'test': 'works'}
        return {'status': 'OK'}
    b = Backend(call, background=True)
    p, q = b.run()
    sleep(1)
    f = Frontend('http://localhost:5020/')
    assert {'status': 'OK'} == f.send({'test': 'works'})