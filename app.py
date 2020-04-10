import os
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'projectDB'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://root:r00tUser@myFirstCluster-yilmx.mongodb.net/projectDB?retryWrites=true&w=majority')
app.secret_key = 'secretkey123'


mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_reviews', methods=['GET', 'POST'])
def get_reviews():
    email = request.args.get('email')
    user = mongo.db.users.find_one({'email': email})
    if user:
        for k, v in user.items():
            if k == 'username':
                username = v
        results = mongo.db.reviews.find({"username": {"$regex": username}})
        return render_template('reviews.html', reviews=results, username=username)
    else:
        flash('Email not found, would you like to sign up?')
        return render_template('index.html')

    if request.method == 'POST':
        session['username'] = username


@app.route('/get_users')
def get_users():
    return render_template('users.html', users=mongo.db.users.find())


@app.route('/add_user')
def add_user():
    return render_template('adduser.html')


@app.route('/insert_user', methods=['POST'])
def insert_user():
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
    return render_template('addreview.html')


@app.route('/insert_review', methods=['POST'])
def insert_review():
    if request.method == 'POST':
        reviews = mongo.db.reviews
        reviews.insert_one(request.form.to_dict())
        username = request.form.get('username')
        results = mongo.db.reviews.find({'username': {'$regex': username}})
    return render_template('reviews.html', reviews=results, username=username)


@app.route('/edit_review/<review_id>')
def edit_review(review_id):
    the_review = mongo.db.reviews.find_one({'_id': ObjectId(review_id)})
    return render_template('editreview.html', review=the_review)


@app.route('/update_review/<review_id>', methods=['POST'])
def update_review(review_id):
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
    mongo.db.reviews.remove({'_id': ObjectId(review_id)})
    return redirect(url_for('get_reviews'))


@app.route('/search')
def search():
    return render_template('findreviews.html')


@app.route('/find_reviews')
def find_reviews():
    query = request.args.get('query')
    searchby = request.args.get('searchby')
    results = mongo.db.reviews.find({searchby: {"$regex": query}})
    return render_template('searchresults.html', reviews=results)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
