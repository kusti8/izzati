Quickstart - ESP8266
===========================

Install
-------------

Add the following to the top of your code:

.. code-block:: c

    #include <ESP8266HTTPClient.h>

    HTTPClient http;

And the following function:

.. code-block:: c

    String izzati(String url, String data) {
    http.begin(url);
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");
    http.POST(data);
    String str = http.getString();
    int locStart = str.indexOf("\"");
    if (locStart==-1) return "";
    locStart += String("\"").length();
    int locFinish = str.indexOf("\"", locStart);
    if (locFinish==-1) return "";
    return str.substring(locStart, locFinish);
    }

Usage
---------

``String out = izzati("http://192.168.100.113:5020/", "test=ing");`` sends a message that would look like ``{'test': 'ing'}``. **The output from the server must be a string.**