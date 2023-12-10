from flask import Flask, Blueprint, render_template, redirect, url_for
from flask import flash, request

from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length

from datetime import datetime

import mysql.connector

# from weblet import rootPath, passwordTA, passwordTC, app
def ourPaths():
    """
    ourPaths() must be placed at the beginning of the file 
    in order for the site to build and run.
    
    ourPaths() must be called immediately after it ends.
    
    Purpose: Initializes necessary variable for web app.
    """
    import os

    global rootPath
    rootPath = os.path.abspath(os.getcwd())

    global passwordTA
    global passwordTC
    pwFile = (rootPath + "\\Misc_Folder\\SQL\\TA_ourPySQL.txt")
    with open(pwFile, 'r') as passFile:
        passwordTA = passFile.readline()
    pwFile = (rootPath + "\\Misc_Folder\\SQL\\TC_ourPySQL.txt")
    with open(pwFile, 'r') as passFile:
        passwordTC = passFile.readline()
        # Password for the databases gets read from a file, so
        # that it is not explicitly stored here in the code.
        # MySQL Injections are scary.

    print("Loading '/Course-Reviews'...")
ourPaths() # Must be placed at beginning of file.


# app.register_blueprint(courseReviews_bp, url_prefix='/course-reviews')
courseReviews_bp = Blueprint('courseReviews', __name__,
                  root_path = rootPath,
                  template_folder= rootPath + "/front-end/src/Course_Reviews/templates",
                  static_folder= rootPath + "/front-end/src/static")

courseReviews_Flask = Flask('courseReviews')

courseReviews_Flask.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
courseReviews_Flask.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(courseReviews_Flask)

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


@courseReviews_bp.route('/course-review', methods=['GET', 'POST'])
def courseReview():
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

@courseReviews_bp.route('/course-selection', methods=['GET', 'POST'])
def courseSelection():
    try:
        courses = list()

        progress = mysql.connector.connect(
            host="174.138.53.254",
            user="TheAuditor",
            password=passwordTA,
            database="progress"
        )
        myProgress = progress.cursor(prepared=True)
        data = "qualityPoints"
        sql_query = """SELECT courseTitle FROM `800737736` WHERE qualityPoints IS NOT NULL;"""
        myProgress.execute(sql_query)
        myResult = myProgress.fetchall()

        for x in myResult:
            courses.append(x)
            print(x)
        if request.method == 'POST':
            selected_course = request.form['course_name']
            return render_template('reviews.html', course=selected_course)
        else:
            return render_template('course_selection.html', courses=courses)

    except mysql.connector.Error as error:
        print("query failed {}".format(error))

    finally:
        if progress.is_connected():
            myProgress.close()
            progress.close()
            print("MySQL connection is closed.")
    return render_template('course_selection.html', courses=courses)








# #COURSE REVIEWS
# @views.route('/review')
# def review():
#     return render_template("Review/course_selection.html")

# @views.route('/courses')
# def courses():
#     courses = Course.query.all()
#     return render_template('Review/reviews.html', courses=courses)

# @views.route('/all_reviews')
# def all_reviews():
#     reviews = Review.query.all()
#     return render_template('Review/all_reviews.html', reviews=reviews)

# @views.route('/select_course')
# def select_course():
#     return render_template('Review/course_selection.html')

# @views.route('/review_form', methods=['POST'])
# def review_form():
#     selected_course = request.form['course_name']
#     # Do something with the selected course, like render a new template
#     return render_template('Review/review_form.html', course=selected_course)

# @views.route('/submit_review', methods=['POST'])
# def submit_review():
#     form = ReviewForm(request.form)
#     if form.validate_on_submit():
#         try:
#             # Assuming you have logic to get or handle the course_id appropriately
#             course_id = course_selection.html  # Replace with actual logic to handle course_id

#             new_review = Review(
#                 course_id=course_id,
#                 review_text=form.review_text.data,
#                 # ... other fields ...
#             )
#             db.session.add(new_review)
#             db.session.commit()

#             # Save the review to a file
#             with open("reviews.txt", "a") as file:
#                 file.write(f"Course ID: {new_review.course_id}\n")
#                 file.write(f"Review Text: {new_review.review_text}\n")
#                 file.write("------\n")

#             flash('Review submitted successfully!', 'success')
#         except Exception as e:
#             # If an error occurs, log it and flash a message
#             flash(f'An error occurred: {str(e)}', 'error')

#         return redirect(url_for('index'))

#     # If the form is not valid or it's a GET request, render the form again
#     return render_template('reviews.html', form=form)

# @views.route('/download_reviews')
# def download_reviews():
#     directory = os.path.dirname(os.path.abspath(__file__))
#     return send_from_directory(directory, "reviews.txt", as_attachment=True)

# @views.route('/reviews/<int:course_id>')
# def show_reviews(course_id):
#     course = Course.query.get(course_id)
#     if course is None:
#         flash('Course not found!', 'error')
#         return redirect(url_for('index'))
    
#     reviews = Review.query.filter_by(course_id=course_id).all()
#     return render_template('course_reviews.html', course=course, reviews=reviews)
