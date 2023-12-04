from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length
from datetime import datetime
from flask import send_from_directory

import mysql.connector
import os
rootPath = os.path.abspath(os.getcwd())

# pwFile = (rootPath + "\\ourPySQL.txt")
pwFile = (rootPath + "\\Misc_Folder\\SQL\\ourPySQL.txt")
with open(pwFile, 'r') as passFile:
    password = passFile.readline()
    # Password for the databases gets read from a file, so
    # that it is not explicitly stored here in the code.
    # Also, the databases are currently located locally on 
    # my machine (Alexander G.) and I do not feel inclined 
    # to allowing the entire world have free root access to 
    # my computer's databases. MySQL Injections are scary.

catalog = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password,
    database="catalog"
)
reviews = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password,
    database="reviews"
)
myCatalog = catalog.cursor(prepared=True)
myReviews = reviews.cursor(prepared=True)


app = Flask(
    __name__,
    root_path=(rootPath),
    template_folder= rootPath + "/back-end/Sydney/CourseReviewApp/templates",
    static_folder= rootPath + "/back-end/Sydney/CourseReviewApp/static")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)



class Course(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(200), unique=True, nullable=False)
    reviews     = db.relationship('Review', backref='course', lazy=True)
    # id = db.Column(db.Integer, primary_key=True)
    # course_name = db.Column(db.String(200), unique=True, nullable=False)
    # reviews = db.relationship('Review', backref='course', lazy=True)

class Review(db.Model):
    id                 = db.Column(db.Integer, primary_key=True)
    course_id          = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    review_text        = db.Column(db.Text, nullable=False)
    professor_feedback = db.Column(db.Text, nullable=True)
    course_load        = db.Column(db.Text, nullable=True)
    quizzes_tests      = db.Column(db.Text, nullable=True)
    timestamp          = db.Column(db.DateTime, default=datetime.utcnow)
    # id = db.Column(db.Integer, primary_key=True)
    # course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    # review_text = db.Column(db.Text, nullable=False)
    # professor_feedback = db.Column(db.Text, nullable=True)
    # course_load = db.Column(db.Text, nullable=True)
    # quizzes_tests = db.Column(db.Text, nullable=True)
    # timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    # New fields
    instructor_notes_online       = db.Column(db.String(3))
    instructor_offer_extra_credit = db.Column(db.String(3))
    instructor_flexibility        = db.Column(db.String(15))
    instructor_demeanor           = db.Column(db.String(250))
    # instructor_notes_online = db.Column(db.String(3))
    # instructor_offer_extra_credit = db.Column(db.String(3))
    # instructor_flexibility = db.Column(db.String(15))
    # instructor_demeanor = db.Column(db.String(250))
    # Add other new fields as needed...

