Samples
=============

Backend
-----------

.. code-block:: python

    from izzati import Backend, file_return

    def pr(form, files):
        print(form) # Print out the dictionary received
        for x in files:
            x.save('/tmp/test.jpg') # Save the file received
        return {'It': 'Worked'} # Return a dictionary to the frontend

    back = Backend(pr)
    back.run()

Frontend - Python
-------------------

.. code-block:: python

    from izzati import Frontend

    f = Frontend('http://localhost:5020/')
    out = f.send(js={'test': '123'}, f=open('/tmp/test.jpg', 'rb')) # Send a file and a dictionary
    print(out)

Frontend - Java
-------------------

.. code-block:: java

    public void sendMessage(View view) throws JSONException {
        EditText text = (EditText)findViewById(R.id.jsonTxt);
        String value = text.getText().toString(); // The JSON data is stored here
                                                  // The input parameter can be a JSONObject or a string
        Izzati i = new Izzati();                  // Initialize Izzati
        JSONObject obj = new JSONObject(value);
        i.url = "http://192.168.100.118:5020/";   // Set in Izzati, the URL
        if (file == null) {
            i.send(obj, new IzzatiJsonHandler() { // If there is no file selected, send JSON and expect JSON back
                @Override
                public void callback(JSONObject response) {
                    System.out.println(response); // Print out the response
                }
            });
        } else {
            i.send(obj, file, new IzzatiJsonHandler() { // If there is a file, simply specify it after the JSON
                @Override
                public void callback(JSONObject response) {
                    System.out.println(response);
                }
            });
        }
    }
