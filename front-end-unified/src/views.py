from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/review')
def review():
    return "<h1>Course Reviews Page</h1>"

@views.route('/culture')
def culture():
    return "<h1>Cultural Credits Opportunity Tracker</h1>"