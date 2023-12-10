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

    print("Loading '/Cultural-Credits'...")
ourPaths() # Must be placed at beginning of file.


# app.register_blueprint(culturalCredits_bp, url_prefix='/cultural-credits')
culturalCredits_bp = Blueprint('culturalCredits', __name__,
                               root_path = rootPath,
                               template_folder= rootPath + "/front-end/src/blueprints/Cultural_Credits/templates",
                               static_folder= rootPath + "/front-end/src/static")


@culturalCredits_bp.route('/culture')
def culture():
    # Here, you would fetch data from Stetson's Engage platform and process it to show the user's cultural credits.
    user_cultural_credits = 24
    credits_remaining = 10  # Change this to the remaining credits.

    # Dummy data for cultural credit events.
    cultural_events = [
        {"name": "Pollination:The Art of Citizen Science", "date": "2023-24-08", "units": "1"},
        {"name": "The Bone Wars: Museums, Fossils and National Identity ", "date": "2023-24-08", "units": "1"},
        # Add more events here.
    ]

    return render_template('culture.html', credits=user_cultural_credits, remaining=credits_remaining, events=cultural_events)
