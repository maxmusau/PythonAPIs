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
