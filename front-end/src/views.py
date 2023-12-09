from flask import Blueprint, render_template, redirect, send_from_directory, url_for
from flask import flash, request

from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length

from datetime import datetime

import mysql.connector
import os
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

views = Blueprint('views', __name__,
                  root_path = rootPath,
                  template_folder= rootPath + "/front-end/src/templates",
                  static_folder= rootPath + "/front-end/src/static")


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

# views.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
# views.config['SECRET_KEY'] = 'your_secret_key'

# db = SQLAlchemy(views)

# class Course(db.Model):
#     id          = db.Column(db.Integer, primary_key=True)
#     course_name = db.Column(db.String(200), unique=True, nullable=False)
#     reviews     = db.relationship('Review', backref='course', lazy=True)
#     # id = db.Column(db.Integer, primary_key=True)
#     # course_name = db.Column(db.String(200), unique=True, nullable=False)
#     # reviews = db.relationship('Review', backref='course', lazy=True)

# class Review(db.Model):
#     id                 = db.Column(db.Integer, primary_key=True)
#     course_id          = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
#     review_text        = db.Column(db.Text, nullable=False)
#     professor_feedback = db.Column(db.Text, nullable=True)
#     course_load        = db.Column(db.Text, nullable=True)
#     quizzes_tests      = db.Column(db.Text, nullable=True)
#     timestamp          = db.Column(db.DateTime, default=datetime.utcnow)
#     # id = db.Column(db.Integer, primary_key=True)
#     # course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
#     # review_text = db.Column(db.Text, nullable=False)
#     # professor_feedback = db.Column(db.Text, nullable=True)
#     # course_load = db.Column(db.Text, nullable=True)
#     # quizzes_tests = db.Column(db.Text, nullable=True)
#     # timestamp = db.Column(db.DateTime, default=datetime.utcnow)

#     # New fields
#     instructor_notes_online       = db.Column(db.String(3))
#     instructor_offer_extra_credit = db.Column(db.String(3))
#     instructor_flexibility        = db.Column(db.String(15))
#     instructor_demeanor           = db.Column(db.String(250))
#     # instructor_notes_online = db.Column(db.String(3))
#     # instructor_offer_extra_credit = db.Column(db.String(3))
#     # instructor_flexibility = db.Column(db.String(15))
#     # instructor_demeanor = db.Column(db.String(250))
#     # Add other new fields as needed...

# class ReviewForm(FlaskForm):
#     course_name        = StringField('Course Name:', validators=[DataRequired()])
#     review_text        = TextAreaField('Overall Course Review:', validators=[DataRequired()])
#     professor_rate     = RadioField('Please rate the Professor:', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
#     professor_feedback = TextAreaField('What did you think of the Professor:', validators=[DataRequired()])
#     course_load        = TextAreaField('Describe the course load:', validators=[DataRequired()])
#     quizzes_tests      = TextAreaField('Describe quizzes/tests (if any):', validators=[DataRequired()])
#     submit             = SubmitField('Submit Review')
#     # course_name = StringField('Course Name:', validators=[DataRequired()])
#     # review_text = TextAreaField('Overall Course Review:', validators=[DataRequired()])
#     # professor_rate = RadioField('Please rate the Professor:', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
#     # professor_feedback = TextAreaField('What did you think of the Professor:', validators=[DataRequired()])
#     # course_load = TextAreaField('Describe the course load:', validators=[DataRequired()])
#     # quizzes_tests = TextAreaField('Describe quizzes/tests (if any):', validators=[DataRequired()])
#     # submit = SubmitField('Submit Review')

#     # New form fields
#     instructor_notes_online       = RadioField('Does the instructor post the class notes online?', choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')])
#     instructor_offer_extra_credit = RadioField('Does the instructor offer extra credit?', choices=[('Yes', 'Yes'), ('No', 'No')])
#     instructor_flexibility        = RadioField('The instructor is flexible when it comes to unforeseen circumstances:', choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree'), ('N/A', 'N/A')])
#     instructor_demeanor           = TextAreaField('What was the professor\'s demeanor like?', validators=[Length(max=250)])
#     # instructor_notes_online = RadioField('Does the instructor post the class notes online?', choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')])
#     # instructor_offer_extra_credit = RadioField('Does the instructor offer extra credit?', choices=[('Yes', 'Yes'), ('No', 'No')])
#     # instructor_flexibility = RadioField('The instructor is flexible when it comes to unforeseen circumstances:', choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree'), ('N/A', 'N/A')])
#     # instructor_demeanor = TextAreaField('What was the professor\'s demeanor like?', validators=[Length(max=250)])
#     # Add other new form fields as needed...





