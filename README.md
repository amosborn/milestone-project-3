# Lilliput Book Club

  Code Institute milestone project 3, Data Centric Development module 

## UX

  The goal of this project is to create a simple website where users can access information from a database and add to the database too. 
  The website is designed to be responsive on all device sizes. It has a uncluttered design to make it easy to navigate.
  The website is the created by a local bookshop, to bring local readers together so they can share their reviews, and promote the bookshop too by providing a link to buy the book from the bookshop on each review.


### User stories

    As a user of this website, I want to:

    * navigate the website easily
    * join the book club by creating an account and signing up
    * log in to my account to see the reviews I have written
    * create a new review and add it to the database
    * edit my reviews
    * delete a review I have written
    * search the whole database for reviews written by all users
    * read a review of another user and buy that book from the bookshop by the link provided

    As a the bookshop owner, I want to

    * promote the bookshop by having its name on the website
    * allow users to buy books from the shop by clicking a link on the review

##Features

### Existing Features

    * Navbar for site navigation
    * Simple login/register feature
    * Search option with categories (READ)
    * User can add a review (CREATE)
    * User can edit their own reviews (EDIT)
    * User can delete their own reviews (DELETE)
    * Search results shown on cards

### Features Left to Implement

    * authentication for logging in (although not required for this project)
    * member update/delete their profile
    * pagination for results list of reviews
    * link to buy book from bookshop
    * social media links for the bookshop in the footer
    * about page to give more information about the bookshop
    * counter for members to upvote books they like
    * sort for reviews, by date (most recent) or most popular
    * search bar in navbar for full text search

## Database

MongoDB Atlas is the database used for this project. 
There are two collections, 'reviews' for the reviews of books added by users, and 'users' for user details.

#### users:
    
    Field | Type
    ----- | ----
    _id | ObjectId
    username | string
    first_name | string
    last_name | strimg
    email | string
    password | string

#### reviews:

    Field | Type
    ----- | ----
    _id | ObjectId
    username | string
    title | string
    author | string
    category | string
    rating | string
    cover | string
    review | string

## Technologies used

    1. HTML5
    2. CSS3
    3. JQuery 3.2.1
    4. Materialize 0.100.2 framework
    5. Python3
    6. PyMongo for MongoDB Atlas
    7. Flask
    8. Jinja
    9. Google fonts
    10. Gitpod IDE

## Testing

#### Manual testing:

    Navbar:
    * All links in the navbar have been tested to go to the correct pages.

    Footer:
    * About link not connected, as stated in features left to implement section.

    Home page:
    * Form buttons have been tested to redirect to correct pages.
    * Form cannot be submitted without input.
    * Sign in redirects to user's reviews.

    My Reviews page:
    * Displays reviews from correct user.
    * Buttons redirect to correct pages.
    * Edit button gives form for user to edit review.
    * Delete button deletes the review.
    * Buy button not connect, as stated in features left to implement section.

    Sign Up page:
    * Form tested so all fields must be filled to submit.
    * If username already taken, flashed message is diplayed.
    * If email already used, redirect to sign in with flashed message.

    Search page:
    * search returns expected results when tested as a user.
    * blank search returns all reviews in database.

    The website has been tested on desktop, tablet and mobile screen sizes to be responsive.
    Chrome, Google Internet Explorer and Firefox web browsers were tested.

#### Code validation

    * W3C HTML Validator
    * W3C CSS Validator
    * PEP8 python validator

## Deployment

    Gitpod IDE was used for developing this project.
    The Code Instiute Full Template was used to create the repository.
    The code was committed to github repository and pushed to Github.

    The Github repository is:

    To run this project locally in an environment like Gitpod, install PIP and Python3 and run the command 'python3 app.py'.

    ### Heroku Deployment
    1. Create a new Heroku app
    2. Create requirements.txt file
    3. Create a Procfile
    4. Git add and git commit code
    5. Git push to Github
