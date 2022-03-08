package com.isima.im3bg2;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.annotation.Nullable;
//action sur le bouton (façon 2): ajouter ici implements View.OnClickListener
public class MainActivity extends Activity  {
//2: création des objets java de mêmes types que les composants XML
    EditText taille, poids;
    Button calculer, retablir;
    TextView resultat;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        //1: affecter le layout correspondant
        setContentView(R.layout.activity_main);
        //3: associer chaque objet java au composant correspondant
        taille = findViewById(R.id.etTaille);
        poids = findViewById(R.id.etPoids);
        calculer = findViewById(R.id.btnCalculer);
        retablir = findViewById(R.id.btnRetablir);
        resultat = findViewById(R.id.tvResult);
     /*   //2ème façon
        calculer.setOnClickListener(this);
        retablir.setOnClickListener(this); */
/*
        //action sur le bouton (façon 1)
        calculer.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //traitement du bouton
                //a: récupérer le poids et la taille
                String staille = taille.getText().toString();
                String spoids = poids.getText().toString();
                //b: convertir les valeurs récupérées vers float
                float ftaille = Float.valueOf(staille);
                float fpoids = Float.valueOf(spoids);
                //c: calculer IMC
                double res = fpoids / Math.pow(ftaille,2);
                resultat.setText("Votre IMC = " +res);
                }
        });


     retablir.setOnClickListener(new View.OnClickListener() {
         @Override
         public void onClick(View v) {
             taille.setText("");
             poids.setText("");
             resultat.setText("");
         }
     });
     */

    }

/* façon 2
    @Override
    public void onClick(View v) {
        if(v.getId() == R.id.btnCalculer)
        {
            //traitement du bouton
            //a: récupérer le poids et la taille
            String staille = taille.getText().toString();
            String spoids = poids.getText().toString();
            //b: convertir les valeurs récupérées vers float
            float ftaille = Float.valueOf(staille);
            float fpoids = Float.valueOf(spoids);
            //c: calculer IMC
            double res = fpoids / Math.pow(ftaille,2);
            resultat.setText("Votre IMC = " +res);

        }
        else
            if(v.getId()==R.id.btnRetablir){
                taille.setText("");
                poids.setText("");
                resultat.setText("");
            }
    }*/

    public void calculate(View v) {
        //traitement du bouton
        //a: récupérer le poids et la taille
        String staille = taille.getText().toString();
        String spoids = poids.getText().toString();
        //b: convertir les valeurs récupérées vers float
        float ftaille = Float.valueOf(staille);
        float fpoids = Float.valueOf(spoids);
        //c: calculer IMC
        double res = fpoids / Math.pow(ftaille,2);
        resultat.setText("Votre IMC = " +res);

    }

    public void cancel(View v){
        taille.setText("");
        poids.setText("");
        resultat.setText("Résultat");
    }
}