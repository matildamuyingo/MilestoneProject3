# Milestone Project 3 
    
<img src='static/images/readme/StartpageMockups.png' width='400px'>

This page is created for users to be able to keep track of books that they want to read, have read, or publish a review for other users to read.

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

  - I want to understand how to start using the service
  - I want to be able to use the service on any type of device
  - I want to be able to register a profile that saves my information for future use
  - I want to easily navigate through the different pages within the website
  - When a profile has been set up, I want to be able to add books to my profile
  - I want to have the choice of just saving a book that I want to read, or list it as a book I've already read
  - When adding a book, I want to have the option of writing a freehand book review
  - I want to see all books and users that exist on the site
  - I want to be able to sort books and users, using simple alternatives that apply to what I'm looking for
  - When I'm finished using the site I want to be able to log out

- #### Returning User
  - **As a returning user** I want to update the information in my profile

  - If I have added any books I want to be able to edit the information I've provided, or add a review
  - I want to see other user's profiles and what books that user have added
  - I want to find new books to read
  - I want to see if there are any new users on the site



  ## Wireframes

- [All the wireframes for this project can be found on this link](https://docs.google.com/presentation/d/1DuUcqRKpWg7ZiIwY2kd2eEBEdwci3eMaHwU-0roaQvA/edit?usp=sharing)

- **Can't view?**
  - [Click link to open PDF of wireframes]("static/wireframes/Wireframes.pdf")


## DataBase

In the early stages of the project, the use of MySQL as a database for the project was tested out.
The test DataBase Name is Mile and currently contains the tables Users and UserInfo


After trying out the MySQL database, the project database was changed to use MongoDB instead. The MongoDB contains 8 collections. Below you can see all the collections and fields that are stored in the MongoDB for this project.

|   Users     | Reviews        | Authors       | Books             | Genders      | Ratings       | Icons        | Genders      |
|-------------|----------------|---------------|-------------------|--------------|---------------|--------------|--------------|
| _id         | _id            | _id           | _id               | _id          | _id           | _id          | _id          |
| first_name  | book_id        | author_name   | book_title        | genre_name   | book_rating   | icon_name    | gender_name  |
| last_name   | added_by       |               | author_first_name |              |               | icon_link    |              |
| username    | review_title   |               | author_last_name  |              |               | icon_path    |              |
| email       | rating         |               | genre             |              |               |              |              |
| password    | review         |               | read_book         |              |               |              |              |
| date_joined |                |               | rating            |              |               |              |              |
| user_icon   |                |               | review            |              |               |              |              |
| user_age    |                |               | added_by          |              |               |              |              |
| user_gender |                |               | book_image        |              |               |              |              |
| fav_book    |                |               | date_added        |              |               |              |              |
| fav_author  |                |               |                   |              |               |              |              |
| fav_genre   |                |               |                   |              |               |              |              |



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


### Content

[No Cover added Photo](https://darkseries.fandom.com/wiki/Dark_Tarot) - This is the source for the photo added when a user decides not to add their own photo to the added book.

[404 Gif](https://www.google.com/url?sa=i&url=https%3A%2F%2Fgiphy.com%2Fgifs%2FoyQ9vezXhFLYRTUx2z%2Fhtml5&psig=AOvVaw1gVv-HS4JvfyMTzRapb8Cp&ust=1608761783663000&source=images&cd=vfe&ved=0CA0QjhxqFwoTCID47ujO4u0CFQAAAAAdAAAAABAI) - If there is an access error, the user will be brought to the 404 page where a book-gif can be seen. The gif comes from Giphy.com 

### Code

- The javascript code for setting the height of the cards to be equal came from [css-tricks.com](https://css-tricks.com/snippets/jquery/equalize-heights-of-divs/).
You can find this code on line 40 in the script.js document

- [Objectrocket.com](https://kb.objectrocket.com/mongo-db/how-to-insert-a-document-into-a-mongodb-collection-using-python-367) was used when finding out how to import a date and how to insert it in MongoDB when inserting a document
- [hover another element](https://stackoverflow.com/questions/6910049/on-a-css-hover-event-can-i-change-another-divs-styling)

## Acknoledgements

I would like to thank my mentor Arnold Kyeza for continuos help throughout the project, and always helping me to aim higher.

Another big thank you to Code Institue, especially the tutor support team that have been a big help when solving problems in the project and helping me understand certain functionalities.


