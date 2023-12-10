from flask import Blueprint, render_template

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

    print("Loading '/Course-Registration'...")
ourPaths() # Must be placed at beginning of file.


# app.register_blueprint(courseRegistration_bp, url_prefix='/course-registration')
courseRegistration_bp = Blueprint('courseRegistration', __name__,
                                  root_path = rootPath,
                                  template_folder= rootPath + "/front-end/src/blueprints/Course_Registration/templates",
                                  static_folder= rootPath + "/front-end/src/static")


@courseRegistration_bp.route('/course-registration')
def courseRegistration():
    return render_template('course_registration.html')
