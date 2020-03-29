import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'projectDB'
app.config["MONGO_URI"] = os.getenv('MONGO_URI','mongodb+srv://root:r00tUser@myFirstCluster-yilmx.mongodb.net/projectDB?retryWrites=true&w=majority')

mongo = PyMongo(app)


@app.route('/')
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


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
