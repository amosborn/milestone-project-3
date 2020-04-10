import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists('env.py'):
    import env


app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'projectDB'
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')


mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_reviews', methods=['GET', 'POST'])
def get_reviews():
    """Get user's review"""
    email = request.args.get('email')
    user = mongo.db.users.find_one({'email': email})
    if user:
        for k, v in user.items():
            if k == 'username':
                username = v
        results = mongo.db.reviews.find({'username': {'$regex': username}})
        return render_template('reviews.html', reviews=results, username=username)
    else:
        flash('Email not found, would you like to sign up?')
        return render_template('index.html')


@app.route('/add_user')
def add_user():
    """Form to create user"""
    return render_template('adduser.html')


@app.route('/insert_user', methods=['POST'])
def insert_user():
    """Add user to the database"""
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        used_email = mongo.db.users.find_one({'email': email})
        used_username = mongo.db.users.find_one({'username': username})
        if used_username is not None:
            flash('Username already taken, please choose another.')
            return render_template('adduser.html')
        elif used_email is not None:
            flash('Email already registered, would you like to sign in?')
            return render_template('index.html')
        else:
            users = mongo.db.users
            users.insert_one(request.form.to_dict())
    return redirect(url_for('add_review'))


@app.route('/add_review')
def add_review():
    """Form to create review"""
    return render_template('addreview.html')


@app.route('/insert_review', methods=['POST'])
def insert_review():
    """Add review to the database"""
    if request.method == 'POST':
        reviews = mongo.db.reviews
        reviews.insert_one(request.form.to_dict())
        username = request.form.get('username')
        results = mongo.db.reviews.find({'username': {'$regex': username}})
    return render_template('reviews.html', reviews=results, username=username)


@app.route('/edit_review/<review_id>')
def edit_review(review_id):
    """Form to edit review"""
    the_review = mongo.db.reviews.find_one({'_id': ObjectId(review_id)})
    return render_template('editreview.html', review=the_review)


@app.route('/update_review/<review_id>', methods=['POST'])
def update_review(review_id):
    """Add edited review to database"""
    reviews = mongo.db.reviews
    reviews.update({'_id': ObjectId(review_id)},
    {
        'username': request.form.get('username'),
        'title': request.form.get('title'),
        'author': request.form.get('author'),
        'category': request.form.get('category'),
        'rating': request.form.get('rating'),
        'cover': request.form.get('cover'),
        'review': request.form.get('review')
    })
    username = request.form.get('username')
    results = mongo.db.reviews.find({'username': {'$regex': username}})
    return render_template('reviews.html', reviews=results, username=username)


@app.route('/delete_review/<review_id>')
def delete_review(review_id):
    """Delete selected review"""
    mongo.db.reviews.remove({'_id': ObjectId(review_id)})
    return redirect(url_for('get_reviews'))


@app.route('/search')
def search():
    """Search form"""
    return render_template('findreviews.html')


@app.route('/find_reviews')
def find_reviews():
    """Search from form input"""
    query = request.args.get('query')
    searchby = request.args.get('searchby')
    results = mongo.db.reviews.find({searchby: {'$regex': query}})
    return render_template('searchresults.html', reviews=results)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
