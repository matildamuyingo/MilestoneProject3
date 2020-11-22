import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    return render_template('login.html')


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_username = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email")})

        if existing_username:
            flash("Username already taken")
            return redirect(url_for("register"))
        elif existing_email:
            flash("Email already taken")
            return redirect(url_for("register"))

        register_user = {
            'first_name': request.form.get('first_name').lower(),
            'last_name': request.form.get('last_name').lower(),
            'username': request.form.get('username').lower(),
            'email': request.form.get('email'),
            'password': generate_password_hash(request.form.get('password'))
        }
        mongo.db.users.inser_one(register_user)

        session['user'] = request.form.get('username').lower()
        flash('Registration Successful!')
        return redirect(url_for('profile', username=session['user']))
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
