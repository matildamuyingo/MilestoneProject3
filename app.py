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


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check for a username match
        existing_username = mongo.db.users.find_one(
            {'username': request.form.get('username').lower()})
        
        # Check for an email match
        existing_email = mongo.db.users.find_one(
            {'email': request.form.get('email').lower()})

        # If the username exists, display warning
        if existing_username:
            flash('Username already taken')
            return redirect(url_for('register'))

        # If the email exists, display warning
        if existing_email:
            flash('Email already taken')
            return redirect(url_for('register'))

        # The user information from the form that is going to be added
        register_user = {
            'first_name': request.form.get('first_name').lower(),
            'last_name': request.form.get('last_name').lower(),
            'username': request.form.get('username').lower(),
            'email': request.form.get('email'),
            'password': generate_password_hash(request.form.get('password'))
        }
        # Insert the form information to the database
        mongo.db.users.insert_one(register_user)

        # Save the username as session user
        session['user'] = request.form.get('username').lower()
        flash('Registration Successful!')
        return redirect(url_for('profile', username=session['user']))
    return render_template('register.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if the username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Check if password matches username
            if check_password_hash(
                existing_user['password'], request.form.get('password')):
                    session['user'] = request.form.get('username').lower()
                    flash('Welcome, {}'.format(request.form.get('username')))
                    return redirect(url_for(
                        'profile', username=session['user']))
            else:
                # password and username does not match
                flash("Wrong password or username")
                return redirect(url_for('login'))
        else: 
            # the username does not exist
            flash('Wrong password or username')
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route("/profile", methods=["GET", "POST"])
def profile():
    return render_template('profile.html')


@app.route('/logout')
def logout():
    # remove the user from session cookies
    flash("You have been logged out")
    session.pop('user')
    return redirect(url_for('login'))

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
