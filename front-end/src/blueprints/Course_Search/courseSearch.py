from flask import Blueprint, render_template

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

    print("Loading '/Course-Search'...")
ourPaths() # Must be placed at beginning of file.


# weblet.register_blueprint(courseSearch_bp, url_prefix='/course-search')
courseSearch_bp = Blueprint(
    name='courseSearch',
    import_name=__name__,
    root_path=rootPath,
    template_folder=rootPath + "/front-end/src/blueprints/Course_Search/templates",
    static_folder=rootPath + "/front-end/src/static"
)


@courseSearch_bp.route('/')
def courseSearch():
    return render_template('course_search.html')
