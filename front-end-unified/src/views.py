from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/review')
def review():
    return render_template("review.html")

@views.route('/culture')
def culture():
    return render_template("culture.html")