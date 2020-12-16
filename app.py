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
    if 'user' in session:
        session.pop('user')
        flash('You have been logged out')
        return redirect(url_for('homepage'))
    return render_template('homepage.html')


# Route for register form
@app.route('/register', methods=["GET", "POST"])
def register():

    # If the request method is post (sign up button has been clicked):
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

    # The user information from the form that is going to be added:
        # Save time of submission in a variable
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

        # Insert the form information to the users collection in database
        mongo.db.users.insert_one(register_user)

        # Save the username as session user
        session['user'] = request.form.get('username').lower()

        # Flash a message to the user and redirect to the user login page
        flash('Registration Successful!')
        return redirect(url_for('profile', username=session['user']))

    # Get the icon options from the database
    icons = mongo.db.icons.find()

    # If the user clicked a link to get
    # to register form, return the rendered template
    return render_template('register.html', icons=icons)


# Route for login form
@app.route('/login', methods=["GET", "POST"])
def login():

    # If the request method is post (login button has been clicked):
    if request.method == "POST":

        # Check if the username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # If the username exists in the database, do the following:
        if existing_user:

            # Check if password matches username
            # and redirect user to profile or login-page
            if check_password_hash(
                    existing_user['password'], request.form.get('password')):
                session['user'] = request.form.get('username').lower()
                return redirect(url_for(
                    'profile', username=session['user']))
            else:
                # if password and username does not match
                flash("Wrong password or username")
                return redirect(url_for('login'))

        # If the username does not exist:
        else:
            # inform the user that they cannot log in
            flash('Wrong password or username')
            return redirect(url_for('login'))

    # If the user clicked a link to get
    # to login form, return the rendered template
    return render_template('login.html')


# Route for profile pages
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Gets a list with all books added
    # to the database and sets the user variable
    books = list(mongo.db.books.find())
    user = mongo.db.users.find_one(
        {'username': username})
    reviews = list(mongo.db.reviews.find())

    # if the username is the same as
    # session user, send user to their own profile
    if session['user'] == user['username']:
        return render_template(
            'profile.html', username=user, books=books, reviews=reviews)
    # if the username is not the same as
    # session user, send user the other userprofile
    else:
        return render_template(
            'profile.html', username=user, books=books, reviews=reviews)

    return redirect(url_for('login'))


# Route to edit profile info (only available on the users own profile page)
@app.route('/edit_profile/<username>', methods=["GET", "POST"])
def edit_profile(username):

    if session['user'] == username:
        # Get lists with saved database-information and set the user variable
        books = list(mongo.db.books.find().sort('book_title', 1))
        genres = list(mongo.db.genres.find().sort('genre_name', 1))
        authors = list(mongo.db.authors.find().sort('author_name', 1))
        genders = list(mongo.db.genders.find())
        icons = list(mongo.db.icons.find())
        user = mongo.db.users.find_one(
            {'username': username})

        # If the form is submitted
        if request.method == "POST":

            # Save username, email, password and
            # date joined in variables, these won't be changed
            u_name = user['username']
            email = user['email']
            password = user['password']
            joined = user['date_joined']

            # Create an object that gets the values from the update info form
            update_info = {
                'first_name': request.form.get('first_name').lower(),
                'last_name': request.form.get('last_name').lower(),
                'username': u_name,
                'email': email,
                'password': password,
                'date_joined': joined,
                'user_icon': request.form.get('user_icon').lower(),
                'user_age': int(request.form.get('user_age')),
                'user_gender': request.form.get('user_gender').lower(),
                'fav_book': request.form.get('fav_book').title(),
                'fav_author': request.form.get('fav_author').lower(),
                'fav_genre': request.form.get('fav_genre').lower()
            }

            # Insert the updated info into the database
            mongo.db.users.update(
                {'_id': ObjectId(user['_id'])}, update_info)
            flash('User info updated!')
            return redirect(url_for('profile', username=u_name))
    else:
        return render_template('404.html')

    # If the user clicked the link to get
    # to the edit info form, pass through variable info
    return render_template(
            'edit_profile.html', username=user, books=books,
            genres=genres, icons=icons, authors=authors, genders=genders)


