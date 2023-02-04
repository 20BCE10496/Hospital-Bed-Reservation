# from flask import Flask, render_template, redirect, request
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import UserMixin
# from werkzeug.security import generate_password_hash,check_password_hash

# from flask_login import login_required, logout_user, login_user, login_manager,LoginManager, current_user   
# import json
# import pymysql
# pymysql.install_as_MySQLdb


# app = Flask(__name__)

# # database connection
# local_server=True
# app.secret_Key="amishagoyal"

# # this is for getting a unique access to user.
# login_manager=LoginManager(app)
# login_manager.login_view='login'

# app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://root:@localhost/covid'
# db = SQLAlchemy(app)

# @login_manager.user_loader
# def load_user(user_uid):
#     return User.query.get(int(user_uid)) 

# class Test(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     name= db.Column(db.String(50))
    

# class User(UserMixin,db.Model):
#     uid=db.Column(db.Integer,primary_key=True)
#     srfid=db.Column(db.String(20),unique=True)
#     email=db.Column(db.String(50))   
#     dob=db.Column(db.String(1000)) 
    
    

# @app.route('/')
# def home():
#     return render_template("index.html")

# @app.route('/usersignup')
# def usersignup():
#     return render_template("usersignup.html")

# @app.route('/userlogin')
# def userlogin():
#     return render_template("userlogin.html")

# @app.route('/signup',methods=['POST','GET'])
# def signup():
#     if request.method=='POST':
#         srfid=request.form.get('srf')
#         dob=request.form.get('dob')
#         email=request.form.get('email')
#         # print(srfid,dob,email)
#         encpassword=generate_password_hash(dob)
#         new_user=db.engine.execute(f"INSERT INTO `user` (`srfid`,`email`,`dob`) VALUES ('{srfid}','{email}','{encpassword}') ")
#         return 'USER ADDED'

#     return render_template("/usersignup.html")

# @app.route('/login',methods=['POST','GET'])
# def login():
#     if request.method=="POST":
#         srfid=request.form.get('srf')
#         dob=request.form.get('dob')
#         user=User.query.filter_by(srfid=srfid).first()
#         if user and check_password_hash(user.dob,dob):
#             login_user(user)
#             return "Login success"
#             # return render_template("index.html")
#         else:
#             return "login fail"
#             # return render_template("userlogin.html")


#     return render_template("userlogin.html")



# # testing wheather database is connected or not
# @app.route('/test')
# def test():
#     try:
#         a=Test.query.all()
#         print(a)
#         return "My database is connected"
#     except Exception as e:
#         print(e)
#         return "My database is not connected"
        


# if __name__=="__main__":
#     app.run(debug=True)

from flask import Flask, json,redirect,render_template,flash,request
# from flask.globals import request, session
# from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

from flask_login import login_required,logout_user,login_user,login_manager,LoginManager,current_user
import json
import pymysql
pymysql.install_as_MySQLdb


# mydatabase connection
local_server=True
app=Flask(__name__)
app.secret_key="amishagoyal"





# this is for getting the unique user access
login_manager=LoginManager(app)
login_manager.login_view='login'

# app.config['SQLALCHEMY_DATABASE_URI']='mysql://username:password@localhost/databsename'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/covid'
db=SQLAlchemy(app)



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) 


class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))


class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    srfid=db.Column(db.String(20),unique=True)
    email=db.Column(db.String(50))
    dob=db.Column(db.String(1000))






@app.route("/")
def home():
    return render_template("index.html")

@app.route('/usersignup')
def usersignup():
    return render_template("usersignup.html")

@app.route('/userlogin')
def userlogin():
    return render_template("userlogin.html")



@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method=="POST":
        srfid=request.form.get('srf')
        email=request.form.get('email')
        dob=request.form.get('dob')
        # print(srfid,email,dob)
        encpassword=generate_password_hash(dob)
        new_user=db.engine.execute(f"INSERT INTO `user` (`srfid`,`email`,`dob`) VALUES ('{srfid}','{email}','{encpassword}') ")
        return "USER added"

    return render_template("usersignup.html")


@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=="POST":
        srfid=request.form.get('srf')
        dob=request.form.get('dob')
        user=User.query.filter_by(srfid=srfid).first()
        if user and check_password_hash(user.dob,dob):
            login_user(user)
            flash("Login successful","info")
            return render_template("index.html")
        else:
            flash("Invalid credentails","danger")
            return render_template("userlogin.html")          
        


    return render_template("userlogin.html")

# @app.route('/hospitallogin',methods=['POST','GET'])
# def hospitallogin():
#     if request.method=="POST":
#         email=request.form.get('email')
#         password=request.form.get('password')
#         user=Hospitaluser.query.filter_by(email=email).first()
#         if user and check_password_hash(user.password,password):
#             login_user(user)
#             flash("Login Success","info")
#             return render_template("index.html")
#         else:
#             flash("Invalid Credentials","danger")
#             return render_template("hospitallogin.html")


#     return render_template("hospitallogin.html")

# @app.route('/admin',methods=['POST','GET'])
# def admin():
 
#     if request.method=="POST":
#         username=request.form.get('username')
#         password=request.form.get('password')
#         if(username=="admin" and password=="admin"):
#             session['user']=username
#             flash("login success","info")
#             return render_template("addHosUser.html")
#         else:
#             flash("Invalid Credentials","danger")

#     return render_template("admin.html")

# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     flash("Logout SuccessFul","warning")
#     return redirect(url_for('login'))



# @app.route('/addHospitalUser',methods=['POST','GET'])
# def hospitalUser():
   
#     if('user' in session and session['user']=="admin"):
      
#         if request.method=="POST":
#             hcode=request.form.get('hcode')
#             email=request.form.get('email')
#             password=request.form.get('password')        
#             encpassword=generate_password_hash(password)  
#             hcode=hcode.upper()      
#             emailUser=Hospitaluser.query.filter_by(email=email).first()
#             if  emailUser:
#                 flash("Email or srif is already taken","warning")
         
#             db.engine.execute(f"INSERT INTO `hospitaluser` (`hcode`,`email`,`password`) VALUES ('{hcode}','{email}','{encpassword}') ")

#             # my mail starts from here if you not need to send mail comment the below line
           
#             # mail.send_message('COVID CARE CENTER',sender=params['gmail-user'],recipients=[email],body=f"Welcome thanks for choosing us\nYour Login Credentials Are:\n Email Address: {email}\nPassword: {password}\n\nHospital Code {hcode}\n\n Do not share your password\n\n\nThank You..." )

#             flash("Data Sent and Inserted Successfully","warning")
#             return render_template("addHosUser.html")

#     else:
#         flash("Login and try Again","warning")
#         return render_template("addHosUser.html")
    


# testing wheather db is connected or not  
@app.route("/test")
def test():
    try:
        a=Test.query.all()
        print(a)
        return f'MY DATABASE IS CONNECTED'
    except Exception as e:
        print(e)
        return f'MY DATABASE IS NOT CONNECTED {e}'





if __name__=="__main__":
    app.run(debug=True)