default_interests = ["Computer Science", "Psychology", "Biology", "Mathematics", "Chemistry", "Cybersecurity"]
selected_interests = []


# #ROUTING FUNCTIONS
# def generate_course_recommendations(interests):
#     recommended_courses = []
#     for interest in interests:
#         if interest in course_data:
#             recommended_courses.extend(course_data[interest])
#     return recommended_courses

# mail = Mail(views)
# def check_hold_status(student_email):
#     students = [
#         "amgarofalo@stetson.edu",
#         "rwiegner@stetson.edu",
#         "rpfoster@stetson.edu"
#     ]
#     student = students.get(student_email)

#     if student:
#         return student['has_hold']
#     else:
#         # If the student is not found in the fake database, consider them as having a hold for this example
#         app.logger.warning(f"Student with email {student_email} not found in the fake database.")
#         return True


# def send_email(to, subject, body):
#     msg = Message(subject, sender="pshelly@stetson.edu", recipients=[to], body=body)
#     mail.send(msg)

# @views.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         print("Request Method = POST")
#     else:
#         print("Request Method = GET")
#     return render_template('index.html')


#WEBPAGE ROUTING
@views.route('/')
def home():
    return render_template("home.html")

@views.route('/idForm', methods=['POST'])
def idForm():
    try:
        courses_data = list()

        studentID    = request.form['student_id']
        # studentEmail = request.form['student_email']
        print(studentID)
        type(str(studentID))
        data = studentID

        studentsTA = mysql.connector.connect(
            host="174.138.53.254",
            user="TheAuditor",
            password=passwordTA,
            database="progress"
        )
        # studentsTC = mysql.connector.connect(
        #     host="174.138.53.254",
        #     user="TheCreator",
        #     password=passwordTC,
        #     database="students"
        # )
        myStudentsTA = studentsTA.cursor(prepared=True)
        sql_query = f"SELECT `id`, `courseNumber`, `subject`, `courseReferenceNumber`, `courseTitle`, `campusCode`, `termDescription`, `gpaHours`, `hoursAttempted`, `hoursEarned`, `midtermGrade`, `finalGrade`, `qualityPoints` FROM `800737736` ; "
        myStudentsTA.execute(sql_query)
        myResult = myStudentsTA.fetchall()
        # print(f"myResult: {myResult}")

        for x in myResult:
            courses_data.append(x)
        return render_template('APT/progress_tracker.html', courses=courses_data)

    except mysql.connector.Error as error:
        print("query failed {}".format(error))

    finally:
        if studentsTA.is_connected():
            myStudentsTA.close()
            studentsTA.close()
            print("MySQL connection (TA) is closed.")
        # if studentsTC.is_connected():
        #     myStudentsTC.close()
        #     studentsTC.close()
        #     print("MySQL connection (TC) is closed.")
    return render_template('APT/progress_tracker.html', courses=courses_data)


# #Email
# #@views.route('/email')
# #def home():
# #    return render_template("email.html")

# #@views.route('/send_alert', methods=['POST'])
# #def send_alert():
# #    student_email = request.form.get('email')  # Update 'email' to match the actual name attribute in your form
# #
# #    has_hold = check_hold_status(student_email)#
# #
# #    if has_hold:
# #        flash('You have a hold on your account. Please remove it to register for classes.', 'warning')#
# #
# #        send_email(student_email, 'Hold Alert',
# #                   'You have a hold on your account. Please remove it to register for classes.')#
# #
# #    else:
# #        flash('No holds on your account. You can proceed with class registration.', 'success')
# #
# #    return redirect(url_for('index'))

# #Academic Progress <- ALEX LOOK HERE
@views.route('/progress-tracker')
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
        return render_template('APT/progress_tracker.html', courses=courses_data)

    except mysql.connector.Error as error:
        print("query failed {}".format(error))

    finally:
        if progress.is_connected():
            myProgress.close()
            progress.close()
            print("MySQL connection is closed.")

