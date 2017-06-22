Heroku
==========================

Install
------------
Deploy the following:
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/kusti8/izzati)

Usage
------------
Create a file on a publically hosted place, with a single function, called "callback".
Like the backend quickstart, it takes all the same arguments and operates
the same way. It *must be called "callback"*. Specify the URL in the heroku
deploy, and you're all set.

Everytime a new call is made, the script will check for changes, and if there are,
will run the latest code available to download.
