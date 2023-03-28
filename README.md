# PythonAPIs
#Main activity Kotlin Code
package com.example.myproject

    import androidx.appcompat.app.AppCompatActivity
    import android.os.Bundle
    import android.view.View
    import android.widget.ImageView
    import android.widget.ProgressBar
    import android.widget.TextView
    import android.widget.Toast
    import androidx.recyclerview.widget.LinearLayoutManager
    import androidx.recyclerview.widget.RecyclerView
    import androidx.recyclerview.widget.RecyclerView.LayoutManager
    import com.google.gson.GsonBuilder
    import com.loopj.android.http.AsyncHttpClient
    import com.loopj.android.http.JsonHttpResponseHandler
    import cz.msebera.android.httpclient.Header
    import org.json.JSONArray
    import org.json.JSONObject

    class MainActivity : AppCompatActivity() {
        lateinit var recyclerAdapter: RecyclerAdapter //call the RecyclerAdapter
        lateinit var progressbar:ProgressBar
        lateinit var recyclerView: RecyclerView
        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
            setContentView(R.layout.activity_main)
    //      consume the conference room details from the api
            recyclerView=findViewById(R.id.recycler)
            progressbar=findViewById(R.id.progressbar)

            val client =AsyncHttpClient(true,80,443)
            //pass the product list to the adapter
            recyclerAdapter= RecyclerAdapter(applicationContext)
            recyclerView.layoutManager=LinearLayoutManager(applicationContext)
            recyclerView.setHasFixedSize(true)
            client.get(this,
                "https://musau.pythonanywhere.com/getconference_room",
                null,"application/json",

                object : JsonHttpResponseHandler() {
                    override fun onSuccess(
                        statusCode: Int,
                        headers: Array<out Header>?,
                        response: JSONArray?
                    ) {
                       // super.onSuccess(statusCode, headers, response)
                        //we convert json array into a list of a given model
                        val gson=GsonBuilder().create()
                        val list=gson.fromJson(response.toString(),
                            Array<Conference_Room>::class.java).toList()
                        //now pass the conveeted list to adapter
                        recyclerAdapter.setProductItems(list)
                        progressbar.visibility=View.GONE
                    }
                    //onfailureon
                    override fun onFailure(
                        statusCode: Int,
                        headers: Array<out Header>?,
                        responseString: String?,
                        throwable: Throwable?
                    ) {
                        progressbar.visibility=View.GONE
                        Toast.makeText(applicationContext,
                            "No Conference available to display",Toast.LENGTH_LONG).show()
                    }
                }
            )
            //put the adapter into recycler view
            recyclerView.adapter=recyclerAdapter





        }
    }
# axtivity_main xml code
        <?xml version="1.0" encoding="utf-8"?>
        <LinearLayout
        xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        xmlns:tools="http://schemas.android.com/tools"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:orientation="vertical"
        android:background="#CFE4F5"
        tools:context=".MainActivity">
        <ProgressBar
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:id="@+id/progressbar"
            android:layout_marginLeft="10dp"/>
        <androidx.recyclerview.widget.RecyclerView
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:id="@+id/recycler"
            tools:listitem="@layout/single_item">

        </androidx.recyclerview.widget.RecyclerView>



        </LinearLayout>
        
 # add this code under holder.itemview after Context.MODE_PRIVATE)
    //save the product
            val editor: SharedPreferences.Editor = prefs.edit()
            editor.putString("room_id", item.room_id)
            editor.putString("room_name", item.room_name)
            editor.putString("room_desc", item.room_desc)
            editor.putString("num_of_persons", item.num_of_persons)
            editor.putString("availability", item.availability)
            editor.putString("cost", item.cost)
            editor.putString("image_url", item.image_url)
            editor.apply()

            //Navigate to SingleACtivity, Created Earlier
            val i = Intent(context, SingleActivity::class.java)
            i.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
            context.startActivity(i)
