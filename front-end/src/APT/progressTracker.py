from flask import Blueprint, render_template

from weblet import rootPath, passwordTA, passwordTC, app
import mysql.connector

# app.register_blueprint(progressTracker_bp, url_prefix='/APT')

progressTracker_bp = Blueprint('progressTracker', __name__,
                               root_path = rootPath,
                               template_folder= rootPath + "/front-end/src/APT/templates",
                               static_folder= rootPath + "/front-end/src/static")


@progressTracker_bp.route('/progress-tracker')
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
