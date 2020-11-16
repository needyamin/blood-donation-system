from flask import Flask, render_template, request, session, redirect
from datetime import datetime 
from datetime import timedelta 
import sqlite3 

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.permanent_session_lifetime = timedelta(minutes=5)

con = sqlite3.connect("needyamin.db")  
#print("Database opened successfully")  
#con.execute("create table Employees (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, address TEXT NOT NULL)")  
#print("Table created successfully")  
  
#index start# 
@app.route("/")  
def index():  
    return render_template("index.html"); 
#index end#

#index start# 
@app.route("/contact_us")  
def contact():  
    return render_template("contact_us.html"); 
#index end#


#dcma start# 
@app.route("/dcma")  
def dcma():  
    return render_template("dcma.html"); 
#dcma end#

#dcma start# 
@app.route("/profile")  
def profile():  
    return render_template("profile.html"); 
#dcma end#


#success start# 
@app.route("/success")  
def success():  
    return render_template("success.html"); 
#dcma end#


##start login request POST##
@app.route('/login',methods = ["POST"])
def login_post():
    session.permanent = True
    username = request.form["username"]
    password = request.form["password"]
    session["user"] = username
    username = session["user"]
    con = sqlite3.connect("needyamin.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()
    cur.execute("select * from admin where username= ? AND password = ?;",[username,password]) 
    user = cur.fetchall()
    msg = "username or password not match"
    if len(user)>0:
        return redirect('dashboard')

    return render_template("login.html",msg = msg)
##end login request POST##



##redirect dashboard start##
@app.route('/dashboard',methods=['GET'])
def dashboard():
 if request.method == "GET":
     with sqlite3.connect("needyamin.db") as con:
         try:
             con.row_factory = sqlite3.Row  
             cur = con.cursor()
             m = con.cursor()
             cur.execute("SELECT * from admin limit 1") #Admin last login
             rows = cur.fetchall()
             m.execute("SELECT COUNT(*) FROM users where gender='Male'") #Total Male
             male = m.fetchall()
             m.execute("SELECT COUNT(*) FROM users where gender='Female'") #Total Female
             female = m.fetchall()
             m.execute("SELECT COUNT(*) FROM users") #Total Users
             total = m.fetchall()
             m.execute("SELECT COUNT(*) FROM users where status='0'") #Pending Users
             pending = m.fetchall() 
             m.execute("SELECT COUNT(*) FROM contact_us") #Contact
             contact = m.fetchall() 
             m.execute("SELECT COUNT(*) FROM request") #Request 
             requestx = m.fetchall() 
             session["user"]
             username = session["user"]
             session["user"] = username
             username = session["user"]
             ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
             if len(username)>0:
                 return render_template('dashboard.html',username = username, ip = ip, total = total, male = male,female = female, pending = pending, contact = contact, requestx = requestx, rows = rows)
         except:
                     return render_template('login.html')
##redirect dashboard end##


###########Login check GET start####################
@app.route('/login',methods=['GET'])
def loginxx():
 if request.method == "GET":
     with sqlite3.connect("needyamin.db") as con:
         try:
             model.save() #hideValueError
             con.row_factory = sqlite3.Row  
             cur = con.cursor()
             cur.execute("select * from admin")
             cur.execute("select * from users")
             rows = cur.fetchall() 
             session["user"]
             username = session["user"]
             session["user"] = username
             username = session["user"]
             ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
             if len(username)>0:
                 return render_template('dashboard.html',username = username, ip = ip, rows = rows)
         except:
                     return render_template('login.html')
###################Login check GET end###################


##auth start##
@app.route('/mem',methods=['GET', 'POST'])
def mem():
 if request.method == "GET":   
    try:
        session["user"]
        username = session["user"]
        if len(username)>0:
            return render_template('dashboard.html')
    except:
        return redirect("login")
##auth end##



###logout###
@app.route('/logout')
def logout():
    session.clear()
    return redirect('login')
    
###logout###

##loop donar table start# 
@app.route("/doner")  
def doner():  
    con = sqlite3.connect("needyamin.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from users where status='1'")  
    rows = cur.fetchall()  
    return render_template("doner.html",rows = rows)   
##loop donar table end# 

 
##auth all users start##
@app.route('/all',methods=['GET', 'POST'])
def all_users():
 if request.method == "GET":
    with sqlite3.connect("needyamin.db") as con:
        try:  
            con.row_factory = sqlite3.Row  
            cur = con.cursor()  
            cur.execute("select * from users")  
            rows = cur.fetchall()         
            session["user"]
            username = session["user"]
            if len(username)>0:
                return render_template("all.html",rows = rows)
        except:
                    return redirect("login")
##auth all users end##



##auth pending start##
@app.route('/pending',methods=['GET', 'POST'])
def pending():
 if request.method == "GET":
    with sqlite3.connect("needyamin.db") as con:
        try:  
            con.row_factory = sqlite3.Row  
            cur = con.cursor()  
            cur.execute("select * from users where status='0'")  
            rows = cur.fetchall()         
            session["user"]
            username = session["user"]
            if len(username)>0:
                return render_template("pending.html",rows = rows)
        except:
                    return redirect("login")
##auth pending end##

#auth contact start#
@app.route('/contact_users',methods=['GET', 'POST'])
def contact_users():
 if request.method == "GET":
    with sqlite3.connect("needyamin.db") as con:
        try:  
            con.row_factory = sqlite3.Row  
            cur = con.cursor()  
            cur.execute("select * from contact_us")  
            rows = cur.fetchall()         
            session["user"]
            username = session["user"]
            if len(username)>0:
                return render_template("contact_users.html",rows = rows)
        except:
                    return redirect("login")
#auth contact end##


###contacts del end
@app.route("/contact_del", methods=["POST"])  
def contact_delete():    
    id = request.form["id"]  
    with sqlite3.connect("needyamin.db") as con:  
        try:
            con.row_factory = sqlite3.Row  
            cur = con.cursor()  
            cur.execute("select * from contact_us")  
            rows = cur.fetchall()  
            cur.execute("delete from contact_us where id = ?",(id,))
            con.commit()  
            msg = "record successfully deleted" 
        except:  
            msg = "can't be deleted" 
        finally:  
            return render_template("request.html",msg = msg, rows = rows) 
            ### contacts del request end



#auth request start#
@app.route('/request',methods=['GET', 'POST'])
def request_users():
 if request.method == "GET":
    with sqlite3.connect("needyamin.db") as con:
        try:  
            con.row_factory = sqlite3.Row  
            cur = con.cursor()  
            cur.execute("select * from request inner join users ON request.request_id = users.id")  
            rows = cur.fetchall()         
            session["user"]
            username = session["user"]
            if len(username)>0:
                return render_template("request.html",rows = rows)
        except:
                    return redirect("login")
#auth request end##

###blood request end
@app.route("/request_del", methods=["POST"])  
def request_delete():    
    id = request.form["id"]  
    with sqlite3.connect("needyamin.db") as con:  
        try:
            con.row_factory = sqlite3.Row  
            cur = con.cursor()  
            cur.execute("select * from request inner join users ON request.request_id = users.id")  
            rows = cur.fetchall()  
            cur.execute("delete from request where rid = ?",(id,))
            con.commit()  
            msg = "record successfully deleted" 
        except:  
            msg = "can't be deleted" 
        finally:  
            return render_template("request.html",msg = msg, rows = rows) 
            ### blood request end


##blood request contact start##
@app.route("/requests",methods = ["POST","GET"])  
def blood_request():  
    msg = ""
    id = request.form["id"] 
    if request.method == "POST":  
        try: 
            name = request.form["name"]
            email = request.form["email"]
            phone = request.form["phone"]
            hospital = request.form["hospital"]
            message = request.form["message"]  
            today = datetime.utcnow() 
            date = today.strftime('%Y-%m-%d')
            ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  
            with sqlite3.connect("needyamin.db") as con:
                cur = con.cursor()
            cur.execute("INSERT into request (request_id, r_name, r_email, r_phone, hospital, message, rip, rdate) values (?,?,?,?,?,?,?,?)",(id,name,email,phone,hospital,message,ip,date))  
            con.commit()
            msg = "Thank you! Your request has been submitted.."

        except:
            con.rollback()
            msg = "We can not add your blood group request to the list"
            
        finally:  
            return render_template("success.html",msg = msg)  
            con.close()   
    ##blood request contact end###


@app.route("/pending_del", methods=["POST"])  
def pending_delete():    
    id = request.form["id"]  
    with sqlite3.connect("needyamin.db") as con:  
        try:
            con.row_factory = sqlite3.Row  
            cur = con.cursor()  
            cur.execute("select * from users where status='1'")  
            rows = cur.fetchall()  
            cur.execute("delete from users where id = ?",(id,))
            con.commit()  
            msg = "record successfully deleted" 
        except:  
            msg = "can't be deleted" 
        finally:  
            return render_template("pending.html",msg = msg, rows = rows) 

##loop donar table pending end# 


##update conditions start
@app.route("/update", methods=["GET"])  
def update_router(): 
    return render_template("pending.html")      

@app.route("/update", methods=["POST"])  
def update_users():    
    id = request.form["id"]  
    with sqlite3.connect("needyamin.db") as con:  
        try:
            con.row_factory = sqlite3.Row  
            cur = con.cursor()
            cur.execute("select * from users where status='0'")  
            rows = cur.fetchall()  
            cur.execute("update users set status='1' where id = ?",(id,))
            con.commit()  
            msg = "record successfully updated" 
        except:  
            msg = "can't be update" 
        finally:  
            return render_template("pending.html",msg = msg,rows = rows) 
            #update condition end





##store blood donar information start##
@app.route("/blood_database",methods = ["POST","GET"])  
def blood_g():  
    msg = "" 
    if request.method == "POST":  
        try: 
            name = request.form["name"]  
            email = request.form["email"]  
            number = request.form["number"]
            blood_group = request.form["blood_group"]
            age = request.form["age"]
            donar_type = request.form["donar_type"]
            gender = request.form["gender"]
            street = request.form["street"]
            area = request.form["area"]  
            city = request.form["city"]  
            district = request.form["district"]  
            today = datetime.utcnow() 
            date = today.strftime('%Y-%m-%d')
            ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
            status = 0  
            with sqlite3.connect("needyamin.db") as con:
                cur = con.cursor()
            cur.execute("INSERT into users (name, email, number, blood_group, age, donar_type, gender, street, area, city, district, date, ip, status) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(name,email,number,blood_group,age,donar_type,gender,street,area,city,district,date,ip,status))  
            con.commit()
            msg = "Thank you! Your information has been submitted.."

        except:
            con.rollback()
            msg = "We can not add your blood group request to the list"
            
        finally:  
            return render_template("success.html",msg = msg)  
            con.close()   
    ##store blood donar information end###



##Contact Us start##
@app.route("/contact_us",methods = ["POST","GET"])  
def contact_form():  
    msg = "msg" 
    if request.method == "POST":  
        try: 
            name = request.form["name"]
            email = request.form["email"]
            phone = request.form["phone"]
            blood_group = request.form["blood_group"]
            message = request.form["message"]  
            today = datetime.utcnow() 
            date = today.strftime('%Y-%m-%d')
            ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  
            with sqlite3.connect("needyamin.db") as con:
                cur = con.cursor()
            cur.execute("INSERT into contact_us (name, email, phone, blood_group, message, ip, date) values (?,?,?,?,?,?,?)",(name,email,phone,blood_group,message,ip,date))  
            con.commit()
            msg = "Thank you! Your request has been submitted.."

        except:
            con.rollback()
            msg = "We can not add the your blood group to the list"
            
        finally:  
            return render_template("success.html",msg = msg)  
            con.close()   
    ##Contact Us end###


##user router start##
@app.route('/user/<int:user_id>')
def show_post(user_id):
    with sqlite3.connect("needyamin.db") as con:  
        try:
            con.row_factory = sqlite3.Row  
            cur = con.cursor()   
            cur.execute("select * from users where id= ?",(user_id,))
            rows = cur.fetchall()  
            msg = "success" 
        except:  
            msg = "wrong method" 
        finally:
         return render_template("profile.html", rows = rows);
##user router end##


 ##debugger command###   
if __name__ == "__main__":
    #export FLASK_ENV=development
    #source venv/bin/activate
    app.run(debug=True)