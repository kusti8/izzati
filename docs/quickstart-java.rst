Quickstart - Java
=====================

Install
----------------
Add the following to your project build.gradle

.. code-block:: java

    dependencies {
        compile 'com.github.kusti8:izzati:1.2.0'
    }

Usage
----------
The Java library is very easy to use as well

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

Return Types
------------------
If you want to receive a binary instead of a JSON, observe the following changes:

.. code-block:: java

    public void sendMessage(View view) throws JSONException {
        EditText text = (EditText)findViewById(R.id.jsonTxt);
        String value = text.getText().toString();
        Izzati i = new Izzati();
        JSONObject obj = new JSONObject(value);
        i.url = "http://192.168.100.118:5020/";
        if (file == null) {
            i.send(obj, new FileAsyncHttpResponseHandler(this) {
                @Override
                public void onFailure(int statusCode, Header[] headers, Throwable throwable, File file) {
                    throwable.printStackTrace();
                }

                @Override
                public void onSuccess(int statusCode, Header[] headers, File response) {
                    Log.w("self", response.toString());
                }
            });
        } else {
            i.send(obj, file, new FileAsyncHttpResponseHandler(this) {
                @Override
                public void onFailure(int statusCode, Header[] headers, Throwable throwable, File file) {
                    throwable.printStackTrace();
                }

                @Override
                public void onSuccess(int statusCode, Header[] headers, File response) {
                    Log.w("self", response.toString());
                }
            });
        }
    }

NB! Remember Permissions
----------------------------
Remember to set permissions in the manifest:

.. code-block:: xml

    <uses-permission android:name="android.permission.INTERNET"/>
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />

And to request permissions if you are accessing files:

.. code-block:: java

    private void checkPermission(){
        if (checkSelfPermission(Manifest.permission.READ_EXTERNAL_STORAGE)
                != PackageManager.PERMISSION_GRANTED) {

            // Should we show an explanation?
            if (shouldShowRequestPermissionRationale(
                    Manifest.permission.READ_EXTERNAL_STORAGE)) {
                // Explain to the user why we need to read the contacts
            }

            requestPermissions(new String[]{Manifest.permission.READ_EXTERNAL_STORAGE},
                    123);

            // MY_PERMISSIONS_REQUEST_READ_EXTERNAL_STORAGE is an
            // app-defined int constant that should be quite unique

            return;
        }
    }

And then call that function in the onCreate override.
