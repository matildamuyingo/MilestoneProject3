# Milestone Project 3 

[View the live project here](http://bookers-milestone-project.herokuapp.com/)
    
<img src='static/images/readme/StartpageMockups.png' width='400px'>

This page is created for users to be able to keep track of books that they want to read, have read, or publish a review for other users to read.

# Table of Content

1. [UX](#ux)
2. [Features](#features)
3. [Testing](#testing)
4. [Bugs](#bugs)
5. [Credit](#credit)


## UX

### Design
The page design has been made with simplicity in thought, but at the same time calming and easy colors and fonts. 

#### Colors
**Hex-number & Materializecss name:**
  - #689f38 - light-green darken-2  
  - #388e3c - green darken-2

#### Typography
**Fonts used:**
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

<br>

## Wireframes

[All the wireframes for this project can be found on this link](https://docs.google.com/presentation/d/1DuUcqRKpWg7ZiIwY2kd2eEBEdwci3eMaHwU-0roaQvA/edit?usp=sharing)

<br>

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

## Features
*** 

### Existing Features 
[Jump to testing section](#project-walktrough)

#### Navigation Bar
* **1.1** Hover navigation bar at top of the page to get a darker background for the clickable links.

* **1.2** On smaller screens, switch navbar to a book-icon that opens a side navigation when clicked.
* **1.3** If not logged in, only show links for login, register and homepage.
* **1.4** When logged in, show links for startpage, add books, all books, all users, profile and log out.
* **1.5** When hovering the page logo, displayed in the middle of the navbar, an animation of a page turning should be showed.
* **1.6** If logo is clicked, redirect user to homepage (if not logged in), and to startpage (if logged in)

#### Homepage
* **2.1** Display buttons with links to register and to login pages.

    * **2.1.1** When hovering buttons, the button-shadow will get smaller.
* **2.2** If a user was logged in when accessing the homepage, log them out/remove session cookies.
    * **2.2.1** Flash message that the user was logged out.

#### Register
* **3.1** A responsive size form with input fields is displayed.

* **3.2** The field for icon is a dropdown select, which displays pictures of the diferent options for profile-icon.
* **3.3** Fields for first name, last name, email, username and password are text inputs.
* **3.4** When adding text in the input fields, the input bottom-border will turn green.
* **3.5** When clicking the submit button, all information added to the register form is inserted in the users collection in the database.
* **3.6** If there is an empty field when submitting the form, a message will be displayed to the user that input is required, and field bottom-border will change color to red.
* **3.7** If username or email address already exists in database a flash message will be displayed telling the user to pick another username/email.
* **3.8** If all information is correct, redirect user to the user profile.


#### Login
* **4.1** Show two text input fields that requires username and password for login.

* **4.2** When button for log in is clicked, check if username and password matches any stored user information in the database.
* **4.3** If username does not match any username in the database, flash a message that the information is incorrect.
* **4.4** If the password does not match the username, flash a message that the information is incorrect.
* **4.5** If trying to submit without adding information, a message will pop up telling user that input is required.
* **4.6** If all information is correct, redirect user to the user profile.
* **4.7** When user is logged in, display a plus icon at the bottom right of every page with link to add book.
  * **4.7.1** If icon is hovered, display tooltip information 'add a new book'.

#### Profile
* **5.1** Display the added first name + s' profile at the top of the profile.

* **5.2** If no books have been added by the profile user, display 'No books added' text underneath the 'Saved books' and 'Read books' headings.
* **5.3** If no reviews have been added, display 'No added reviews' underneath the Review heading.
* **5.4** Display selected user icon and the user information to the left of profile page on larger screens. On smaller screen the about section is displayed directly underneath the page header.
* **5.5** If books have been added by user, show books with 'read_book' = 'on' under the 'Have read heading' and books without the condition under the 'Saved Books' heading.
* **5.6** When hovering book-cards, lift the card and deepen the shadow.
* **5.7** If the book was added by the logged in user, show buttons to edit and delete the hovered book.
    * **5.7.1** If the edit icon is clicked, redirect user to the edit_book page, with existing information filled in.
    * **5.7.2** If the trashcan icon is clicked, show a popup modal that asks user if they're sure they want to delete the book. 
        * **5.7.2.1** If 'Agree' is clicked, remove book from database and flash message that book was removed. 
        * **5.7.2.2** If cancel is clicked, close modal.
* **5.8** If the book card is clicked, redirect user to that specific book-info page.
* **5.9** If the profile belongs to the logged in user, display 'Edit Info' button at the bottom of about info, and 'Add new book' at the bottom of My Books.
* **5.10** Display all reviews added by profile user at the bottom of the page.
* **5.11** When hovering reviews, show buttons for edit review and delete review.
  * **5.11.1** If the edit icon is clicked, redirect user to the edit_review page, with existing information filled in.
  * **5.11.2** If the trashcan icon is clicked, show a popup modal that asks user if they're sure they want to delete the review. 
    * **5.11.2.1** If 'Agree' is clicked, remove review from database and flash message that review was removed. 
    * **5.11.2.2** If cancel is clicked, close modal.
* **5.12** If review is clicked, bring user to the book info page belonging to that review.

#### Edit Profile
* **6.1** If page is acessed with url by someone who is not the user of the profile that is being edited, user is redirected to the 404 error page.

* **6.2** Edit fields for icon, gender, favorite book, favorite author, favorite genre are dropdown selects with color validation for added input.
* **6.3** Favorite book and author lists are generated from all added books and authors that exists in the database.
* **6.4** If update info button is clicked, the input information is updated in the user collection of the database.
  * **6.4.1** If a required field is missing input, the user will get a message that input is required.

#### Add Book
* **7.1** When accessing a page, the user sees a form where information about a book can be added. 

* **7.2** If the user clicks on the checkbox for 'finished reading', the bottom of the form for filling out book rating and adding a book review is displayed.
* **7.3** When hovering the field for adding an image url, a tooltip message is displayed telling the user to paste an image url.
* **7.4** If an image is not added, a blank image with the text 'No book cover' will be added instead.
* **7.5** When submitting the form, the user will be informed about required fields that have not been filled in.

#### Startpage
* **8.1** When accessing the startpage, displayed the 4 latest added books to the left, and the 6 latest added users to the right. On smaller screens the books will be displayed first and users after books.

* **8.2** When hovering a book or a user card, move the card up and deepen the shadow underneath the card.
* **8.3** If a book card is clicked, bring the user to that specific book page.
* **8.4** If a user card is clicked, bring the user to that user's profile.
* **8.5** At the end of the column with cards, display one button to bring user to see all books, and another button to bring user to page displaying all users.
* **8.6** If hovering a book that was added by the current logged in user, display editing/delete icons.
    * **8.6.1** If delete icon is clicked, open a modal asking for delete confirmation.
        * **8.6.1.1** If deletion is confirmed, remove book from database, close modal and flash message of delete confirmation to user.

#### All Books and All Users
* **9.1** When accessing pages, display all books/all users stored in database.

* **9.2** If the user selects a sorting option in the 'Sort By' input, automatially update sorting conditions and reload page.
* **9.3** If a sorting method has been chosen, display the method in the select input.
* **9.4** When hovering a card, move card up and deepen shadow underneath.
* **9.5** If a book card is clicked, bring user to that book page.
* **9.6** If a user card is clicked, bring user to that user's profile.
* **9.7** At the end of the list of books and users, generate a button that brings user to the top of the same page.
* **9.8** On the 'All books' page, if a book has an added review, display a small 'click to show review' text.

#### Book Info
* **10.1** Display selected books detailed info (all info available).

* **10.2** If there are reviews added, display them.
    * **10.2.1** If there is more than one review added to the book, make the background color change for every second review.
* **10.3** If the review was added by the same user that added the book, use 'Review added by' as review headline.
    * **10.3.1** If user have updated review to include a review title, display the review title as headline instead.
* **10.4** If user hovers a review added by themself, display editing buttons.
    * **10.4.1** If edit icon is clicked, bring user to the edit review page.
    * **10.4.2** If delete icon is clicked, open a modal to confirm review deletion.
        * **10.4.2.1** If delete action is confirmed, remove review from database.

#### Add Review
* **11.1** If link is accessed from the book info page by the user that originally added the book, allow the user to update their review instead of adding a new review.
    * **11.1.1** Let the fields be filled in with existing information.

* **11.2** If link is accessed by a user that did not add the original review, let the user access a blank form with review info to fill out.
* **11.3** If the user clicks the cancel button, redirect them back to the book info page without changing anything.

#### Edit Review
* **12.1** When clicking the edit icon for a review, the user will be brought to the edit form, with all previously added information filled in.

* **12.2** When clicking submit review, the field information will be updated in the database for that specific review.
* **12.3** If a user tries to access a review through url, without being the creator of the original review, the user will be redirected to the 404 page.
* **12.4** If a user tries to submit the form without having filled in all fields, there will be a message telling the user that the field is required.
* **12.5** If the user clickes the cancel button, they will be brought back to the book info page, without updating/changing any information.

<br>

***

## Testing

### Project Walktrough
The testing of the project is based on the [Existing Features](#existing-features) part of the readme. Each test-heading will be linked to the list of features on that page. If you want to doubble check what features have been tested, follow the correlated list numbering.
<br>
[Click here](#code-validation) to skip the feature testing section.


[Navigation Bar](#navigation-bar)

|Feature |Tested |Chrome|IOS   |Commentary |
|--------|-------|------|------|-----------|
|1.1     |x      |works |-     |           |
|1.2     |x      |works |works |           |
|1.3     |x      |works |works |           |
|1.4     |x      |works |works |           |
|1.5     |x      |works |works*|This works if the logo is clicked. There is a bug on mobile that makes the logo animation display worong sometimes.  |
|1.6     |x      |works |works |           |


[Homepage](#homepage)

|Feature |Tested |Chrome|IOS   |Commentary |
|--------|-------|------|------|-----------|
|2.1     |x      |works |works |           |
|2.2     |x      |works |-   |Not displayed on smaller devices |
|2.3     |x      |works |works |           |
|2.4     |x      |works |works |           |

[Register](#register)

|Feature |Tested |Chrome|IOS   |Commentary |
|--------|-------|------|------|-----------|
|3.1     |x      |works*|works |The icon text is a bit to big to fit the field on screen sizes between 600px - 900px           |
|3.2     |x      |works |works |           |
|3.3     |x      |works |works |           |
|3.4     |x      |works |works |           |
|3.5     |x      |works |works |           |
|3.6     |x      |works |works |           |
|3.7     |x      |works |works |           |
|3.8     |x      |works |works |           |

[Login](#login)

|Feature |Tested |Chrome|IOS   |Commentary |
|--------|-------|------|------|-----------|
|4.1     |x      |works |works |           |
|4.2     |x      |works |works |           |
|4.3     |x      |works |works |           |
|4.4     |x      |works |works |           |
|4.5     |x      |works |works |           |
|4.6     |x      |works |works |           |
|4.7     |x      |works |works |           |
|4.7.1   |x      |works*|works |The hover function only works on computer devices. On other types of devices, the component has to be clicked for the hover function to display. There is a bug that makes the tooltip stick to one spot on the page.|

[Profile](#profile)

|Feature |Tested |Chrome|IOS   |Commentary |
|--------|-------|------|------|-----------|
|5.1     |x      |works |works |           |
|5.2     |x      |works*|works |If the user have added a book to either the category of 'saved books' or 'have read' books, the text for the other category disappears.|
|5.3     |x      |works |works |           |
|5.4     |x      |works |works |           |
|5.5     |x      |works |works |           |
|5.6     |x      |works |works |           |
|5.7     |x      |works |works*|The hover function only works on computer devices. On other types of devices, the component has to be clicked for the hover function to display.|
|5.7.1   |x      |works |works |           |
|5.7.2   |x      |works |works |           |
|5.7.2.1 |x      |works |works |           |
|5.7.2.2 |x      |works |works |           |
|5.8     |x      |works |works |           |
|5.9     |x      |works |works |           |
|5.10    |x      |works |works |           |
|5.11    |x      |works |works*|The hover function only works on computer devices. On other types of devices, the component has to be clicked for the hover function to display.|
|5.11.1  |x      |works |works |           |
|5.11.2  |x      |works |works |           |
|5.11.2.1|x      |works |works |           |
|5.11.2.2|x      |works |works |           |
|5.12    |x      |works |works |           |

[Edit Profile](#edit-profile)

|Feature |Tested |Chrome|IOS   |Commentary |
|--------|-------|------|------|-----------|
|6.1     |x      |works |works |           |
|6.2     |x      |works |works |           |
|6.3     |x      |works |works |           |
|6.4     |x      |works |works |           |
|6.4.1   |x      |works |works |           |

[Add Book](#add-book)

|Feature |Tested |Chrome|IOS   |Commentary |
|--------|-------|------|------|-----------|
|7.1     |x      |works |works |           |
|7.2     |x      |works |works |           |
|7.3     |x      |works*|works |The hover function works on all devices if the field is selected.|
|7.4     |x      |works*|works |If the url added does not exist, the picture displayed will be one of the standard no image. |
|7.5     |x      |works |works |           |

[Startpage](#startpage)

|Feature |Tested |Chrome|IOS   |Commentary |
|--------|-------|------|------|-----------|
|8.1     |x      |works |works |           |
|8.2     |x      |works |works |           |
|8.3     |x      |works |works |           |
|8.4     |x      |works |works |           |
|8.5     |x      |works |works |           |
|8.6     |x      |works*|works |The hover function only works on computer devices. On other types of devices, the component has to be clicked for the hover function to display.|
|8.6.1   |x      |works |works |           |
|8.6.1.1 |x      |works |works |           |

[All Books and All Users](#all-books-and-all-users)

|Feature |Tested |Chrome|IOS   |Commentary |
|--------|-------|------|------|-----------|
|9.1     |x      |works |works |           |
|9.2     |x      |works |works |           |
|9.3     |x      |works |does not work*|This is a larger bug that appears on some mobile devices. The options pushes the alternatives down to pick the second option over the one clicked.  |
|9.4     |x      |works |works |           |
|9.5     |x      |works |works |           |
|9.6     |x      |works |works |           |
|9.7     |x      |works |works |           |
|9.8     |x      |works |works |           |

[Book Info](#book-info)

|Feature |Tested |Chrome|IOS   |Commentary |
|--------|-------|------|------|-----------|
|10.1    |x      |works |works |           |
|10.2    |x      |works |works |           |
|10.2.1  |x      |works |works |           |
|10.3    |x      |works |works |           |
|10.3.1  |x      |works |works |           |
|10.4    |x      |works*|works*|This feature is not implemented for reviews added by the original book submitter. Only works on mobile devices if clicked. |
|10.4.1  |x      |works |works |           |
|10.4.2  |x      |works |works |           |
|10.4.2.1|x      |works |works |           |

[Add Review](#add-review)

|Feature |Tested |Chrome|IOS   |Commentary |
|--------|-------|------|------|-----------|
|11.1    |x      |works*|works |Edit buttons for originally added reviews are left to be implemented. |
|11.1.1  |x      |works |works |           |
|11.2    |x      |works |works |           |
|11.3    |x      |works |works |           |

[Edit Review](#edit-review)

|Feature |Tested |Chrome|IOS   |Commentary |
|--------|-------|------|------|-----------|
|12.1    |x      |works |works |           |
|12.2    |x      |works |works |           |
|12.3    |x      |works*|works |This only works for urls only containing the review id. If both book id and review id is included in the url, the redirection does not work. If id is not in the database at all, the page throws an error. |
|12.4    |x      |works |works |           |
|12.5    |x      |works |works |           |

### Code Validation

**HTML Validation:**

All pages were checked using the [W3C Markup Validation Service](https://validator.w3.org/).
Since the project uses jinja2 templating there are errors regarding this format, but all other html-elements passed.

**CSS Validation:**

The custom CSS file was checked using [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/).
<br>
Code passed without any errors.

**JavaScript Validation:**

The custom JavaScript file was checked using [JShint](https://jshint.com/).
<br>
Code passed without any errors.

**Python Validation:**

The python code was validated using [PEP8 online check](http://pep8online.com/checkresult).
There are a few errors related to a few lines being to long. This is a problem that was decided to be left in the project to not interfere with existing url links or non-breakable code lines.


### Bugs


**Solved Bugs**

- The displaying of a modal and confirming delete action [solved with this as help](https://stackoverflow.com/questions/22071042/dynamic-bootstrap-modal-within-a-loop). The modal was being displayed inside the card, instead of inside the window. Solved by moving the code to the end of the card loop.

- Displaying a text about there being no books added on a user profile, if that specific user haven't added any books
    - The bug appeared as a problem because of div closing. The indentation prevented some text to appear since div had already been closed. The code was also changed so that the text would only appear one time, instead of once for every iteration of existing books in the database.

- When adding editing buttons to the cards created by the current user, the a tag that wraps every list item was pushed to only cover the image in the card, and the image size was reduced to about half.
    - The bug was solved by moving the a tag so that it wraps the card content/text instead of the whole card.

- The images for the list with reviews and users were not lining up with the card-left-border. 
    - I started with adding (.row .col) to the style.css document and set padding:0. This solved the problem but removed the padding for every col and row on the page. To solve it I created a new class called no-padding and applied it to the concerned elements 

- Cards displaying books on a user profile created the bug of pushing the cards down and breaking the rows. This was due to each card containing a diferent amount of text in the review. 
This was first solved by adding a specific height to the cards:
```
.book-card-style {
        height: 300px;
    }
```

This made all cards very big and unpleasing to the eye, and one of the cards contained a longer review, the text would push over. To solve it a piece of code from [css-tricks.com](https://css-tricks.com/snippets/jquery/equalize-heights-of-divs/) was used to set the card height to the largest value for the exsisting cards.

- When trying to update the user data, the login information that needs to be unchanged was being overwritten. This bug was solved by storing the static values in variables and then updating them with the same value as what they previously contained
```
    if request.method == "POST":
    
//These variables were created to get the stored information 
        u_name = user['username']
        email = user['email']
        password = user['password']
        joined = user['date_joined']

        update_info = {
            'first_name': request.form.get('first_name').capitalize(),
            'last_name': request.form.get('last_name').capitalize(),

// The variables were added as the information to be updated to prevent a loss of the original information
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

- The user info edit form was not sending information correctly to mongodb 
    - Solved by changing the jinja templating in the dropdowns to display correctly and debugged by adding  print(update_info) and checking the added information when called

- The icon in the bottom right corner does not disappear if the user already have a session stored. 
    - Solved by automatically removing stored sessions if homepage is accessed with a stored session.

<br>

***

## Deployment


### Deploying to Heroku

To get the project to run correctly we first have to make sure all dependecies are installed and can be found in the requirements.txt file:

In the console, type:
``` 
1. pip3 freeze --local >requirements.txt
2. echo web:python.app > Procfile
```

Make sure all required files are installed, and that an env.py containing the IP, PORT, SECRET_KEY, MONGO_URI and MONGO_DBNAME variables are set.

Go to [Heroku.com](https://www.heroku.com/) and create a profile/log in.

- When logged in, find the 'Create a New App' button on the dashboard.
- Give your app a name using dashes instead of spaces.
- Click 'Create App'.

To set up automatic deployment from Github to Heroku, do the following:

- Click the github logo on the deploy page.
- Connect your github account and select the correct repository.
- Click 'Connect' to connect the repository to your app.

Go to the Settings tab and click 'Reveal Config Vars'

- Fill in the values for the variables hidden in the env.py file (IP, PORT, SECRET_KEY, MONGO_URI, MONGO_DBNAME)
- Go back to the deploy tab and click 'Enable Automatic Deplolyment'

<br>

When making changes in the github file, do the following in the console:
```
1. $ git status
2. $ git add file
3. $ git push -m "message"
```

***
## Credit

### Resources

- [Responsivedesign.is](http://ami.responsivedesign.is/) was used to make mockups that can be seen at the start of the readme file.
- [Github](https://github.com/) is the project host
- [MongoDB](https://www.mongodb.com/) is the database host that was used in the project to store all data.
- [FontAwesome](https://fontawesome.com/) provided all icons that are seen in the project.
- [Materializecss.com]() is the framework used to make the project responsive on all screen sizes and provided many pre-made components that can be found throughout the project.
- [Google Fonts](https://fonts.google.com/) was used to import the fonts used in the project.
- [JQuery](http://code.jquery.com/) was used when writing custom JavaScript and is also required for some of the Materializecss components to work.

<br>

### Content

[Books Backgroun Image](https://www.incimages.com/uploaded_files/image/1920x1080/rey-seven-nm-mZ4Cs2I-unsplash_397351.jpg) that can be seen throughout the page comes from this link.

[No Cover added Photo](https://darkseries.fandom.com/wiki/Dark_Tarot) - This is the source for the photo added when a user decides not to add their own photo to the added book.

[404 Gif](https://www.google.com/url?sa=i&url=https%3A%2F%2Fgiphy.com%2Fgifs%2FoyQ9vezXhFLYRTUx2z%2Fhtml5&psig=AOvVaw1gVv-HS4JvfyMTzRapb8Cp&ust=1608761783663000&source=images&cd=vfe&ved=0CA0QjhxqFwoTCID47ujO4u0CFQAAAAAdAAAAABAI) - If there is an access error, the user will be brought to the 404 page where a book-gif can be seen. The gif comes from Giphy.com 

<br>

### Code

- The javascript code for setting the height of the cards to be equal came from [css-tricks.com](https://css-tricks.com/snippets/jquery/equalize-heights-of-divs/).
You can find this code on line 40 in the script.js document

- [Objectrocket.com](https://kb.objectrocket.com/mongo-db/how-to-insert-a-document-into-a-mongodb-collection-using-python-367) was used when finding out how to import a date and how to insert it in MongoDB when inserting a document
- [Stackoverflow.com](https://stackoverflow.com/questions/6910049/on-a-css-hover-event-can-i-change-another-divs-styling) provided code for how to use the hover function on one element to change another element. This is used in the top book-logo animation.
- The code for the JavaScript function validateMaterializeSelect() was provided by Code Institue. The code can be found in the script.js file on line 51-77.

<br>

## Acknoledgements

I would like to thank my mentor Arnold Kyeza for continuos help throughout the project, and always helping me to aim higher.

Another big thank you to Code Institue, especially the tutor support team that have been a big help when solving problems in the project and helping me understand certain functionalities.


