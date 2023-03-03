#create a route
from flask import *
import pymysql
# create app
app=Flask(__name__)
# connection
con=pymysql.connect(host="Musau.mysql.pythonanywhere-services.com",user="Musau",password="maxwell1234",database="Musau$MyDatabase")
@app.route("/register", methods=['POST','GET'])
def signup():
    # json-file format
    json=request.json
    name=json['name']
    email=json['email']
    phone=json['phone']
    password=['password']
    confirm_password=['confirm_password']
#     validation checks
    if " " not in name:
        response=jsonify({"message":"Name must be two words"})
        response.status_code=401
        return response
    elif "@" not in email:
        response=jsonify({"message":"You must have @ in email address"})
        response.status_code = 402
        return response
    elif "254" not in phone:
        response=jsonify({"message":"Phone must start with 254"})
        response.status_code = 403
        return response
    elif len(phone) != 12:
        response=jsonify({"message":"Enter Valid Phone number"})
        response.status_code = 404
        return response
    elif password != confirm_password:
        response=jsonify({"message":"Password do not match confirm password"})
        response.status_code = 405
        return response
    else:
        con = pymysql.connect(host="Musau.mysql.pythonanywhere-services.com", user="Musau", password="maxwell1234",
                              database="Musau$MyDatabase")
        sql='insert into signup (name,email,phone,password,confirm_password) values(%s,%s,%s,%s,%s)'
        cursor=con.cursor()
        try:
            cursor.execute(sql,(name,email,phone,password,confirm_password))
            con.commit()
            response=jsonify({"message":"Signup successful"})
            response.status_code=200
            return response
        except:
            response=jsonify({"message":"Something went wrong from api side"})
            response.status_code=500


# signin api
@app.route("/signin",methods=['POST'])
def signin():
    try:

        json=request.json
        email=json['email']
        password=json['password']

        con = pymysql.connect(host="Musau.mysql.pythonanywhere-services.com", user="Musau", password="maxwell1234",
                              database="Musau$MyDatabase")

        cursor=con.cursor()
        sql='select * from signup where email= %s and password =%s'
        cursor.execute(sql,(email,password))
    #     check if there is user with credentials
        if cursor.rowcount == 0:
            response =jsonify({"message": "There is no user with above details"})
            response.status_code=406 #client error
            return response
        else:
            response=jsonify({"message":"Signin Successful"})
            response.status_code=201
            return response
    except:
        response=jsonify({"message":"Something went wrong from api side"})
        response.status_code=501
        return response
# route to fetch the conference rooms
@app.route("/getconference_room",methods=['GET'])
def conferenceroom():
    con = pymysql.connect(host="Musau.mysql.pythonanywhere-services.com", user="Musau", password="maxwell1234",
                          database="Musau$MyDatabase")
#     sql to be executed
    sql='select * from conference_room'
#     create cursor to execute the sql
    cursor=con.cursor()
    #execute the sql
    cursor.execute(sql)
    #check if there's any records to fetch
    if cursor.rowcount ==0:
        response=jsonify({"message":"No  products available"})
        response.status_code == 407
        return response
    else:
        rooms=cursor.fetchall()
        response=jsonify(rooms) #fetch the records in json format
        response.status_code==205

        return response