## paste the following code to activity_single.xml
    <?xml version="1.0" encoding="utf-8"?>
    <LinearLayout
        xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        xmlns:tools="http://schemas.android.com/tools"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:orientation="horizontal"
        tools:context=".SingleActivity">
        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:padding="10dp"
            android:orientation="vertical">

            <androidx.cardview.widget.CardView
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_weight="1"
                app:cardMaxElevation="12dp"
                app:cardUseCompatPadding="true"
                app:cardPreventCornerOverlap="true"
                android:layout_marginTop="0dp">
                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:orientation="vertical">

                    <ImageView
                        android:layout_width="300dp"
                        android:layout_height="140dp"
                        android:id="@+id/image_url"
                        android:src="@drawable/img"/>
                    <LinearLayout
                        android:layout_width="match_parent"
                        android:layout_height="wrap_content"
                        android:orientation="horizontal">
                        <TextView
                            android:layout_width="wrap_content"
                            android:layout_height="wrap_content"
                            android:text="Room_Id: "
                            android:layout_marginTop="5dp"
                            android:textSize="20dp"
                            android:textStyle="bold"/>
                        <TextView
                            android:layout_width="wrap_content"
                            android:layout_height="wrap_content"
                            android:text="ID"
                            android:textColor="#7B1FA2"
                            android:layout_marginTop="5dp"
                            android:id="@+id/room_id"
                            android:textSize="20dp"
                            android:textStyle="bold"/>

                        <TextView
                            android:layout_width="wrap_content"
                            android:layout_height="wrap_content"
                            android:layout_marginTop="5dp"
                            android:textAlignment="center"
                            android:textColor="#3C1AD3"
                            android:layout_marginStart="10dp"
                            android:textStyle="bold"
                            android:text="Name of the room"
                            android:textSize="20dp"
                            android:id="@+id/room_name"/>

                    </LinearLayout>
                    <TextView
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="Description"
                        android:textAlignment="center"
                        android:layout_marginTop="5dp"
                        android:textStyle="bold"
                        android:textSize="30dp"/>

                    <TextView
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="This is my description text"
                        android:layout_marginTop="5dp"
                        android:id="@+id/room_desc"
                        android:textStyle="italic"
                        android:textSize="20dp"/>
                    <LinearLayout
                        android:layout_width="match_parent"
                        android:layout_height="wrap_content"
                        android:layout_marginTop="5dp"
                        android:orientation="horizontal">
                        <TextView
                            android:layout_width="wrap_content"
                            android:layout_height="wrap_content"
                            android:text="Capacity: "
                            android:textColor="@color/purple_500"
                            android:layout_marginEnd="10dp"
                            android:textStyle="bold"
                            android:textSize="18dp"/>
                        <TextView
                            android:layout_width="wrap_content"
                            android:layout_height="wrap_content"
                            android:text="persons"
                            android:id="@+id/num_of_persons"
                            android:textColor="@color/purple_500"
                            android:layout_marginEnd="15dp"
                            android:textStyle="bold"
                            android:textSize="18dp"/>
                        <TextView
                            android:layout_width="wrap_content"
                            android:layout_height="wrap_content"
                            android:text="Status: "
                            android:textStyle="bold"
                            android:textSize="20dp"/>
                        <TextView
                            android:layout_width="wrap_content"
                            android:layout_height="wrap_content"
                            android:layout_marginEnd="10dp"
                            android:id="@+id/availability"
                            android:textColor="#27B32D"
                            android:text="available"
                            android:textStyle="bold"
                            android:textSize="18dp"/>

                    </LinearLayout>
                    <LinearLayout
                        android:layout_width="match_parent"
                        android:layout_height="wrap_content"
                        android:orientation="horizontal">
                        <TextView
                            android:layout_width="wrap_content"
                            android:layout_height="wrap_content"
                            android:text="Cost: "
                            android:textStyle="bold"
                            android:textSize="22dp"/>

                        <TextView
                            android:layout_width="wrap_content"
                            android:layout_height="wrap_content"
                            android:id="@+id/cost"
                            android:text="Ksh: 20,000"
                            android:textColor="#E64A19"
                            android:textStyle="bold"
                            android:textSize="20dp"/>

                    </LinearLayout>
                 </LinearLayout>
                </LinearLayout>
## copy and paste the following code inside SingleActivity.kt
    import android.content.Context
    import android.content.Intent
    import android.content.SharedPreferences
    import androidx.appcompat.app.AppCompatActivity
    import android.os.Bundle
    import android.view.View
    import android.widget.*
    import com.bumptech.glide.Glide
    import com.bumptech.glide.request.RequestOptions
    import com.loopj.android.http.AsyncHttpClient
    import com.loopj.android.http.JsonHttpResponseHandler
    import cz.msebera.android.httpclient.Header
    import cz.msebera.android.httpclient.entity.StringEntity
    import org.json.JSONObject

    class SingleActivity : AppCompatActivity() {
        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
            setContentView(R.layout.activity_single)

            //access shared prefferences
            val prefs: SharedPreferences = getSharedPreferences("store",
                Context.MODE_PRIVATE)

            //access the saved product_name from prefferences and put in the TextView
            val id = prefs.getString("room_id", "")
            val room_id = findViewById(R.id.room_id) as TextView
            room_id.text = id

            //access the saved product_desc from prefferences and put in the TextView
            val name = prefs.getString("room_name", "")
            val room_name = findViewById(R.id.room_name) as TextView
            room_name.text = name

            //access the saved product_cost from prefferences and put in the TextView
            val desc = prefs.getString("room_desc", "")
            val room_desc= findViewById(R.id.room_desc) as TextView
            room_desc.text = desc

            val persons = prefs.getString("num_of_persons", "")
            val num_persons= findViewById(R.id.num_of_persons) as TextView
            num_persons.text = persons

            val availability = prefs.getString("availability", "")
            val status= findViewById(R.id.availability) as TextView
            status.text = availability

            val cost = prefs.getString("cost", "")
            val room_cost= findViewById(R.id.cost) as TextView
            room_cost.text = cost

            //access the saved image from prefferences and put in the ImageView Using Glide
            val image_url = prefs.getString("image_url", "")
            val image = findViewById(R.id.image_url) as ImageView
            Glide.with(applicationContext).load(image_url)
                .apply(RequestOptions().centerCrop())
                .into(image)
            val view=findViewById<Button>(R.id.view_reservations)
            view.setOnClickListener {
                val i = Intent(applicationContext,Welcome::class.java)
                startActivity(i)
            }
          }
    }
