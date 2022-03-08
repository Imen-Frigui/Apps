package com.example.bmiapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    private ImageView img;
    private static EditText tailles;
    private static EditText poids;
    private static TextView resultat;
    private static Button calcul;
    private static Button retab;
    String calculation, BMIresult;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        img=(ImageView)findViewById(R.id.image);
        tailles=(EditText)findViewById(R.id.TVtail);
        poids=(EditText) findViewById(R.id.Tv2poids);
        calcul=(Button)findViewById(R.id.calc);
        retab=(Button)findViewById(R.id.act);
        resultat=(TextView)findViewById(R.id.TVimc4);

    }
    public void calculateBMI(View view) {
        String S1 = tailles.getText().toString();
        String S2 = poids.getText().toString() ;



        float taillesValue = Float.parseFloat(S1)/100;
        float poidsValue = Float.parseFloat(S2) ;



        float bmi = poidsValue / (taillesValue * taillesValue);




        if(bmi < 18.5){
            BMIresult = "insuffisance pondérale";
            calculation = "votre BMI:" + bmi + "\n" + BMIresult;
            resultat.setText(calculation);
            resultat.setTextColor(Color.parseColor("#FFFF00"));


        }else if(bmi >= 18.5 && bmi <= 24.9){
            BMIresult = " poids Normal";
            calculation = "votre BMI:" + bmi + "\n" + BMIresult;
            resultat.setText(calculation);
            resultat.setTextColor(Color.parseColor("#008000"));


        }else if (bmi >= 25 && bmi <= 29.9){
            BMIresult = "surpoids";
            calculation = "votre BMI:" + bmi + "\n" + BMIresult;
            resultat.setText(calculation);
            resultat.setTextColor(Color.parseColor("#FFA500"));


        }else{
            BMIresult = "Obese";
            calculation = "votre BMI:" + bmi + "\n" + BMIresult;
            resultat.setText(calculation);
            resultat.setTextColor(Color.parseColor("#FF0000"));

        }



        //calculation = "votre BMI:" + bmi + "\n" + BMIresult;



        // res.setText(calculation);
    }
    public void Retablir(View view){
        resultat.setText("");
        tailles.setText("");
        poids.setText("");
    }
}