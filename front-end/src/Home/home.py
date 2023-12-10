from flask import Blueprint, render_template, redirect, url_for
from flask import request

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

    print("Loading '/Home'...")
ourPaths() # Must be placed at beginning of file.


# app.register_blueprint(home_bp, url_prefix='/home')
home_bp = Blueprint('home', __name__,
                    root_path = rootPath,
                    template_folder= rootPath + "/front-end/src/Home/templates",
                    static_folder= rootPath + "/front-end/src/static")


@home_bp.route('/idForm', methods=['POST'])
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
        sql_query = """SELECT `id`, `courseNumber`, `subject`, `courseReferenceNumber`, `courseTitle`, `campusCode`, `termDescription`, `gpaHours`, `hoursAttempted`, `hoursEarned`, `midtermGrade`, `finalGrade`, `qualityPoints` FROM `800737736` ; """
        myStudentsTA.execute(sql_query)
        myResult = myStudentsTA.fetchall()
        # myStudentsTA.execute(f"CALL sys.table_exists('students', '{studentID}', @exists); SELECT @exists;")
        # # sql_query = """SELECT studentID FROM students.students WHERE studentID=%s ;"""
        # # myStudentsTA.execute(sql_query,studentID)
        # myResult = myStudentsTA.fetchall()


        for x in myResult:
            courses_data.append(x)
        return redirect(url_for('progress_tracker'), courses=courses_data)

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
    return redirect(url_for('progress_tracker'), courses=courses_data)
