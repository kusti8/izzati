Quickstart - Other
==========================

Usage
------------
In whatever programming language you use, notice the following protocol:

All data is sent using parameters, in a JSON-like way. So for example,
a parameter with key "hi" and value "me", would exit the backend as {"hi": "me"}.

Data is sent as a parameter as well, *with key 'file'*.

Everything is a POST request to a URL. The sent message is either data, a file,
or both. The return is either data or a file.

That's it!