class ReviewForm(FlaskForm):
    course_name        = StringField('Course Name:', validators=[DataRequired()])
    review_text        = TextAreaField('Overall Course Review:', validators=[DataRequired()])
    professor_rate     = RadioField('Please rate the Professor:', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    professor_feedback = TextAreaField('What did you think of the Professor:', validators=[DataRequired()])
    course_load        = TextAreaField('Describe the course load:', validators=[DataRequired()])
    quizzes_tests      = TextAreaField('Describe quizzes/tests (if any):', validators=[DataRequired()])
    submit             = SubmitField('Submit Review')
    # course_name = StringField('Course Name:', validators=[DataRequired()])
    # review_text = TextAreaField('Overall Course Review:', validators=[DataRequired()])
    # professor_rate = RadioField('Please rate the Professor:', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    # professor_feedback = TextAreaField('What did you think of the Professor:', validators=[DataRequired()])
    # course_load = TextAreaField('Describe the course load:', validators=[DataRequired()])
    # quizzes_tests = TextAreaField('Describe quizzes/tests (if any):', validators=[DataRequired()])
    # submit = SubmitField('Submit Review')

    # New form fields
    instructor_notes_online       = RadioField('Does the instructor post the class notes online?', choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')])
    instructor_offer_extra_credit = RadioField('Does the instructor offer extra credit?', choices=[('Yes', 'Yes'), ('No', 'No')])
    instructor_flexibility        = RadioField('The instructor is flexible when it comes to unforeseen circumstances:', choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree'), ('N/A', 'N/A')])
    instructor_demeanor           = TextAreaField('What was the professor\'s demeanor like?', validators=[Length(max=250)])
    # instructor_notes_online = RadioField('Does the instructor post the class notes online?', choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')])
    # instructor_offer_extra_credit = RadioField('Does the instructor offer extra credit?', choices=[('Yes', 'Yes'), ('No', 'No')])
    # instructor_flexibility = RadioField('The instructor is flexible when it comes to unforeseen circumstances:', choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree'), ('N/A', 'N/A')])
    # instructor_demeanor = TextAreaField('What was the professor\'s demeanor like?', validators=[Length(max=250)])
    # Add other new form fields as needed...

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ReviewForm()
    if form.validate_on_submit():
        rating = form.professor_rate.data
        course = Course.query.filter_by(course_name=form.course_name.data).first()
        if not course:
            flash('Course not found! Please add the course before submitting a review.', 'error')
            return redirect(url_for('index'))
        
        new_review = Review(
            course_id=course.id,
            review_text=form.review_text.data,
            professor_feedback=form.professor_feedback.data,
            course_load=form.course_load.data,
            quizzes_tests=form.quizzes_tests.data,
            instructor_notes_online=form.instructor_notes_online.data,
            instructor_offer_extra_credit=form.instructor_offer_extra_credit.data,
            instructor_flexibility=form.instructor_flexibility.data,
            instructor_demeanor=form.instructor_demeanor.data
            # Assign other new fields here...
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

@app.route('/select_course')
def select_course():
    return render_template('course_selection.html')

@app.route('/review_form', methods=['POST'])
def review_form():
    selected_course = request.form['course_name']
    # Do something with the selected course, like render a new template
    return render_template('review_form.html', course=selected_course)

@app.route('/course_selection', methods=['GET', 'POST'])
def course_selection():
    if request.method == 'POST':
        selected_course = request.form['course_name']
        return render_template('reviews.html', course=selected_course)
    return render_template('course_selection.html')

@app.route('/submit_review', methods=['POST'])
def submit_review():
    form = ReviewForm(request.form)
    if form.validate_on_submit():
        try:
            # Assuming you have logic to get or handle the course_id appropriately
            course_id = course_selection.html  # Replace with actual logic to handle course_id

            new_review = Review(
                course_id=course_id,
                review_text=form.review_text.data,
                # ... other fields ...
            )
            db.session.add(new_review)
            db.session.commit()

            # Save the review to a file
            with open("reviews.txt", "a") as file:
                file.write(f"Course ID: {new_review.course_id}\n")
                file.write(f"Review Text: {new_review.review_text}\n")
                file.write("------\n")

            flash('Review submitted successfully!', 'success')
        except Exception as e:
            # If an error occurs, log it and flash a message
            flash(f'An error occurred: {str(e)}', 'error')

        return redirect(url_for('index'))

    # If the form is not valid or it's a GET request, render the form again
    return render_template('reviews.html', form=form)



@app.route('/download_reviews')
def download_reviews():
    directory = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(directory, "reviews.txt", as_attachment=True)



@app.route('/reviews/<int:course_id>')
def show_reviews(course_id):
    course = Course.query.get(course_id)
    if course is None:
        flash('Course not found!', 'error')
        return redirect(url_for('index'))
    
    reviews = Review.query.filter_by(course_id=course_id).all()
    return render_template('course_reviews.html', course=course, reviews=reviews)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    # app.run(host='192.168.1.46', port=3000, debug=True)
    app.run(host='127.0.0.1', port=3000, debug=True)
