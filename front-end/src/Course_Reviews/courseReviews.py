from flask import Blueprint, render_template

import os

courseReviews_bp = Blueprint('courseReviews', __name__,
                  root_path = rootPath,
                  template_folder= rootPath + "/front-end/src/Course-Reviews/templates",
                  static_folder= rootPath + "/front-end/src/static")
