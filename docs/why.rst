Why?
=========

I created this because I was recently at a hackathon where we created an
app and a backend and had to send a picture to the backend and receive
some text as a response. We spent close to 9 hours of our 36 hours and we
still couldn't get it working. We were sleep deprived, there were so many
options and we just couldn't get it to work. So I made this, which is designed
to Just Work between a backend and a frontend where you can send send text or
a file with a few commands and removing all the need for extra research or
dealing with HTTP POST or GET etc.

Features
--------------

* Dead simple library that is intuitive to use
* Supports sending images back and forth and returns a simple file object on both sides
* Uses callbacks so no large while loop
* Deciphers all the messages into native dictionary objects
* Clear documentation so everything you need is in one place
