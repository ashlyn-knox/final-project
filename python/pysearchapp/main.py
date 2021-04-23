from flask import Flask, render_template
from flask import Blueprint
from .extensions import mongo

# for mapping data to mongoDb
main = Blueprint('main', __name__)

# @ flask server app to connect to express
@main.route('/flask', methods=['GET'])
def flask():
    # deal with form data here
    return "This page is hosted on flask"

if __name__ == "__main__":
    app.run(port=5000, debug=True)
