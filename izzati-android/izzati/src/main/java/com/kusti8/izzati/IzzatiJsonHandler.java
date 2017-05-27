package com.kusti8.izzati;

import com.loopj.android.http.JsonHttpResponseHandler;

import org.json.JSONArray;
import org.json.JSONObject;

import cz.msebera.android.httpclient.Header;

/**
 * Created by kusti8 on 5/27/17.
 */

public class IzzatiJsonHandler extends JsonHttpResponseHandler {
    @Override
    public void onSuccess(int statusCode, Header[] headers, JSONObject response) {
        callback(response);
    }
    public void callback(JSONObject response) {
        System.out.println(response);
    }
    @Override
    public void onFailure(int statusCode, Header[] headers, String errorResponse, Throwable e) {
        e.printStackTrace();
    }
}
