package Project;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import com.isima.t2g2b.R;

public class SecondActivity extends AppCompatActivity {

    TextView tvpren,tvnom,tvtel,tvmail;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);
        Intent intent = getIntent();
        String Phone = intent.getStringExtra("Phone");
        String CH_N = intent.getStringExtra("ch_N");
        String CH_M = intent.getStringExtra("ch_M");
        String ch_P = intent.getStringExtra("ch_P");
        tvpren = findViewById(R.id.PREN);
        tvnom = findViewById(R.id.NOM);
        tvmail=findViewById(R.id.MAIL);
        tvtel=findViewById(R.id.PHONE);
        tvpren.setText(ch_P);
        tvnom.setText(CH_N);
        tvmail.setText(CH_M);
        tvtel.setText(Phone);
    }
    public void calling(View view) {
        Uri number = Uri.parse("tel:"+tvtel.getText().toString());
        Intent callIntent = new Intent(Intent.ACTION_DIAL, number);
        startActivity(callIntent);
    }
    public void mailing(View view) {
        Uri mail = Uri.parse("mailto:"+tvmail.getText().toString());
        Intent mailIntent = new Intent(Intent.ACTION_SENDTO, mail);
        startActivity(mailIntent);
    }
}