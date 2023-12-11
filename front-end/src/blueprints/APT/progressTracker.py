from flask import Blueprint, render_template, redirect, url_for
from flask import flash, request
import time

import mysql.connector

# from weblet import rootPath, passwordTA, passwordTC, weblet
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

    print("Loading '/APT'...")
ourPaths() # Must be placed at beginning of file.


# weblet.register_blueprint(progressTracker_bp, url_prefix='/APT')
progressTracker_bp = Blueprint(
    name='progressTracker',
    import_name=__name__,
    root_path=rootPath,
    template_folder=rootPath + "/front-end/src/blueprints/APT/templates",
    static_folder=rootPath + "/front-end/src/static"
)


# @progressTracker_bp.route('/progress-tracker', methods=['POST'])
@progressTracker_bp.route('/progress-tracker', methods=['POST'])
def progress_tracker():
    try:
        # Progress Tracker: Student Heading
        student_data = list()

        studentID    = request.form.get('student_id')
        studentEmail = request.form.get('student_email')

        students = mysql.connector.connect(
            host="174.138.53.254",
            user="TheAuditor",
            password=passwordTA,
            database="students"
        )
        myStudents = students.cursor(prepared=True)
        query_studentHeading = (
            """SELECT 
            `studentLevel`, `studentClass`, `studentGPA`, `majorOne`, `programOne`, `collegeOne`, 
            CASE WHEN `majorTwo` IS NOT NULL THEN `majorTwo`ELSE NULL END AS `majorTwo`,
            CASE WHEN `programTwo` IS NOT NULL THEN `programTwo`ELSE NULL END AS `programTwo`,
            CASE WHEN `collegeTwo` IS NOT NULL THEN `collegeTwo`ELSE NULL END AS `collegeTwo`,
            `anticipatedGradDate`
            FROM students WHERE studentID=%s ;""" 
            % (studentID))
        myStudents.execute(query_studentHeading)
        myResult1 = myStudents.fetchall()

        for x in myResult1:
            student_data.append(x)
        print(student_data)

        # Progress Tracker: Course History
        courses_data = list()

        progress = mysql.connector.connect(
            host="174.138.53.254",
            user="TheAuditor",
            password=passwordTA,
            database="progress"
        )
        myProgress = progress.cursor(prepared=True)

        # query to create table in MySQL for new student
        query_createTable = ("""CREATE TABLE IF NOT EXISTS `%s` LIKE defaultStudent ;""" % studentID)
        myProgress.execute(query_createTable)
        progress.commit()

        # query to fill Progress Tracker with data from MySQL table
        query_APT = (
            """SELECT 
            `id`, `courseNumber`, `subject`, `courseReferenceNumber`, `courseTitle`, 
            `campusCode`, `termDescription`, `gpaHours`, 
            `hoursAttempted`, `hoursEarned`, 
            `midtermGrade`, `finalGrade`, `qualityPoints` 
            FROM `%s` ;""" 
            % studentID
        )
        myProgress.execute(query_APT)
        myResult2 = myProgress.fetchall()
        for y in myResult2:
            courses_data.append(y)

        return render_template('progress_tracker.html', courses=courses_data, student=student_data)

    except mysql.connector.Error as error:
        if TypeError:
            flash(
                message="Invalid Student ID or Email.",
                category='error'
            )
            print("query failed {}".format(error))
            return redirect(url_for('home.index'))
        elif UnboundLocalError:
            flash(
                message="Invalid Student ID or Email.",
                category='error'
            )
            print("query failed {}".format(error))
            return redirect(url_for('home.index'))
        else:
            flash(
                message="Invalid Student ID or Email.",
                category='error'
            )
            print("query failed {}".format(error))
            return redirect(url_for('home.index'))
    finally:
        if progress.is_connected():
            myProgress.close()
            progress.close()
            print("MySQL connection (progress) is closed.")
        if students.is_connected():
            myStudents.close()
            students.close()
            print("MySQL connection (students) is closed.")
