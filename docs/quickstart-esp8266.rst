Quickstart - ESP8266
===========================

Install
-------------

Add the following to the top of your code:

.. code-block:: c

    #include <ESP8266HTTPClient.h>
    #include <ArduinoJson.h> // Only if working with JSON. Use https://bblanchon.github.io/ArduinoJson/assistant/ for size.

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

    JsonObject& izzatiJson(String url, String data) {
        const size_t MAX_CONTENT_SIZE = 512;
        const size_t BUFFER_SIZE = JSON_OBJECT_SIZE(2) + JSON_ARRAY_SIZE(2) + MAX_CONTENT_SIZE; // See: https://bblanchon.github.io/ArduinoJson/assistant/
        http.begin(url);
        http.addHeader("Content-Type", "application/x-www-form-urlencoded");
        http.POST(data);
        String str = http.getString();
        DynamicJsonBuffer jsonBuffer(BUFFER_SIZE);
        JsonObject& root = jsonBuffer.parseObject(str);
        return root;
    }

Usage
---------

For string: ``String out = izzati("http://192.168.100.113:5020/", "test=ing");`` sends a message that would look like ``{'test': 'ing'}``. **The output from the server must be a string.**

For JSON: 

.. code-block:: c

    JsonObject& ing = izzatiJson("http://192.168.100.113:5020/", "test=ing");
    String hello = ing["hello"];