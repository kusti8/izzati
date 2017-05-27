Quickstart - Python
==========================

Install
------------
The frontend is included with the backend, so a simple
``sudo pip install izzati``
will work

Usage
------------
Usage is dead simple:

.. code-block:: python

    from izzati import Frontend

    f = Frontend('http://localhost:5020/') # Initialize the frontend with a url
    f.send(js={'test': '123'}, f=open('/tmp/test.jpg', 'rb')) # Send a dictionary and a file

A dictionary doesn't need to be sent:

.. code-block:: python

    from izzati import Frontend

    f = Frontend('http://localhost:5020/') # Initialize the frontend with a url
    f.send(f=open('/tmp/test.jpg', 'rb')) # Send a file

That's it!