# Route to add a new book
@app.route('/add_book', methods=["GET", "POST"])
def add_book():

    # If the add book form is submitted
    if request.method == "POST":

        # Set the image, rating and date
        # variable to the form input (optional inputs)
        image = request.form.get('book_image')
        datetime_now = datetime.now()
        rating = request.form.get('rating-drop')

        # if a rating has been added, save it as an integer

        # The user information from the form that is going to be added/updated
        addBook = {
            'book_title': request.form.get('book_title').lower(),
            'author_first_name': request.form.get(
                'author_first_name').lower(),
            'author_last_name': request.form.get(
                'author_last_name').lower(),
            'genre': request.form.get('genre').lower(),
            'read_book': 'on' if request.form.get('read-check') else False,
            'rating': 'None' if rating is None else int(request.form.get('rating-drop')),
            'review': request.form.get('book_review').capitalize(),
            'added_by': session['user'],
            'book_image': image,
            'date_added': datetime_now
        }

        # if the user did not upload an image, use this url as default
        if not image:
            addBook['book_image'] = (
                'https://vignette.wikia.nocookie.net/darkseries/images/9/96/No_book_cover_lg.jpg/revision/latest?cb=20170826200421')

        # if the user uploaded an image, use the uploaded image
        else:
            addBook['book_image'] = request.form.get('book_image')

        # Insert the form information about the book to the database
        mongo.db.books.insert_one(addBook)

        # Add the authors full name into the
        # database merged in a single variable
        addAuthor = {
            'author_name': request.form.get(
                'author_first_name').lower() + (" ")
            + request.form.get('author_last_name').lower()
        }

        # Check if the author already exists in the database
        existing_author = mongo.db.authors.find_one(
            {'author_name': addAuthor['author_name'].lower()})

        # If the author does not exist, insert name
        if not existing_author:
            mongo.db.authors.insert_one(addAuthor)

        # Flash confirmation message to user and redirect for profile
        flash('Book added successfully!')
        return redirect(url_for(
            'profile', username=session['user']))
    # Save ratings and genres from database
    # in variables and sort genres alphabetically
    ratings = mongo.db.ratings.find()
    genres = mongo.db.genres.find().sort('genre_name', 1)

    # If user clicked link to access add book
    # page render template with parameters set
    return render_template('add_book.html', ratings=ratings, genres=genres)


# Route to edit book info (only available on books the user created)
@app.route('/edit_book/<book_id>', methods=["GET", "POST"])
def edit_book(book_id):

    # Get lists with saved database-information and set the user variable
    genres = list(mongo.db.genres.find().sort('genre_name', 1))
    ratings = mongo.db.ratings.find()
    rating = request.form.get('rating-drop')

    book = mongo.db.books.find_one(
        {'_id': ObjectId(book_id)})

    if session['user'] == book['added_by']:

        # If the form is submitted
        if request.method == "POST":

            # Set the image, rating and date
            # variable to the form input (optional inputs)
            image = request.form.get('book_image')
            datetime_now = datetime.now()

            # if a rating has been added, save it as an integer

            # Create an object that gets the values from the update book form
            update_book = {
                'book_title': request.form.get('book_title').lower(),
                'author_first_name': request.form.get(
                    'author_first_name').lower(),
                'author_last_name': request.form.get(
                    'author_last_name').lower(),
                'genre': request.form.get('genre').lower(),
                'read_book': 'on' if request.form.get('read-check') else False,
                'rating': 'None' if rating is None else int(request.form.get('rating-drop')),
                'review': request.form.get('book_review').capitalize(),
                'added_by': session['user'],
                'book_image': image,
                'date_added': datetime_now
            }
            print(update_book['read_book'])

            # Insert the updated info into the database
            mongo.db.books.update(
                {'_id': ObjectId(book_id)}, update_book)

            # Inform the user that the book was successfully updated
            flash('Book updated!')
            return redirect(url_for(
                'profile', username=update_book['added_by']))
    else:
        return render_template('404.html')

    return render_template(
            'edit_book.html', book_id=book, books=book,
            genres=genres, ratings=ratings)


# Route to delete a book
@app.route('/delete/<book_id>')
def delete_book(book_id):

    # Find and delete the book with same id as clicked object (book)
    mongo.db.books.delete_one({'_id': ObjectId(book_id)})
    flash('Deleted Book')

    # Set variables and render template for user profile after book is deleted
    books = list(mongo.db.books.find())
    reviews = list(mongo.db.reviews.find())
    user = mongo.db.users.find_one(
        {'username': session['user']})

    return render_template(
        'profile.html', username=user, books=books, reviews=reviews)


