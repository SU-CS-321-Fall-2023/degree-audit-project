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

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(200), unique=True, nullable=False)
    reviews = db.relationship('Review', backref='course', lazy=True)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    review_text = db.Column(db.Text, nullable=False)
    professor_feedback = db.Column(db.Text, nullable=True)
    course_load = db.Column(db.Text, nullable=True)
    quizzes_tests = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class ReviewForm(FlaskForm):
    course_name = StringField('Course Name', validators=[DataRequired()])
    review_text = TextAreaField('Overall Course Review', validators=[DataRequired()])
    professor_feedback = TextAreaField('What did you think of the Professor', validators=[DataRequired()])
    course_load = TextAreaField('Describe the course load', validators=[DataRequired()])
    quizzes_tests = TextAreaField('Describe quizzes/tests (if any)', validators=[DataRequired()])
    submit = SubmitField('Submit Review')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ReviewForm()
    if form.validate_on_submit():
        course = Course.query.filter_by(course_name=form.course_name.data).first()
        if not course:
            flash('Course not found! Please add the course before submitting a review.', 'error')
            return redirect(url_for('index'))
        
        new_review = Review(
            course_id=course.id,
            review_text=form.review_text.data,
            professor_feedback=form.professor_feedback.data,
            course_load=form.course_load.data,
            quizzes_tests=form.quizzes_tests.data
        )
        db.session.add(new_review)
        db.session.commit()
        flash('Review added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('reviews.html', form=form)

@app.route('/courses')
def courses():
    courses = Course.query.all()
    return render_template('reviews.html', courses=courses)

@app.route('/all_reviews')
def all_reviews():
    reviews = Review.query.all()
    return render_template('all_reviews.html', reviews=reviews)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Make sure to create the database tables before running the app
    app.run(debug=True)
