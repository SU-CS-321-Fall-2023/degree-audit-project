from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>Homepage</h1>"

@views.route('/reviews')
def reviews():
    return "<h1>Course Reviews Page</h1>"

@views.route('/cultural')
def culture():
    return "<h1>Cultural Credits Opportunity Tracker</h1>"