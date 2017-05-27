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
    b.run()

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
