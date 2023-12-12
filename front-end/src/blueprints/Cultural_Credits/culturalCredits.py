from flask import Blueprint, render_template, redirect, url_for


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

    print("Loading '/Cultural-Credits'...")
ourPaths() # Must be placed at beginning of file.


# weblet.register_blueprint(culturalCredits_bp, url_prefix='/cultural-credits')
culturalCredits_bp = Blueprint(
    name='culturalCredits',
    import_name=__name__,
    root_path=rootPath,
    template_folder=rootPath + "/front-end/src/blueprints/Cultural_Credits/templates",
    static_folder=rootPath + "/front-end/src/static"
)


@culturalCredits_bp.route('/')
def culture():
    try:
        # student_data = list()
        studentID = 800737736
        
        cultural_events = [
            {"name": "Pollination:The Art of Citizen Science", "date": "2023-24-08", "units": "1"},
            {"name": "The Bone Wars: Museums, Fossils and National Identity ", "date": "2023-24-08", "units": "1"},
            # Add more events here.
        ]

        students = mysql.connector.connect(
            host="174.138.53.254",
            user="TheAuditor",
            password=passwordTA,
            database="students"
        )
        myStudents = students.cursor(prepared=True)
        query_current = (
            """SELECT 
            `currentCulturalCredits`
            FROM students WHERE studentID=%s ;""" 
            % (studentID))
        myStudents.execute(query_current)
        resultCurrent = myStudents.fetchone()
        query_required = (
            """SELECT 
            `requiredCulturalCredits`
            FROM students WHERE studentID=%s ;""" 
            % (studentID))
        myStudents.execute(query_required)
        resultRequired = myStudents.fetchone()

        currentCredits  = int(resultCurrent[0])
        requiredCredits = int(resultRequired[0])

        remainingCredits = (requiredCredits - currentCredits)
        if (remainingCredits < 0):
            remainingCredits = 0

        return render_template(
            'culture.html', 
            currentCredits=currentCredits,
            requiredCredits=requiredCredits,
            remainingCredits=remainingCredits,
            events=cultural_events
        )

    except mysql.connector.Error as error:
        print("query failed {}".format(error))
        return redirect(url_for('home.index'))


        # if TypeError:
        #     flash(
        #         message="Invalid Student ID or Email.",
        #         category='error'
        #     )
        #     print("query failed {}".format(error))
        #     return redirect(url_for('home.index'))
        # elif UnboundLocalError:
        #     flash(
        #         message="Invalid Student ID or Email.",
        #         category='error'
        #     )
        #     print("query failed {}".format(error))
        #     return redirect(url_for('home.index'))
        # else:
        #     flash(
        #         message="Invalid Student ID or Email.",
        #         category='error'
        #     )
        #     print("query failed {}".format(error))
        #     return redirect(url_for('home.index'))
    finally:
        if students.is_connected():
            myStudents.close()
            students.close()
            print("MySQL connection (students) is closed.")



    # # Here, you would fetch data from Stetson's Engage platform and process it to show the user's cultural credits.
    # user_cultural_credits = 24
    # credits_remaining = 10  # Change this to the remaining credits.

    # # Dummy data for cultural credit events.
    # cultural_events = [
    #     {"name": "Pollination:The Art of Citizen Science", "date": "2023-24-08", "units": "1"},
    #     {"name": "The Bone Wars: Museums, Fossils and National Identity ", "date": "2023-24-08", "units": "1"},
    #     # Add more events here.
    # ]

    # return render_template('culture.html', credits=user_cultural_credits, remaining=credits_remaining, events=cultural_events)
