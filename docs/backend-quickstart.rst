Quickstart - Backend
====================

Installation
--------------

``sudo pip install izzati``

Usage
-----------
A simple example which prints out the data received and a list of the filenames
of all the files which were received.

.. code-block:: python

    from izzati import Backend, file_return

    def p(text, data):
        print(text, [x.filename for x in data])
        return {'status': 'yes'}
        # return file_return('file.txt')

    b = Backend(p)
    b.run() # The host and port can be set as well:
    # b.run(host='0.0.0.0', port=5030) # Default is 0.0.0.0 and 5020

The function must have arguments for text and data, even if no data is sent.

A file can also be returned with the file_return function.

Data
----------
The data supports many functions that are revealed:

``file.read()``
Read a file
``file.save(location)``
Save a file to a location
``file.filename``
The name of the file when it was transferred

Text
--------------
The text is all returned as a dictionary, with keys and values. During transit,
it is converted to JSON, but will always be exposed as a dictionary.

Background Processes
-----------------------
Izzati provides a nice frontend for background processes and supports running
the backend in the background or a function in the background. This is built
on top of multiprocessing and supports multiple CPU cores etc.

1. Make the webserver in the background.

.. code-block:: python

    from izzati import Backend

    def callback(q, text, data): # <---------------------------------
        print(text, [x.filename for x in data])
        return {'status': 'OK'}

    b = Backend(callback, background=True) # <-----------------------
    p, q = b.run() # <----------------------------------------
    # Block the Python process, or else everything quits

Notice there's two extra return values, p and q and the callback accepts an extra argument. This is a Queue object, where
you can communicate with the callback function. Use ``q.put("hello")`` to put
data into the queue and ``q.get()`` to get data out of the queue. p is the process,
which can be used to join (``p.join()``) or to kill etc.

See https://docs.python.org/3/library/multiprocessing.html for more details.

**The callback, in this case, must have q as the first argument, with no default
value.**

2. Make another process in the background.

.. code-block:: python

    from izzati import Backend, background # <-------------

    def callback(text, data, q):
        print(text, [x.filename for x in data])
        q.put(text['name'])
        return {'status': 'OK'}

    def background_process(q, greeting): # <---------------
        while True:
            name = q.get()
            print(greeting + ", " + name)

    p, q = background(background_process, args=("Hello",)) # <--------------
    # Also supports default arguments with kwargs:
    # p, q = background(background_process, kwargs={"greeting": "Hello"})

    b = Backend(callback, args=(q,)) # <-----------------------
    # Also supports default arguments with kwargs:
    # b = Backend(callback, kwargs={'q': q})

    b.run()

**These methods can be used at the same time as well, but something must be
blocking the Python code from finishing.**

Arguments
------------
The Backend object supports args and kwargs, as shown above. The background
process does as well. In both, the args and kwargs follow the essentials,
such as text, data, and q if running in the background.
