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

    print("Loading '/'...")
ourPaths() # Must be placed at beginning of file.


# app.register_blueprint(views, url_prefix='/')
views = Blueprint(
    name='views',
    import_name=__name__,
    root_path=rootPath,
    template_folder=rootPath + "/front-end/src/templates",
    static_folder=rootPath + "/front-end/src/static"
    )

# @views.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         print("Request Method = POST")
#     else:
#         print("Request Method = GET")
#     # return redirect(url_for('views.index'))
#     return render_template('index.html')





