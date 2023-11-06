from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)

class ReviewForm(FlaskForm):
    course_name = StringField('Course Name', validators=[DataRequired()])
    review_text = TextAreaField('Review', validators=[DataRequired()])
    submit = SubmitField('Save Review')


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(200), nullable=False)
    reviews = db.relationship('Review', backref='course', lazy=True)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    review_text = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)  # for sorting by year
    # ... other fields for the review

@app.route('/courses')
def courses():
    courses = Course.query.all()  # Fetch all courses from the database
    return render_template('courses.html', courses=courses)  # Send them to the template for rendering

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ReviewForm()
    if form.validate_on_submit():
        new_review = Review(course_name=form.course_name.data, review_text=form.review_text.data)
        db.session.add(new_review)
        db.session.commit()
        flash('Review added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('reviews.html', form=form)

@app.route('/all_reviews')
def all_reviews():
    reviews = Review.query.all()
    return render_template('all_reviews.html', reviews=reviews)

if __name__ == '__main__':
    app.run(debug=True)