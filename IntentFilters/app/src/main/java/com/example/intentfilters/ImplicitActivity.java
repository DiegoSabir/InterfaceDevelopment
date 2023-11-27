package com.example.intentfilters;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.webkit.WebView;

public class ImplicitActivity extends AppCompatActivity {
    private WebView webView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_implicit);

        webView=findViewById(R.id.webviewImplicita);
        Intent intent = getIntent();
        Uri uriRecibida = intent.getData();
        webView.loadUrl(uriRecibida.toString());
    }
}