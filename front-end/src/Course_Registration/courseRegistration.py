from flask import Blueprint, render_template

import os

courseRegistration_bp = Blueprint('courseRegistration', __name__,
                                  root_path = rootPath,
                                  template_folder= rootPath + "/front-end/src/Course-Registration/templates",
                                  static_folder= rootPath + "/front-end/src/static")