# #Interest Exploration
# @views.route('/interest')
# def interest():
#     return render_template("interest.html")
    
# @views.route('/submit', methods=['POST'])
# def submit():
#     selected_interests.clear()
#     interests_from_form = request.form.getlist('interests') or []
#     print("Interests from form:", interests_from_form)

#     selected_interests.extend(interests_from_form)

#     recommended_courses = generate_course_recommendations(selected_interests)

#     # Check if 'OTHER' is selected and handle it separately
#     if 'OTHER' in selected_interests and len(interests_from_form) > 1:
#         custom_interest = interests_from_form[interests_from_form.index('OTHER') + 1]
#         if custom_interest.lower() == 'music':
#             recommended_courses.extend(course_data['Music'])
#         elif custom_interest.lower() == 'digital arts':
#             recommended_courses.extend(course_data['Digital Arts'])
#         else:
#             recommended_courses.append(f"{custom_interest} - Introductory Course in {custom_interest}")

#     return render_template('courses.html', interests=selected_interests, courses=recommended_courses)

# #Cultural Credits
# @views.route('/culture')
# def culture():
#     # Here, you would fetch data from Stetson's Engage platform and process it to show the user's cultural credits.
#     user_cultural_credits = 24
#     credits_remaining = 10  # Change this to the remaining credits.

#     # Dummy data for cultural credit events.
#     cultural_events = [
#         {"name": "Pollination:The Art of Citizen Science", "date": "2023-24-08", "units": "1"},
#         {"name": "The Bone Wars: Museums, Fossils and National Identity ", "date": "2023-24-08", "units": "1"},
#         # Add more events here.
#     ]

#     return render_template('culture.html', credits=user_cultural_credits, remaining=credits_remaining, events=cultural_events)

# # #COURSE REVIEWS
# # @views.route('/review')
# # def review():
# #     return render_template("course_selection.html")

# # @views.route('/courses')
# # def courses():
# #     courses = Course.query.all()
# #     return render_template('reviews.html', courses=courses)

# # @views.route('/all_reviews')
# # def all_reviews():
# #     reviews = Review.query.all()
# #     return render_template('all_reviews.html', reviews=reviews)

# # @views.route('/select_course')
# # def select_course():
# #     return render_template('course_selection.html')

# # @views.route('/review_form', methods=['POST'])
# # def review_form():
# #     selected_course = request.form['course_name']
# #     # Do something with the selected course, like render a new template
# #     return render_template('review_form.html', course=selected_course)

# # @views.route('/course_selection', methods=['GET', 'POST'])
# # def course_selection():
# #     if request.method == 'POST':
# #         selected_course = request.form['course_name']
# #         return render_template('reviews.html', course=selected_course)
# #     return render_template('course_selection.html')

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

