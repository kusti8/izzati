package com.kusti8.izzati;

import com.loopj.android.http.*;

import org.json.JSONObject;

import java.io.File;
import java.io.FileNotFoundException;

/**
 * Created by kusti8 on 5/27/17.
 */

public class Izzati {
    public String url = "http://example.com:5020";

    private AsyncHttpClient client = new AsyncHttpClient();

    public void send(JSONObject param, AsyncHttpResponseHandler responseHandler) {
        RequestParams params = new RequestParams();
        params.put("json", param.toString());
        client.post(url, params, responseHandler);
    }

    public void send(String param, AsyncHttpResponseHandler responseHandler) {
        RequestParams params = new RequestParams();
        params.put("json", param);
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

    public void send(JSONObject param, File file, AsyncHttpResponseHandler responseHandler) {
        RequestParams params = new RequestParams();
        params.put("json", param.toString());
        try {
            params.put("file", file);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        client.post(url, params, responseHandler);
    }

    public void send(String param, File file, AsyncHttpResponseHandler responseHandler) {
        RequestParams params = new RequestParams();
        params.put("json", param);
        try {
            params.put("file", file);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        client.post(url, params, responseHandler);
    }
}
