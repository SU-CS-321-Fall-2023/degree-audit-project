from flask import Flask

from src.APT.progressTracker import progressTracker_bp
from src.Course_Registration.courseRegistration import courseRegistration_bp
from src.Course_Reviews.courseReviews import courseReviews_bp
from src.Course_Search.courseSearch import courseSearch_bp
from src.Cultural_Credits.culturalCredits import culturalCredits_bp
from src.Errors.errors import errors_bp
from src.Home.home import home_bp

app = Flask(__name__,
            root_path = rootPath,
            # template_folder= rootPath + "/front-end/src/templates",
            static_folder= rootPath + "/front-end/src/static")
app.config['SECRET_KEY'] = 'hai'


app.register_blueprint(progressTracker_bp, url_prefix='/APT')
app.register_blueprint(courseRegistration_bp, url_prefix='/course-registration')
app.register_blueprint(courseReviews_bp, url_prefix='/course-reviews')
app.register_blueprint(courseSearch_bp, url_prefix='/course-search')
app.register_blueprint(culturalCredits_bp, url_prefix='/cultural-credits')

app.register_blueprint(errors_bp, url_prefix='/error')
app.register_blueprint(home_bp, url_prefix='/')





# from werkzeug.utils import secure_filename
# from flask import Flask, jsonify, redirect, url_for, send_from_directory
# import csv
from flask import render_template, request, redirect, send_from_directory, url_for
from flask import flash, request
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length

from datetime import datetime

from flask_cors import CORS
import os
import mysql.connector

from src import create_app

def ourPaths():
    """
    ourPaths() must be placed at the beginning of the file 
    in order for the site to build and run.
    
    ourPaths() must be called immediately after it ends.
    
    Purpose: Initializes necessary variable for web app.
    """
    global rootPath
    rootPath = os.path.abspath(os.getcwd())
    print(f"rootPath: {rootPath}")
    
    # global webletIndex
    # webletIndex =  "index.html"
    
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
ourPaths()# Must be placed at beginning of file.

# Connections to the MySQL Databases
# catalog = mysql.connector.connect(
#     host="174.138.53.254",
#     user="TheAuditor",
#     password=passwordTA,
#     database="catalog"
# )
# reviews = mysql.connector.connect(
#     host="174.138.53.254",
#     user="TheAuditor",
#     password=passwordTA,
#     database="reviews"
# )
# myCatalog = catalog.cursor(prepared=True)
# myReviews = reviews.cursor(prepared=True)

app = create_app()
# cors = CORS(app)
# Configure the value of the "origins" key to be the actual URL of the React Frontend.
# Make sure to NOT have a / at the end of the "origins" URL.
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:*"}})

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

@app.errorhandler(404)
def page_not_found(e):
    # if a page does not exist
    if request.path.startswith('/'):
        # we return a generic 404 page
        return render_template("Errors/404.html"), 404
    else:
        # otherwise we return a generic 404 page
        return render_template("Errors/404.html"), 404
@app.errorhandler(405)
def method_not_allowed(e):
    # if a request has the wrong method to our API
    if request.path.startswith('/'):
        # we return a generic 405 page
        return render_template("Errors/405.html"), 405
    else:
        # otherwise we return a generic 405 page
        return render_template("Errors/405.html"), 405



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("Request Method = POST")
    else:
        print("Request Method = GET")
    return render_template('index.html')
# @app.route('/Review', methods=['GET', 'POST'])
# def reviewal():
#     if request.method == 'POST':
#         print("Request Method = POST")
#     else:
#         print("Request Method = GET")
#     return render_template('index.html')

# @app.route('/idForm', methods=['POST'])
# def idForm():
#     try:
#         courses_data = list()

#         studentID    = request.form['student_id']
#         # studentEmail = request.form['student_email']
#         print(studentID)

#         students = mysql.connector.connect(
#             host="174.138.53.254",
#             user="TheAuditor",
#             password=passwordTA,
#             database="students"
#         )
#         myStudents = students.cursor(prepared=True)
#         myStudents.execute(f"CALL sys.table_exists('students', '{studentID}', @exists); SELECT @exists;")
#         # sql_query = """SELECT studentID FROM students.students WHERE studentID=%s ;"""
#         # myStudents.execute(sql_query,studentID)
#         myResult = myStudents.fetchall()

#         for x in myResult:
#             courses_data.append(x)
#         return render_template('APT/progress_tracker.html', courses=courses_data)

#     except mysql.connector.Error as error:
#         print("query failed {}".format(error))

#     finally:
#         if students.is_connected():
#             myStudents.close()
#             students.close()
#             print("MySQL connection is closed.")



@app.route('/course-registration')
def courseRegistration():
    return render_template('Registration/course_registration.html')

@app.route('/course-search')
def courseSearch():
    return render_template('Course-Search/course_search.html')

@app.route('/course-review', methods=['GET', 'POST'])
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
    return render_template('Review/reviews.html', form=form)

