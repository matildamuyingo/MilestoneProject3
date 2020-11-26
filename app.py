import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Route for homepage - Only displayed when logged out
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
        datetime_now = datetime.now()

        register_user = {
            'first_name': request.form.get('first_name').lower(),
            'last_name': request.form.get('last_name').lower(),
            'username': request.form.get('username').lower(),
            'email': request.form.get('email'),
            'password': generate_password_hash(request.form.get('password')),
            'date_joined': datetime_now,
            'user_icon': request.form.get('user_icon'),
            'user_age': "",
            'user_gender': "",
            'fav_book': "",
            'fav_author': "",
            'fav_genre': ""
        }

        # Insert the form information to the database
        mongo.db.users.insert_one(register_user)

        # Save the username as session user
        session['user'] = request.form.get('username').lower()
        flash('Registration Successful!')
        return redirect(url_for('profile', username=session['user']))
    icons = mongo.db.icons.find()
    return render_template('register.html', icons=icons)


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


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Gets a list with all books added to the database
    books = list(mongo.db.books.find())
    user = mongo.db.users.find_one(
        {'username': username})

    if session['user'] == user['username']:
        return render_template(
            'profile.html', username=user, books=books)
    else:
        return render_template(
            'profile.html', username=user, books=books)

    return redirect(url_for('login'))


@app.route('/edit_profile/<username>', methods=["GET", "POST"])
def edit_profile(username):
    books = list(mongo.db.books.find())
    genres = list(mongo.db.genres.find())
    authors = list(mongo.db.authors.find())
    genders = list(mongo.db.genders.find())
    icons = list(mongo.db.icons.find())
    user = mongo.db.users.find_one(
        {'username': username})

    if request.method == "POST":

        u_name = user['username']
        email = user['email']
        password = user['password']
        joined = user['date_joined']

        update_info = {
            'first_name': request.form.get('first_name').capitalize(),
            'last_name': request.form.get('last_name').capitalize(),
            'username': u_name,
            'email': email,
            'password': password,
            'date_joined': joined,
            'user_icon': request.form.get('user_icon'),
            'user_age': request.form.get('user_age'),
            'user_gender': request.form.get('user_gender'),
            'fav_book': request.form.get('fav_book'),
            'fav_author': request.form.get('fav_author'),
            'fav_genre': request.form.get('fav_genre')
        }
        print(update_info)
        mongo.db.users.update(
            {'_id': ObjectId(user['_id'])}, update_info)
        flash('User info updated!')

    else:
        if session['user'] == user['username']:
            return render_template(
                'edit_profile.html', username=user, books=books,
                genres=genres, icons=icons, authors=authors, genders=genders)

        else:
            return render_template(
                'edit_profile.html', username=user, books=books,
                genres=genres, icons=icons, authors=authors, genders=genders)

    return render_template(
            'edit_profile.html', username=user, books=books,
            genres=genres, icons=icons, authors=authors, genders=genders)


@app.route('/add_book', methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        # Set the image variable to the form input
        image = request.form.get('book_image')
        rating = request.form.get('rating-drop')
        if rating:
            rating = int(request.form.get('rating-drop'))

        # The user information from the form that is going to be added
        addBook = {
            'book_title': request.form.get('book_title').capitalize(),
            'author_first_name': request.form.get(
                'author_first_name').capitalize(),
            'author_last_name': request.form.get(
                'author_last_name').capitalize(),
            'genre': request.form.get('genre').lower(),
            'read_book': request.form.get('read-check'),
            'rating': rating,
            'review': request.form.get('book_review'),
            'added_by': session['user'],
            'book_image': image
        }
        # if the user did not upload an image, use this url
        if not image:
            addBook['book_image'] = (
                'https://vignette.wikia.nocookie.net/darkseries/images/9/96/No_book_cover_lg.jpg/revision/latest?cb=20170826200421')

        # if the user uploaded an image, use the uploaded image
        else:
            addBook['book_image'] = request.form.get('book_image')

        # Insert the form information about the book to the database
        mongo.db.books.insert_one(addBook)

        # add the authors full name into the database
        addAuthor = {
            'author_name': request.form.get(
                'author_first_name').title() + (" ")
            + request.form.get('author_last_name').title()
        }

        # Check if the author already exists in the database
        existing_author = mongo.db.authors.find_one(
            {'author_name': addAuthor['author_name'].title()})

        # If the author does not exist, insert name
        if not existing_author:
            mongo.db.authors.insert_one(addAuthor)

        flash('Book added successfully!')
        return redirect(url_for(
            'profile', username=session['user']))
    ratings = mongo.db.ratings.find()
    genres = mongo.db.genres.find().sort('genre_name', 1)
    return render_template('add_book.html', ratings=ratings, genres=genres)


@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    mongo.db.books.delete_one({'_id': ObjectId(book_id)})
    flash('Deleted Book')
    return redirect(url_for('profile', username=session['user']))


@app.route('/logout')
def logout():
    # remove the user from session cookies
    flash("You have been logged out")
    session.pop('user')
    return redirect(url_for('login'))


@app.route('/startpage')
def startpage():
    books = list(mongo.db.books.find())
    all_users = list(mongo.db.users.find())

    return render_template('startpage.html', books=books, all_users=all_users)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
