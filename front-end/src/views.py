from flask import Blueprint, render_template
from flask import request

import mysql.connector

from weblet import rootPath, passwordTA, passwordTC, app

# app.register_blueprint(views, url_prefix='/')


views = Blueprint('views', __name__,
                  root_path = rootPath,
                  template_folder= rootPath + "/front-end/src/templates",
                  static_folder= rootPath + "/front-end/src/static")

@views.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("Request Method = POST")
    else:
        print("Request Method = GET")
    return render_template('index.html')





