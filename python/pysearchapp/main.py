from flask import Flask
from flask import Blueprint
# connection to mongodb
from .extensions import mongo


# for mapping data to mongoDb
main = Blueprint('main', __name__)

@main.route('/')
def index():
    user_collection = mongo.db.users
    user_collection.insert({'name': 'Annie'})
    return '<h1>Added a user</h1>'

# @ flask server app to connect to express
# TODO send form data to this location to load it into the database
@main.route('/flask', methods=['GET'])
def flask():
    # deal with form data here
    return "Flask Server"

if __name__ == "__main__":
    app.run(port=5000, debug=True)