## Mpesa integration API
    import requests
    import datetime
    import base64
    from requests.auth import HTTPBasicAuth
    @app.route('/mpesa_payment', methods = ['POST'])
    def mpesa_payment():
            #if request.method == 'POST':
                from flask import request
                json = request.json
                amount = json['amount']
                phone = json['phone']
                # GENERATING THE ACCESS TOKEN
                consumer_key = "GTWADFxIpUfDoNikNGqq1C3023evM6UH"
                consumer_secret = "amFbAoUByPV2rM5A"

                api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials" #AUTH URL
                r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

                data = r.json()
                access_token = "Bearer" + ' ' + data['access_token']

                #  GETTING THE PASSWORD
                timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
                passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
                business_short_code = "174379"
                data = business_short_code + passkey + timestamp
                encoded = base64.b64encode(data.encode())
                password = encoded.decode('utf-8')


                # BODY OR PAYLOAD
                payload = {
                    "BusinessShortCode": "174379",
                    "Password": "{}".format(password),
                    "Timestamp": "{}".format(timestamp),
                    "TransactionType": "CustomerPayBillOnline",
                    "Amount": amount,  # use 1 when testing
                    "PartyA": phone,  # change to your number
                    "PartyB": "174379",
                    "PhoneNumber": phone,
                    "CallBackURL": "https://modcom.co.ke/job/confirmation.php",
                    "AccountReference": "account",
                    "TransactionDesc": "account"
                }

                # POPULAING THE HTTP HEADER
                headers = {
                    "Authorization": access_token,
                    "Content-Type": "application/json"
                }

                url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest" #C2B URL

                response = requests.post(url, json=payload, headers=headers)
                print (response.text)
                response = jsonify({"sucess":"Paid {} - {}".format(phone, amount)})
                response.status_code = 200
                return response
 ## Mpesa integration kotlin code
     //mpesa integration
            val amount=findViewById<EditText>(R.id.amount)
            val phone=findViewById<EditText>(R.id.phone)
            amount.visibility=View.GONE
            progressbar.visibility=View.GONE
            book.setOnClickListener {
                amount.visibility=View.VISIBLE
                progressbar.visibility=View.VISIBLE
                val client = AsyncHttpClient(true,80,443)
                val body= JSONObject()
    //
                body.put("amount",amount.text.toString())
                body.put("phone",phone.text.toString())
                val con_body= StringEntity(body.toString())
                client.post(this,"https://musau.pythonanywhere.com/mpesa_payment",con_body,
                    "application/json",

                    object : JsonHttpResponseHandler() {

                        override fun onSuccess(
                            statusCode: Int,
                            headers: Array<out Header>?,
                            response: JSONObject?
                        ) {
                            println("printing after accessing onsuccess")
                            if (statusCode ==200){
                                Toast.makeText(applicationContext,"Please Confirm booking through mpesa pin",
                                    Toast.LENGTH_LONG).show()
                            }
                            else{
                                Toast.makeText(applicationContext,"Mpesa payment not successful $statusCode",
                                    Toast.LENGTH_LONG).show()
                            }
                            //super.onSuccess(statusCode, headers, response)
                        }

                        override fun onFailure(
                            statusCode: Int,
                            headers: Array<out Header>?,
                            throwable: Throwable?,
                            errorResponse: JSONObject?
                        ) {
                            println("on failure")
                            Toast.makeText(applicationContext,"Something Went wrong $statusCode", Toast.LENGTH_LONG).show()
                        }

                    }
                )
            }
