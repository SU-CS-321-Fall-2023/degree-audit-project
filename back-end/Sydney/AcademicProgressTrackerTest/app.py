from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
from wtforms import SubmitField 

import mysql.connector
import os
rootPath = os.path.abspath(os.getcwd())

pwFile = (rootPath + "/ourPySQL.txt")
with open(pwFile, 'r') as passFile:
    password = passFile.readline()
    # Password for the databases gets read from a file, so
    # that it is not explicitly stored here in the code.
    # Also, the databases are currently located locally on 
    # my machine (Alexander G.) and I do not feel inclined 
    # to allowing the entire world have free root access to 
    # my computer's databases. MySQL Injections are scary.

# catalog = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password=password,
#     database="catalog"
# )
# reviews = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password=password,
#     database="reviews"
# )
# myCatalog = catalog.cursor(prepared=True)
# myReviews = reviews.cursor(prepared=True)

app = Flask(
    __name__,
    root_path=(rootPath),
    template_folder= rootPath + "/back-end/Sydney/AcademicProgressTrackerTest/templates")
    # static_folder= rootPath + "/back-end/Sydney/CourseReviewApp/static")

app.config['SECRET_KEY'] = 'your_secret_key_here'  # You can use a more secure method to generate a secret key

# class CourseForm(FlaskForm):
#     course_name = StringField('Course Name', validators=[DataRequired()])
#     grade = StringField('Grade', validators=[DataRequired()])
#     academic_year = SelectField('Academic Year', choices=[('Year 1', 'Year 1'), ('Year 2', 'Year 2'), ('Year 3', 'Year 3'), ('Year 4', 'Year 4')])
#     submit = SubmitField('Add Course')  # This is the new line to add

@app.route('/')
def index():
    try:
        courses_data = list()

        progress = mysql.connector.connect(
            host="localhost",
            user="root",
            password=password,
            database="progress"
        )
        myProgress = progress.cursor(prepared=True)
        sql_query = """SELECT `id`, `courseNumber`, `subject`, `courseReferenceNumber`, `courseTitle`, `campusCode`, `termDescription`, `gpaHours`, `hoursAttempted`, `hoursEarned`, `midtermGrade`, `finalGrade`, `qualityPoints` FROM agarofalo;"""
        myProgress.execute(sql_query)
        myResult = myProgress.fetchall()

        for x in myResult:
            courses_data.append(x)
        return render_template('index.html', courses=courses_data)

    except mysql.connector.Error as error:
        print("query failed {}".format(error))

    finally:
        if progress.is_connected():
            myProgress.close()
            progress.close()
            print("MySQL connection is closed.")


    # courses_data = myProgress.execute(f"SELECT * FROM {StudentID}")
    # This is sample data. In a real-world scenario, you'd likely fetch this data from a database.
    # courses_data = [
    #     {"name": "Math 101", "grade": "A", "academic_year": "Year 1"},
    #     {"name": "English 101", "grade": "D", "academic_year": "Year 1"},
    #     {"name": "Physics 101", "grade": "B", "academic_year": "Year 2"},
    #     {"name": "Computer Science 101", "grade": "A", "academic_year": "Year 3"},
    #     {"name": "Cybersecurity 101", "grade": "C", "academic_year": "Year 4"},
        # ... you can add more courses as per your requirement ...
    # ]

# @app.route('/add_course', methods=['GET', 'POST'])
# def add_course():
#     # count = myProgress.execute("SELECT COUNT(*) FROM alex;")
#     # print(count)
#     form = CourseForm()
#     if form.validate_on_submit():
#         course_name = form.course_name.data
#         grade = form.grade.data
#         academic_year = form.academic_year.data
#         print(course_name)
#         print(grade)
#         print(academic_year)

#         myProgress.execute(f"INSERT INTO alex (courseName, grade, academicYear) VALUES ('{course_name}', '{grade}', '{academic_year}');")
#         progress.commit()
#         myProgress.execute("SELECT * FROM alex;")
#         myResult = myProgress.fetchall()
#         for x in myResult:
#             print(x)


#         # Save the data... (like saving to a database or any other storage)

#         return redirect(url_for('index'))
#     return render_template('add_course.html', form=form)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7000, debug=True)
