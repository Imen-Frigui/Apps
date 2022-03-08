package com.example.my_application;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

public class Main extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
    String ch_N,ch_P,ch_M,Phone;
    EditText prenom,nom,tel,mail;

    public void ajouter(View view) {
        prenom = findViewById(R.id.edPren);
        nom = findViewById(R.id.edNom);
        tel = findViewById(R.id.edPhone);
        mail = findViewById(R.id.edMail);
        ch_N=nom.getText().toString();
        ch_P=prenom.getText().toString();
        ch_M=mail.getText().toString();
        Phone=tel.getText().toString();
        Intent intent = new Intent(getApplicationContext(), Second.class);
        intent.putExtra("ch_N", String.valueOf(ch_N));
        intent.putExtra("ch_P", String.valueOf(ch_P));
        intent.putExtra("ch_M", String.valueOf(ch_M));
        intent.putExtra("Phone", String.valueOf(Phone));
        startActivity(intent);
    }

    public void annuler(View view) {
        prenom = findViewById(R.id.edPren);
        nom = findViewById(R.id.edNom);
        tel = findViewById(R.id.edPhone);
        mail = findViewById(R.id.edMail);
        prenom.setText("");
        nom.setText("");
        tel.setText("");
        mail.setText("");
    }
}