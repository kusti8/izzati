package com.kusti8.izzatitest;

import android.Manifest;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.database.Cursor;
import android.net.Uri;
import android.provider.MediaStore;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;

import com.kusti8.izzati.Izzati;
import com.kusti8.izzati.IzzatiJsonHandler;
import com.loopj.android.http.FileAsyncHttpResponseHandler;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.File;

import cz.msebera.android.httpclient.Header;

public class MainActivity extends AppCompatActivity {
    private int PICK_IMAGE_REQUEST = 1;
    private File file;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        checkPermission();
    }

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

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == PICK_IMAGE_REQUEST && resultCode == RESULT_OK && null != data) {
            Uri selectedImage = data.getData();
            String[] filePathColumn = { MediaStore.Images.Media.DATA };

            Cursor cursor = getContentResolver().query(selectedImage,
                    filePathColumn, null, null, null);
            cursor.moveToFirst();

            int columnIndex = cursor.getColumnIndex(filePathColumn[0]);
            String picturePath = cursor.getString(columnIndex);
            cursor.close();

            // String picturePath contains the path of selected Image
            Log.w("self", picturePath);
            file = new File(picturePath);
            Log.w("self", String.valueOf(file.exists()));
        }
    }

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
                    Log.w("self", response.toString()); // Print out the response
                }
            });
        } else {
            i.send(obj, file, new IzzatiJsonHandler() { // If there is a file, simply specify it after the JSON
                @Override
                public void callback(JSONObject response) {
                    Log.w("self", response.toString());
                }
            });
        }
    }

    public void chooseFile(View view) {
        Intent i = new Intent(Intent.ACTION_PICK, MediaStore.Images.Media.EXTERNAL_CONTENT_URI);
        startActivityForResult(i, PICK_IMAGE_REQUEST);
    }
}
