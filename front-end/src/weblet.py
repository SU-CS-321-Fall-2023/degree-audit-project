from flask import Flask, render_template
from flask import request


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

def create_weblet():
    """_summary_
    "View Imports" block should be placed before the 
    "Page Registry" block.

    "Page Registry" block is to be placed at the end of 
    create_weblet(). If it is not placed at the end, and a 
    "@blueprint.route()" is called on an existing blueprint, 
    then an "AssertionError" will be triggered.

    Returns:
        _type_: _description_
    """
    weblet = Flask(
        import_name=__name__,
        root_path=rootPath,
        template_folder=rootPath + "/front-end/src/templates",
        static_folder=rootPath + "/front-end/src/static"
    )
    weblet.config['SECRET_KEY'] = 'hai'

    # View Imports
    from blueprints.APT.progressTracker import progressTracker_bp

    from blueprints.Course_Registration.courseRegistration import courseRegistration_bp
    from blueprints.Course_Reviews.courseReviews import courseReviews_bp
    from blueprints.Course_Search.courseSearch import courseSearch_bp

    from blueprints.Cultural_Credits.culturalCredits import culturalCredits_bp
    from blueprints.Email.email import email_bp
    # from blueprints.Errors.errors import errors_bp
    from blueprints.Home.home import home_bp
    from blueprints.Interests.interests import interests_bp

    from views import views
    # END OF View Imports


    # Global Error Handlers
    @weblet.errorhandler(404)
    def page_not_found(e):
        # if a page does not exist
        if request.path.startswith('/'):
            # we return a generic 404 page
            return render_template("errors/404.html"), 404
        else:
            # otherwise we return a generic 404 page
            return render_template("errors/404.html"), 404
    @weblet.errorhandler(405)
    def method_not_allowed(e):
        # if a request has the wrong method to our API
        if request.path == "/APT/progress-tracker":
            # we return a special 405 page
            return render_template("errors/405_APT.html"), 405
        else:
            # otherwise we return a generic 405 page
            return render_template("errors/405.html"), 405


    # Page Registry
    # To be placed at the end of the create_app()
    weblet.register_blueprint(progressTracker_bp, url_prefix='/APT')

    weblet.register_blueprint(courseRegistration_bp, url_prefix='/course-registration')
    weblet.register_blueprint(courseReviews_bp, url_prefix='/course-reviews')
    weblet.register_blueprint(courseSearch_bp, url_prefix='/course-search')

    weblet.register_blueprint(culturalCredits_bp, url_prefix='/cultural-credits')
    weblet.register_blueprint(email_bp, url_prefix='/email')
    # weblet.register_blueprint(errors_bp, url_prefix='/error')
    weblet.register_blueprint(home_bp, url_prefix='/home')
    weblet.register_blueprint(interests_bp, url_prefix='/interests')

    weblet.register_blueprint(views, url_prefix='/')
    # END OF Page Registry


    return weblet

weblet = create_weblet()

if __name__ == "__main__":
    """
    Must be placed at the end of the file.
    """
    weblet.run(host = '127.0.0.1', port = 9000, debug=True)
    # app.run(host= "174.138.53.254" , port = 9000, debug = True)



# import mysql.connector
# # Connections to the MySQL Databases
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



# # cors = CORS(app)
# # Configure the value of the "origins" key to be the actual URL of the React Frontend.
# # Make sure to NOT have a / at the end of the "origins" URL.
# cors = CORS(app, resources={r"/*": {"origins": "http://localhost:*"}})