# course_data = {
#     "Computer Science": ["CSCI141 - Introduction to Computer Science I ",
#                          "CSCI142 - Introduction to Computer Science II",
#                          "CSCI201 - Introduction to Computer Organization ", "CSCI211-Discrete Structures ",
#                          "CSCI221-Software Development I ",
#                          "CSCI321 - Software Development II ", "CSCI301 - Operating Systems",
#                          "CSCI311 - Algorithm Analysis"],
#     "Psychology": ["PSYC101S - Introduction to Psychology",
#                    "PSYC203 - Foundations for Psychology Majors: Scientific Inquiry, "
#                    "Information Literacy, and Professional Dev.", "PSYC306Q - Behavioral Statistics ",
#                    "PYSC498 - Research Methods and Proposal",
#                    "Select four units from at least three of the following five Pillars:", " ---  ",
#                    "Pillar 1 - Biological  :", " ----  ",
#                    " PYSC211 - Biological Psychology", "PSYC313V - Drugs, Mind and Behavior",
#                    "PYSC414 - Neuropsychology", " ---  ",
#                    "Pillar 2 - Cognitive :", "PSYC221- Cognitive Psychology", "PSYC322 - Memory in Everyday Life",
#                    " ---- ", "Pillar 3 Developmental:",
#                    "PYSC231 - Developmental Psychology", "PYSCH332 - Adolescence and Emgerging Adulthood",
#                    "PSYC334 - Adult Devlopment and Aging",
#                    "PSYC435 - Childhood Behavior Disorders", " ---- ", "Pillar 4- Social & Personality:",
#                    "PSYC242 - Theories and Research in Personality",
#                    "PSYC241 - Social Psychology", "PSYC343 - Industrial and Organizational Psychology",
#                    "PSYC444 - Psychometrics", "PSYC445 - Psychology of Women", " ---- ",
#                    "Pillar 5 - Physical & Mental Health:", "PSYC251V - Psychopathology", "PSYC352V - Health Psychology",
#                    "PSYC353 - Forensic Psychology", "PSYC451 - Clinical and Counseling Psychology",
#                    "PSYC452V - 	Human Sexuality", " ---  ", "Select one additional PSYC unit:",
#                    "Any PSYC courses, excluding JSEMs, PSYC courses offered Pass-Fail Only, or PSYC 180."],
#     "Biology": ["BIOL100 - Current Perspectives Biology",
#                 "BIOL141P - Introductory Biology: Biochemistry, Cell Biology and Molecular Genetics",
#                 "BIOL142P - Introductory Biology: Animal and Plant Physiology", "BIOL243Q - Biostatistics",
#                 "BIOL244 - Introductory Biology III: Ecology and Evolution",
#                 "BIOL497 - Research Proposal",
#                 "Four BIOL units at the 300- or 400-level (not to include any independent study or Junior Seminar)",
#                 "----", "Collateral Requirements: ",
#                 "CHEM 141P & CHEM 142P : General Chemistry I and General Chemistry II",
#                 "Select one from the following:",
#                 " MATH 131Q - Calculus I with Review Part 2", "MATH 141Q - Calculus I with Analytic Geometry",
#                 "MATH 151 - Mathematics for Life Sciences"],
#     "Mathematics": ["MATH142Q - Calculus II with Analytic Geometry", "MATH243Q - Calculus III with Analytic Geometry",
#                     "MATH211Q- Linear Algebra", "MATH221Q - Introduction to Logic and Proof",
#                     "Select one unit from the following proof-oriented courses:", "MATH 312 - Advanced Linear Algebra",
#                     "MATH401 - Real Analysis I", "MATH431 - Topology", "MATH441 - Abstract Algebra I",
#                     "Select one unit from the following applications-oriented courses:",
#                     "MATH321 - Ordinary Differential Equations",
#                     "MATH341 - Mathematical Modeling and Computer Simulation",
#                     "MATH351 - Operations Research", "MATH361 - Numerical Analysis",
#                     "Four units in MATH, numbered 300 or higher", "Collateral Requirements:",
#                     "CSCI 141 or CSCI 261: Introduction to Computer Science I or Data Science I"],
#     "Chemistry": ["CHEM141P - General Chemistry 1", "CHEM142P - General Chemistry II", "CHEM201 - Organic Chemistry 1",
#                   "CHEM202 - Inorganic Chemistry", "CHEM203 - Physical Chemistry", "CHEM204 - Biochemistry I",
#                   "CHEM205 - Analytical Chemistry", "CHEM301 - Organic Chemistry II",
#                   "CHEM498 - Research Proposal", "Select two units from the following in-depth courses: ",
#                   "CHEM302 - Biological Inorganic Chemistry", "CHEM303 - Advanced Physical Chemistry",
#                   "CHEM304 - Biochemistry II", "CHEM305 - Instrumental Analysis: Forensic Chemistry",
#                   "CHEM306 - Spectra and Structure", "CHEM307 - Nucleic Acid Structure, Function, and Metabolism",
#                   "CHEM 308 - Advanced Organic Chemistry", "CHEM309 - Advanced Environmental Chemistry",
#                   "Collateral Requirements: ",
#                   "MATH 141Q & MATH142Q - Calculus I with Analytic Geometry & Calculus II with Analytic Geometry",
#                   "----", "Select one of the following sequences:",
#                   "PHYS 121P & PHYS 122P - College Physics I and College Physics II",
#                   "PHYS 141P & PHYS 142P - University Physics I and University Physics II"],
#     "Cybersecurity": ["CSCI 141 - Introduction to Computer Science I",
#                       "CSCI 142 - Introduction to Computer Science II", "CSCI 221 - Software Development I",
#                       "CSCI 301 - Operating Systems", "CSCI 304 - Computer Networks", "CINF 201 - Database Systems",
#                       "CINF 301 - Web Application Development", "CSEC 141 - Introduction to Cybersecurity",
#                       "CSEC 302 - Secure Coding", "CSEC 331 - Computer and Network Security",
#                       "Two 300- or 400-level CSCI, CINF, CSEC units (excluding CSCI/CINF/CSEC Junior Seminars).",
#                       " Collateral Requirements -", "---", "Select one unit from the following",
#                       " MATH 125Q - Introduction to Mathematical and Statistical Modeling",
#                       " MATH 131Q - Calculus I with Review Part 2", "MATH141Q -  Calculus I with Analytic Geometry"],
#     "Music": ["Courses to be taken in the School of Music - Stetson Music Core", "Theory:",
#               " MUSC 171 - Diatonic Harmony", " MUSC 172 - Chrmoatic Harmony", " MUSC 271 - Form and Analysis", "----",
#               "Aural Training:", "MUSC 173 - Aural Training 1", "MUSC 174 - Aural Training II",
#               "MUSC 273 - Aural Training III", "MUSC 274 - Aural Training IV", "-----", "Functional Keyboard:",
#               "MUSC 175 - Functional Keyboard  I", " MUSC 176 - Functional Keyboard II",
#               "MUSc 275 - Functional Keyboard III", "MUSC 276 - Functional Keyboard IV", "-----", "Music History:",
#               "MUSC 211H - 	History of European Music: 1700-1900", "----", "Lower-divison lessons:",
#               "MUSA 112 - Primary Lower Divison Lessons for Music Majors", "---", "Music Culture:",
#               "MUSC 151 - Music Culture",
#               "---", "Career Skills:", "MUSC 300 - Career Skills for the Entrepeneurial Musician",
#               "Additional Music Requirements", "Upper divison Theory or Music Hisotry and Literature electives",
#               "Select two from the following:",
#               "MUSC 311 - History of European Music:before 1700", "MUSC 371 - Counterpoint",
#               "MUSC 372 - Post-Tonal and Contemporary Music Theory", "MUSC 379 - 	Orchestration and Arranging",
#               "MUSC 383 - Wind Band Literature", "MUSC 387 - Opera Literature", "MUSC 388 - Piano Literature I",
#               "MUSC 389 - Piano Literature II", "MUSC 390 - Special Topics in Music", "MUSC 391 - Symphonic Literature",
#               "MUSC 392 - Song Literature", "MUSC 394 - Chamber Music Literature", "MUSC 471 - Advanced Analysis",
#               "----", "Upper divison lessons/Music Experience Bundle:",
#               "MUSA 312 - Primary Upper-Division Lessons for Music Majors (four semesters)",
#               "MUSX 462 - Senior Recital (25-min)", "Six ensembles", "Sophomore Decision",
#               "Oral Communication Competency"],
#     "Digital Arts": ["DIGA 101A - Digital Art Fundamentals", "DIGA 161A - Digital Audio Fundamentals",
#                      "Two DIGA Electives", "Select Two of the following sequences:",
#                      "DIGA 225 & DIGA 325 Digital Photography and Advanced Digital Photography",
#                      "DIGA 231 & DIGA 331 - Interactivity and Art and Advanced Interactivity and Art",
#                      "DIGA 251 & DIGA 351 - Digital Video Fundamentals and Advanced Digital Video",
#                      "DIGA 301 & DIGA 302 - 3D Modeling and Animation and Advanced 3D Modeling and Animation",
#                      "DIGA 361 & DIGA 362 - Audio Recording and Production I and Audio Recording and Production II",
#                      "DIGA 365 & DIGA 366 - Electronic Music and Sound Design I nd Electronic Music and Sound Design II",
#                      "DIGA 465 & DIGA 466 - Scoring for Multimedia and Advanced Scoring for the Media",
#                      "DIGA 398 - Advanced Digital Arts Studio",
#                      "Three units total from any of the following prefixes: ARTS, ARTH, CREA, MUSC, PHYS, ENCW or THEA"]
# }
