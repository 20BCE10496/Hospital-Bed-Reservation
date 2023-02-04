from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

from flask_login import login_required, logout_user, login_user, login_manager,LoginManager, current_user   
import json
import pymysql
pymysql.install_as_MySQLdb


app = Flask(__name__)

# database connection
local_server=True
app.secret_Key="amishagoyal"

# this is for getting a unique access to user.
login_manager=LoginManager(app)
login_manager.login_view='login'

app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://root:@localhost/covid'
db = SQLAlchemy(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(50))
    

class user(db.Model):
    uid=db.Column(db.Integer,primary_key=True)
    srfid=db.Column(db.String(20),unique=True)
    email=db.column(db.String(20))   
    dob=db.column(db.String(20)) 
    
    

@app.route('/')
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
    if request.method=='POST':
        srfid=request.form.get('srf')
        dob=request.form.get('dob')
        email=request.form.get('email')
        # print(srfid,dob,email)
        encpassword=generate_password_hash(dob)
        new_user=db.engine.execute(f"INSERT INTO `user` (`srfid`,`email`,`dob`) VALUES ('{srfid}','{email}','{encpassword}') ")
        return 'USER ADDED'

    return render_template("/usersignup.html")

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=="POST":
        srfid=request.form.get('srf')
        dob=request.form.get('dob')
        user=User.query.filter_by(srfid=srfid).first()
        if user and check_password_hash(user.dob,dob):
            login_user(user)
            flash("Login Success","info")
            return render_template("index.html")
        else:
            flash("Invalid Credentials","danger")
            return render_template("userlogin.html")


    return render_template("userlogin.html")



# testing wheather database is connected or not
@app.route('/test')
def test():
    try:
        a=Test.query.all()
        print(a)
        return "My database is connected"
    except Exception as e:
        print(e)
        return "My database is not connected"
        


if __name__=="__main__":
    app.run(debug=True)