@app.route('/Review/course-selection', methods=['GET', 'POST'])
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
            return render_template('Review/reviews.html', course=selected_course)
        else:
            return render_template('Review/course_selection.html', courses=courses)

    except mysql.connector.Error as error:
        print("query failed {}".format(error))

    finally:
        if progress.is_connected():
            myProgress.close()
            progress.close()
            print("MySQL connection is closed.")
    return render_template('Review/course_selection.html', courses=courses)


@app.route('/culture')
def culture():
    return render_template('Cultural-Credits/culture.html')

@app.route('/APT/progress-tracker')
def progressTracker():
    try:
        courses_data = list()

        progress = mysql.connector.connect(
            host="174.138.53.254",
            user="TheAuditor",
            password=passwordTA,
            database="progress"
        )
        myProgress = progress.cursor(prepared=True)
        sql_query = """SELECT `id`, `courseNumber`, `subject`, `courseReferenceNumber`, `courseTitle`, `campusCode`, `termDescription`, `gpaHours`, `hoursAttempted`, `hoursEarned`, `midtermGrade`, `finalGrade`, `qualityPoints` FROM `800737736` ; """
        myProgress.execute(sql_query)
        myResult = myProgress.fetchall()

        for x in myResult:
            courses_data.append(x)
        return render_template('progress_tracker.html', courses=courses_data)

    except mysql.connector.Error as error:
        print("query failed {}".format(error))

    finally:
        if progress.is_connected():
            myProgress.close()
            progress.close()
            print("MySQL connection is closed.")


if __name__ == '__main__':
    """
    Must be placed at the end of the file.
    """
    # app.run(host = '192.168.1.46', port = 3000, debug = True)
    # app.run(host = '127.0.0.1', port = 3000, debug = True)
    app.run(host = '127.0.0.1', port = 9000, debug=True)
    # app.run(host= "174.138.53.254" , port = 9000, debug = True)





# # def allowed_file(filename):
# #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# # ALLOWED_EXTENSIONS = {'csv'}
# # class Index(Resource):
#     # def get(self):
#     #     data = []
#     #     # render_template(webletIndex, data=data)
#     #     return jsonify(render_template(webletIndex, data=data))
#     # def post(self):
#     #     data = request.get_json()
#     #     return jsonify({'data': data}), 201


# # @app.route("/index")
# # def index():
# #     return render_template(webletIndex)


# # @app.route('/data')
# # def database():
# #     return 'data'


# # @app.route('/', methods=['GET', 'POST'])
# # def index():
# #     # data = []  # A list to hold our CSV data

# #     # # Use raw string notation for the path or double up the backslashes
# #     # userCSV_path = rootPath + '\\front-end\\src\\user.csv'
# #     # reqsCSV_path = rootPath + r'\\reqs.csv'
# #     # testCSV_path = rootPath + r'\\test.csv'

# #     if request.method == 'POST':
# #         email = request.form.get('student_email', None)  # Fetch the major entered by the user

# #     #     # Read the predefined CSV file and store the data
# #     #     #with open(userCSV_path, 'r') as f:
# #     #      #   reader = csv.reader(f)
# #     #       #  data = [row for row in reader]

# #     #     # Filter the data based on the major if one is entered
# #     #     #if email:
# #     #         # Assuming the major is in the 2nd column (index 1). Adjust the index if needed.
# #     #      #   data = [data[0]] + [row for row in data[1:] if email.lower() in row[1].lower()]
# #     else:
# #         print("else Statement has been reached for /api/index.")
# #     #     # print("GET method has been used for /api/index .")

# #     return render_template("index.html")
# #     # return render_template("index.html", data=data)


# # @app.route('/api/data')
# # def get_data():
# #     data = {'message': 'Hello from the Flask API!'}
# #     return jsonify(data)


# # Sydney's log
#     # csv_path = rootPath + r'\\Academic Programs - Stetson University.csv'
#     #r'C:\Users\sydne\OneDrive - Stetson University, Inc\Desktop\Computer Science\Python\DegreeAudit.Databasefinal.csv'
#     #r'C:\Users\sydne\OneDrive - Stetson University, Inc\Desktop\Computer Science\Python\DegreeAudit.Database.csv'
#     #r'C:\Users\sydne\OneDrive - Stetson University, Inc\Desktop\Computer Science\Python\Academic_Programs_-_Stetson_University.csv'

#     # if request.method == 'POST':
#     #     major = request.form.get('major', None)  # Fetch the major entered by the user

#     #     # Read the predefined CSV file and store the data
#     #     with open(csv_path, 'r') as f:
#     #         reader = csv.reader(f)
#     #         data = [row for row in reader]

#     #     # Filter the data based on the major if one is entered
#     #     if major:
#     #         # Assuming the major is in the 2nd column (index 1). Adjust the index if needed.
#     #         data = [data[0]] + [row for row in data[1:] if major.lower() in row[1].lower()]

#     # return render_template(webletIndex, data=data)
