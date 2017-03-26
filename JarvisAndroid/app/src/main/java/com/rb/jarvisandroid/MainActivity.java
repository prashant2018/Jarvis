package com.rb.jarvisandroid;

import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.speech.RecognizerIntent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.DefaultItemAnimator;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.KeyEvent;
import android.view.View;
import android.view.inputmethod.EditorInfo;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.google.gson.JsonObject;
import com.koushikdutta.async.future.FutureCallback;
import com.koushikdutta.ion.Ion;

import org.json.JSONObject;

import java.net.URLEncoder;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class MainActivity extends AppCompatActivity {

    private String sender,message;
    private ChatAdapter cAdapter;
    private List<ChatModel> chatModelList = new ArrayList<>();
    private RecyclerView recyclerView;
    private EditText editText;
    private ChatModel chatModel;
    private final int REQ_CODE_SPEECH_INPUT = 100;
    public String url;
    public String url_ext;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        init();
    }
    public void init(){
        url = "http://192.168.43.242:8000/";
        url_ext = "home/?query=";
        sender="Prashant";
        recyclerView = (RecyclerView)findViewById(R.id.recycler_view);
        cAdapter = new ChatAdapter(chatModelList);
        editText = (EditText)findViewById(R.id.editText);

        RecyclerView.LayoutManager mLayoutManager = new LinearLayoutManager(getApplicationContext());
        recyclerView.setLayoutManager(mLayoutManager);
        recyclerView.setItemAnimator(new DefaultItemAnimator());
        recyclerView.setAdapter(cAdapter);


        editText.setOnEditorActionListener(new TextView.OnEditorActionListener() {
            @Override
            public boolean onEditorAction(TextView v, int actionId, KeyEvent event) {
                if (actionId == EditorInfo.IME_ACTION_SEND) {
                    getDataFromEditText();
                    return true;
                }
                return false;
            }
        });


    }
    public void send(View view){

        promptSpeechInput();
    }

    public void getDataFromEditText(){
        message = editText.getText().toString().trim();
        editText.setText("");
        recyclerRefresh(sender,message);
        fetchJsonData(message,url+url_ext);
        //emitMessage(message,sender);

    }

    //Refresh the recycler view with new data
    public void recyclerRefresh(String sender, String message){
        chatModel = new ChatModel(sender,message);
        chatModelList.add(chatModel);
        cAdapter.notifyDataSetChanged();
        recyclerView.scrollToPosition(cAdapter.getItemCount()-1);
    }


    private void promptSpeechInput() {

        Intent intent = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL,
                RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);
        intent.putExtra(RecognizerIntent.EXTRA_PREFER_OFFLINE,true);
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, Locale.getDefault());
        intent.putExtra(RecognizerIntent.EXTRA_PROMPT,
                getString(R.string.speech_prompt));
        try {
            startActivityForResult(intent, REQ_CODE_SPEECH_INPUT);
        } catch (ActivityNotFoundException a) {
            Toast.makeText(getApplicationContext(),
                    getString(R.string.speech_not_supported),
                    Toast.LENGTH_SHORT).show();
        }
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        Log.v("voice",resultCode+" ok"+requestCode);
        switch (requestCode) {
            case REQ_CODE_SPEECH_INPUT: {
                if (resultCode == RESULT_OK && null != data) {

                    ArrayList<String> result = data
                            .getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS);
                    String msg = result.get(0);
                    Log.v("debugg",msg+" ok");
                    recyclerRefresh(sender,msg);
                    fetchJsonData(msg,url+url_ext);
                }
                break;
            }

        }
    }



    void fetchJsonData(String message,String url1){
        try {
            message = URLEncoder.encode(message, "utf-8");
            Log.v("debugg","Message Encoded: "+message);
        }catch (Exception e){
            Log.v("debugg","error : "+e);
        }
        url1 = url1 + message;
        Ion.with(this)
                .load(url1)
                .asJsonObject()
                .setCallback(new FutureCallback<JsonObject>() {
                    @Override
                    public void onCompleted(Exception e, JsonObject result) {
                        if(e!=null){
                            recyclerRefresh("Jarvis","I think there is a network problem!");
                            url_ext = "home/?query=";
                        }
                        else if (result.get("status").getAsBoolean()) {
                            String msg = result.get("val").getAsString();
                            String url_ext1 = result.get("url").getAsString();
                            url_ext = url_ext1;
                            Log.v("debugg","url_ext : "+url_ext);
                            recyclerRefresh("Jarvis",msg);
                        }
                    }
                });
    }
}
