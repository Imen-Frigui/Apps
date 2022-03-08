package com.tp.imc;

import android.app.Activity;
import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.annotation.Nullable;
public class MainActivity extends Activity  {
    EditText Hieght, wieght;
    Button result, restart;
    TextView resultat,message;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        message = findViewById(R.id.tvAcc);
        Hieght = findViewById(R.id.Height);
        wieght = findViewById(R.id.edPoids);
        result = findViewById(R.id.btnCalculer);
        restart = findViewById(R.id.btnRetablir);
        resultat = findViewById(R.id.tvResult);
    }

    public void calculate(View v) {
        String staille;
        staille = Hieght.getText().toString();
        String spoids = wieght.getText().toString();
        float ftaille = Float.valueOf(staille);
        float fpoids = Float.valueOf(spoids);
        double res = fpoids / Math.pow(ftaille,2);
        resultat.setText("IMC = " +res);
        if (res < 18.5) {
            resultat.setText(resultat.getText().toString()+"\n"+"Insuffisance pondérale");
            resultat.setTextColor(Color.parseColor("#FFFF00"));
        }
        else if (res > 18.5 && res < 24.9) {
            resultat.setText(resultat.getText().toString()+"\n"+"Poids normal");
            resultat.setTextColor(Color.parseColor("#008000"));
        }
        else if (res > 25 && res < 29.9) {
            resultat.setText(resultat.getText().toString()+"\n"+"Surpoids");
            resultat.setTextColor(Color.parseColor("#FFA500"));
        }
        else if (res > 30){
            resultat.setText(resultat.getText().toString()+"\n"+"Obésité");
            resultat.setTextColor(Color.parseColor("#FF0000"));
        }
    }

    public void cancel(View v){
        Hieght.setText("");
        wieght.setText("");
        resultat.setText("@string/resultat");
    }
}