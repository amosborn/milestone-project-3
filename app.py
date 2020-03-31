import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'projectDB'
app.config["MONGO_URI"] = os.getenv('MONGO_URI','mongodb+srv://root:r00tUser@myFirstCluster-yilmx.mongodb.net/projectDB?retryWrites=true&w=majority')

mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_reviews')
def get_reviews():
    return render_template('reviews.html', reviews=mongo.db.reviews.find())


@app.route('/get_users')
def get_users():
    return render_template('users.html', users=mongo.db.users.find())


@app.route('/add_user')
def add_user():
    return render_template('adduser.html')


@app.route('/insert_user', methods=['POST'])
def insert_user():
    users = mongo.db.users
    users.insert_one(request.form.to_dict())
    return redirect(url_for('add_review'))


@app.route('/add_review')
def add_review():
    return render_template('addreview.html')


@app.route('/insert_review', methods=['POST'])
def insert_review():
    reviews = mongo.db.reviews
    reviews.insert_one(request.form.to_dict())
    return redirect(url_for('get_reviews'))


@app.route('/edit_review/<review_id>')
def edit_review(review_id):
    the_review = mongo.db.reviews.find_one({'_id': ObjectId(review_id)})
    return render_template('editreview.html', review=the_review)


@app.route('/update_review/<review_id>', methods=['POST'])
def update_review(review_id):
    reviews = mongo.db.reviews
    reviews.update({'_id': ObjectId(review_id)},
    {
        'email': request.form.get('email'),
        'title': request.form.get('title'),
        'author': request.form.get('author'),
        'category': request.form.get('category'),
        'rating': request.form.get('rating'),
        'cover': request.form.get('cover'),
        'review': request.form.get('review')
    })
    return redirect(url_for('get_reviews'))


@app.route('/delete_review/<review_id>')
def delete_review(review_id):
    mongo.db.reviews.remove({'_id': ObjectId(review_id)})
    return redirect(url_for('get_reviews'))    


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
