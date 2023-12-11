from flask import Blueprint, render_template

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


@progressTracker_bp.route('/progress-tracker', methods=['POST'])
def progress_tracker():
    try:
        courses_data = list()

        # studentID    = request.form['student_id']
        # studentEmail = request.form['student_email']
        # student_ID = studentID

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
            print("MySQL connection (TA) is closed.")
