from flask import Flask


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

def create_app():
    app = Flask(__name__,
                root_path = rootPath,
                template_folder= rootPath + "/front-end/src/templates",
                static_folder= rootPath + "/front-end/src/static")
    app.config['SECRET_KEY'] = 'hai'

    # View Imports
    import APT.progressTracker
    import Course_Registration.courseRegistration
    import Course_Reviews.courseReviews
    import Course_Search.courseSearch

    import Cultural_Credits.culturalCredits
    import Email.email
    import Errors.errors
    import Home.home
    import Interests.interests

    import views

    # from .APT.progressTracker import progressTracker_bp
    # from .Course_Registration.courseRegistration import courseRegistration_bp
    # from .Course_Reviews.courseReviews import courseReviews_bp
    # from .Course_Search.courseSearch import courseSearch_bp

    # from .Cultural_Credits.culturalCredits import culturalCredits_bp
    # from .Email.email import email_bp
    # from .Errors.errors import errors_bp
    # from .Home.home import home_bp
    # from .Interests.interests import interests_bp

    # from .views import views



    # Page Registry
    app.register_blueprint(progressTracker_bp, url_prefix='/APT')

    app.register_blueprint(courseRegistration_bp, url_prefix='/course-registration')
    app.register_blueprint(courseReviews_bp, url_prefix='/course-reviews')
    app.register_blueprint(courseSearch_bp, url_prefix='/course-search')

    app.register_blueprint(culturalCredits_bp, url_prefix='/cultural-credits')
    app.register_blueprint(email_bp, url_prefix='/email')
    app.register_blueprint(errors_bp, url_prefix='/error')
    app.register_blueprint(home_bp, url_prefix='/home')
    app.register_blueprint(interests_bp, url_prefix='/interests')

    app.register_blueprint(views, url_prefix='/')


    return app

app = create_app()

# app = Flask(__name__,
#             root_path = rootPath,
#             template_folder= rootPath + "/front-end/src/templates",
#             static_folder= rootPath + "/front-end/src/static")
# app.config['SECRET_KEY'] = 'hai'

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


if __name__ == "__main__":
    """
    Must be placed at the end of the file.
    """
    app.run(host = '127.0.0.1', port = 9000, debug=True)
    # app.run(host= "174.138.53.254" , port = 9000, debug = True)





# # cors = CORS(app)
# # Configure the value of the "origins" key to be the actual URL of the React Frontend.
# # Make sure to NOT have a / at the end of the "origins" URL.
# cors = CORS(app, resources={r"/*": {"origins": "http://localhost:*"}})
