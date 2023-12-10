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


# import mysql.connector

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
# progress = mysql.connector.connect(
#     host="174.138.53.254",
#     user="TheAuditor",
#     password=passwordTA,
#     database="progress"
# )

# myCatalog = catalog.cursor(prepared=True)
# myReviews = reviews.cursor(prepared=True)
# myProgress = progress.cursor(prepared=True)

