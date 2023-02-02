from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import json
import pymysql
pymysql.install_as_MySQLdb

app = Flask(__name__)

# database connection
local_server=True
app.secret_Key="amishagoyal"
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://root:@localhost/covid'
db = SQLAlchemy(app)

class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(50))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/usersignup')
def usersignup():
    return render_template("usersignup.html")

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