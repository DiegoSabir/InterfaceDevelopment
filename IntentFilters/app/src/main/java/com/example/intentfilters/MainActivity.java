package com.example.intentfilters;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    private EditText etUrl;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        etUrl=findViewById(R.id.etUrl);
    }

    public void onClickBtn(View view) {
        if (view.getId()==R.id.btnExplicito){
            if(!etUrl.getText().toString().isEmpty()){
                Intent intent = new Intent(this, ExplicitActivity.class);
                intent.putExtra("url_key", etUrl.getText().toString());
                startActivity(intent);
            }else{
                Toast.makeText(this, "Introduce una URL", Toast.LENGTH_SHORT).show();
            }
        }else if (view.getId()==R.id.btnImplicito){
            if(!etUrl.getText().toString().isEmpty()){
                Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(etUrl.getText().toString()));
                startActivity(intent);
            }else{
                Toast.makeText(this, "Introduce una URL", Toast.LENGTH_SHORT).show();
            }
        }
    }
}