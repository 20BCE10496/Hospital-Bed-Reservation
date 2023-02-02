from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import MySQLdb

app = Flask(__name__)

# database connection
local_server=True
app.secret_Key="amishagoyal"
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://root:@localhost/covid'
db = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template("index.html")

# testing wheather database is connected or not
@app.route('/test')
def test():
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)