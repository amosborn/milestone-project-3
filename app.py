import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'projectDB'
app.config["MONGO_URI"] = os.getenv('MONGO_URI','mongodb+srv://root:r00tUser@myFirstCluster-yilmx.mongodb.net/projectDB?retryWrites=true&w=majority')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_books')
def get_books():
    return render_template('books.html', books=mongo.db.books.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
