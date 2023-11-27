package com.example.intentfilters;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.webkit.WebView;

public class ExplicitActivity extends AppCompatActivity {

    private WebView webView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_explicit);
        webView=findViewById(R.id.webviewExplicita);
        Intent intent = getIntent();
        String urlRecibida = intent.getExtras().getString("url_key");
        webView.loadUrl(urlRecibida);
    }
}