# Route to detailed book info
@app.route('/book_info/<book_id>', methods=["GET", "POST"])
def book_info(book_id):

    book = mongo.db.books.find_one(
        {'_id': ObjectId(book_id)})
    reviews = mongo.db.reviews.find(
        {'book_id': book_id})

    return render_template('book_info.html', book_id=book, reviews=reviews)


@app.route('/add_review/<book_id>', methods=["GET", "POST"])
def add_review(book_id):

    book = mongo.db.books.find_one(
        {'_id': ObjectId(book_id)})
    ratings = mongo.db.ratings.find()
    reviews = mongo.db.reviews.find(
        {'book_id': book_id})
    image = book['book_image']
    title = book['book_title']
    authorFN = book['author_first_name']
    authorLN = book['author_last_name']
    genre = book['genre']
    datetime_now = datetime.now()
    rating = request.form.get('rating-drop')

    if request.method == "POST":

        new_review = {
            'book_id': book_id,
            'added_by': session['user'],
            'review_title': request.form.get('review_title'),
            'rating': 'None' if rating is None else int(request.form.get('rating-drop')),
            'review': request.form.get('review')
        }

        update_review = {
            'book_title': title,
            'author_first_name': authorFN,
            'author_last_name': authorLN,
            'genre': genre,
            'book_image': image,
            'read-book': 'on',
            'added_by': session['user'],
            'review_title': request.form.get('review_title'),
            'rating': 'None' if rating is None else int(request.form.get('rating-drop')),
            'review': request.form.get('review'),
            'date_added': datetime_now
        }

        if new_review['added_by'] == book['added_by']:
            mongo.db.books.update(
                {'_id': ObjectId(book_id)}, update_review)
        else:
            mongo.db.reviews.insert_one(new_review)

        return render_template('book_info.html', book_id=book, reviews=reviews)

    return render_template('add_review.html', book_id=book, ratings=ratings)


# Route to delete a review
@app.route('/delete/<review_id>')
def delete_review(review_id):

    # Find and delete the book with same id as clicked object (book)
    mongo.db.reviews.delete_one({'_id': ObjectId(review_id)})
    flash('Deleted Review')

    # Set variables and render template for user profile after book is deleted
    reviews = list(mongo.db.reviews.find())
    books = list(mongo.db.books.find())
    user = mongo.db.users.find_one(
        {'username': session['user']})

    return render_template(
        'profile.html', username=user, books=books, reviews=reviews)


# Route to startpage
@app.route('/startpage')
def startpage():

    # Get list with all books and users and
    # save in variables, then render startpage template
    books = list(mongo.db.books.find().sort('date_added', -1))
    all_users = list(mongo.db.users.find().sort('date_joined', -1))

    return render_template('startpage.html', books=books, all_users=all_users)


# Route to all books page
@app.route('/all_books')
def all_books():

    # Get list with all books and users and
    # save in variables, then render all books template
    books = list(mongo.db.books.find())

    return render_template('all_books.html', books=books)


@app.route('/sort_books', methods=["GET", "POST"])
def sort_books():

    book_query = list(mongo.db.books.find())
    if request.method == "POST":
        sort_method = request.form.get('book_sorting')
        book_query = list(mongo.db.books.find().sort(sort_method, 1))

    return render_template(
        "all_books.html", books=book_query)


# Route to all books page
@app.route('/all_users')
def all_users():

    # Get list with all books and users and
    # save in variables, then render all books template
    users = list(mongo.db.users.find())

    return render_template('all_users.html', all_users=users)


@app.route('/sort_users', methods=["GET", "POST"])
def sort_users():

    user_query = list(mongo.db.users.find())
    if request.method == "POST":
        sort_method = request.form.get('user_sorting')
        user_query = list(mongo.db.users.find().sort(sort_method, 1))

    return render_template(
        "all_users.html", all_users=user_query)


# Route to logout
@app.route('/logout')
def logout():

    # remove the user from session cookies and redirect to login page
    session.pop('user')
    flash('You have been logged out')
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
