package com.kusti8.izzati;

import com.loopj.android.http.*;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Iterator;

/**
 * Created by kusti8 on 5/27/17.
 */

public class Izzati {
    public String url = "http://example.com:5020";

    private AsyncHttpClient client = new AsyncHttpClient();

    public void send(JSONObject param, AsyncHttpResponseHandler responseHandler) throws JSONException {
        RequestParams params = new RequestParams();
        Iterator<?> keys = param.keys();
        while( keys.hasNext() ) {
          String key = (String)keys.next();
          params.put(key, param.get(key));
        }
        client.post(url, params, responseHandler);
    }

    public void send(File file, AsyncHttpResponseHandler responseHandler) {
        RequestParams params = new RequestParams();
        params.setHttpEntityIsRepeatable(true);
        try {
            params.put("file", file);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        client.post(url, params, responseHandler);
    }

    public void send(JSONObject param, File file, AsyncHttpResponseHandler responseHandler) throws JSONException {
        RequestParams params = new RequestParams();
        Iterator<?> keys = param.keys();
        while( keys.hasNext() ) {
          String key = (String)keys.next();
          params.put(key, param.get(key));
        }
        try {
            params.put("file", file);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        client.post(url, params, responseHandler);
    }
}
