# Milestone Project 3

    
## UX

### Design

#### Colors
  - #689f38 - light-green darken-2  
  - #388e3c - green darken-2

#### Typography
- Fonts used:
  - 'IBM Plex Sans'
  - 'Questrial'

## User Stories

- #### First Time User
  - **As a first time user** I want to easily understand the purpose for the website

  - I want to know how to start using the service
  - I want to be able to use the service on any type of device
  - I want to be able to register a user
  - When a user is created I want to be able to add books to my profile
  - I want to adjust the information that I save along with the book
  - I also want to be able to add a new book review
  - I want to see other reviews and other users
  - I want to be able to like or dislike other's reviews
  - When I'm finished using the site I want to be able to log out

- #### Returning User
  - **As a returning user** I want to change the information in my profile

  - If I have made any reviews I would like to edit one
  - I want to see other user's profiles 
  - I want to find new books to read

- #### Frequent User
  - **As a frequent user** I want to add more books that I've read or want to read to my profile

  - I want to se recommendations for new books
  - I want to read other's reviews and like or dislike them



  ## Wireframes

- [All the wireframes for this project can be found on this link](https://wireframe.cc/pro/pp/af3d20833395115)

- **Can't view?**
  - Click link to open PDF of wireframes


## DataBase

In the early stages of the project, the use of MySQL as a database for the project was tested out.
The test DataBase Name is Mile and currently contains the tables Users and UserInfo
  					
|   Users     | UserInfo                                    | Reviews                    | Authors         | Books                                        | Genres         |
|-------------|---------------------------------------------|----------------------------|-----------------|----------------------------------------------|----------------|
| first_name  | username (username)                         | heading                    | author_id       | book_id                                      | genre_id       |
| last_name   | user_height                                 | title (books.title)        | first_name      | author_id (authors.author_id)                | genre_name     |
| username    | hair_color                                  | author (books.author_name) | last_name       | title                                        | total_in_genre |
| email       | fav_book (books.title)                      | genre (books.genre)        | number_of_books | author_name (authors.first_name,+ last_name) |                |
| password    | fav_author (authors.first_name + last_name) | written_by (username)      |                 | genre (genres.genre_id)                      |                |
|             | fav_genre (genre_name)                      | rating                     |                 |                                              |                |
|             | user_pic                                    | review                     |                 |                                              |                |
|             | total_likes                                 |                            |                 |                                              |                |
|             | date_joined                                 |                            |                 |                                              |                |
|             | age                                         |                            |                 |                                              |                |

  ## Documentation

- Added a requirements.txt file to save dependencies
- Created a DataBase in MySQL to test out the building

***
## Testing

### Code Validation

### Bugs

 - #### Discovered Bugs
    - Cards are pushed down on the profile page on computer sometimes
    - The user info edit form is not sending information correctly to mongodb
        - Solved by changing the jinja templating in the dropdowns to display correctly and debugged by adding  print(update_info) and checking the added information when called
    - The dropdown menu does not display in the navbar 

    - The icon in the bottom right corner does not disappear if the user already have a session stored. 

    - The function of displaying a longer form when the checkbox is clicked, needs to include a function for the extended form to disappear, but this is not working as expected.
```
$('#read-check').click(function() {
        $('.fin-read').removeClass('no-display').addClass('full-display');
        /*
        var isCheck = $(this).hasClass('no-display');
        if (isCheck == true){
            $('.fin-read').removeClass('no-display').addClass('full-display');
            console.log("Removed, works fine");
        } 
        else {
            $('.fin-read').removeClass('full-display').addClass('no-display');
            console.log("Displayed, works fine");
        }
        */
    });
```

 - #### Solved Bugs
    - The displaying of a modal and confirming delete action [solved with this as help](https://stackoverflow.com/questions/22071042/dynamic-bootstrap-modal-within-a-loop)
    - The text font and styling for the page h3 elements are not loading
        - Solved by commenting out the following code from the style.css file
```
/*
    font-family: 'IBM Plex Sans', sans-serif;
    font-family: 'Questrial', sans-serif;
*/
```
    - Displaying a text about there being no books added on a user profile, if that specific user haven't added any books
**The code was changed from**
```
{% if books|length > 0 %}
					<ul>
                        {% for book in books %}
                            {% if book.added_by|lower == username.username|lower %}
                            {% else %}
                                <h5 class="center-align">No Books Added</h5>
```
This resulted in the text 'No Books Added' being displayed as many times as the amount of books in the database
**To**
```
{% if books|length > 0 %}
					<ul>
                        {% for book in books if book.added_by|lower == username.username|lower %}
                        {% else %}
                            <h5 class="center-align">No Books Added</h5>
```
The condition for the for loop was changed so that only the books that have the same 'added_by' as the profile username will be iterated through.

The result is that the text is shown only once and then ends the loop

- When adding editing buttons to the cards created by the current user, the a tag that wraps every list item was pushed to only cover the image in the card, and the image size was reduced to about half.
    - The bug was solved by moving the a tag so that it wraps the card content/text instead of the whole card.

    - **Bug solved by moving the a tag from right after the opening li tag, to after the code for the editing buttons**


- The images for the list with reviews and users were not lining up with the card-left-border. 
    - I started with adding (.row .col) to the style.css document and set padding:0. This solved the problem but removed the padding for every col and row on the page. To solve it I created a new class called no-padding and applied it to the concerned elements 

- when trying to update the user data, the login information that needs to be unchanged was being overwritten. This bug was solved by storing the static values in variables and then updating them with the same value as what they previously contained
```
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
        mongo.db.users.replace_one({'_id': ObjectId(user['_id'])}, update_info)
```

### Device Compability
***
## Credit

### Resources

- [Wireframes.cc](https://wireframe.cc/)
- [Mockups](http://ami.responsivedesign.is/)
- [Github]()
- [MongoDB]() Database
- [FontAwesome]()
- [Materializecss.com]()
- [Google Fonts](https://fonts.google.com/)
- [Mysqltutorial.org](https://www.mysqltutorial.org/mysql-create-table/) Refreshed memory about database creation
- [W3Schools.com](https://www.w3schools.com/sql/sql_foreignkey.asp) About MySQL and foreign keys
- [This Page](https://kb.objectrocket.com/mongo-db/how-to-insert-a-document-into-a-mongodb-collection-using-python-367) How to import date and how to insert it in MongoDB when adding user

### Content

### Code


## Acknoledgements




<!--Delete Book Modal
        <div id="modal1" class="modal center-align">
            <div class="modal-content">
            <h4>Delete Book</h4>
            <p>Are you sure you want to delete this book? <br>
            <span>(The book can not be restored when deleted)</span></p>
            </div>
            
            <div class="modal-footer center-align">
                <a href="#!" class="modal-close waves-effect waves-green btn-flat">Cancel</a>
                <a href="{{ url_for('delete_book', book_id=book._id) }}" class="modal-close waves-effect waves-green btn-flat">Delete Book</a>
            </div>
            
        </div>
        -->
