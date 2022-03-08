package com.tp.concat;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    EditText ch_1,ch_2;
    TextView resultat;
    CheckBox chek;
    Button button;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        ch_1 = findViewById(R.id.ch1);
        ch_2 = findViewById(R.id.ch2);
        chek= findViewById(R.id.tvch3);
        button = findViewById(R.id.Butt);
        resultat= findViewById(R.id.tvres);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String ch1val=ch_1.getText().toString();
                String ch2val=ch_2.getText().toString();
                if (chek.isChecked()){
                    resultat.setText(ch1val+" "+ch2val);
                }else{
                    resultat.setText(ch1val+ch2val); }
            }
        });
    }
}
