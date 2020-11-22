import os
import pymysql
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

connection = pymysql.connect(host='localhost',
                             user='root',
                             db='Mile')

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    return render_template('login.html')


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        new_user_reg = {
            'fName': request.form.get("first_name"),
            'lName': request.form.get("last_name"),
            'uName': request.form.get("username"),
            'email': request.form.get("email"),
            'password': generate_password_hash(request.form.get("password"))
        }

        try:
            with connection.cursor() as cursor:
                new_user = """INSERT INTO Users(first_name, last_name, username, email, password)
                            VALUES (%s, %s,%s, %s, %s,);""", new_user_reg
                cursor.execute(new_user)
                for row in cursor:
                    print(row)
        finally:
            connection.close()
    return render_template('register.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/startpage')
def startpage():
    return render_template('startpage.html')


@app.route('/add_book')
def add_book():
    return render_template('add_book.html')


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)
