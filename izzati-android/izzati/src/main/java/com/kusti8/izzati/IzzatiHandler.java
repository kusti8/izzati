package com.kusti8.izzati;

import com.loopj.android.http.AsyncHttpResponseHandler;
import com.loopj.android.http.*;

import org.json.JSONArray;

import java.nio.charset.StandardCharsets;

import cz.msebera.android.httpclient.Header;

/**
 * Created by kusti8 on 5/27/17.
 */

public class IzzatiHandler extends AsyncHttpResponseHandler {
    @Override
    public void onSuccess(int statusCode, Header[] headers, byte[] response) {
        String str = new String(response, StandardCharsets.UTF_8);
        callback(str);
    }
    public void callback(String response) {
        System.out.println(response);
    }
    @Override
    public void onFailure(int statusCode, Header[] headers, byte[] errorResponse, Throwable e) {
        e.printStackTrace();
    }
}
