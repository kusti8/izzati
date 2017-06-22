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

*Your changes may take a few minutes to update. For rapid debugging, it is best
to just start a quick bash shell: ``heroku run bash`` and experiment there.

Own Changes
-----------------

.. code-block:: bash

    heroku login
    heroku git:clone -a [name of deploy]
    cd [name of deploy]
    # Make whatever changes you need
    git add .
    git commit -m "Added changes"
    git push heroku master

*Be sure to change Procfile to reflect the name of your new script*
