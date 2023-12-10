from flask import Blueprint, render_template

import os

courseSearch_bp = Blueprint('courseSearch', __name__,
                            root_path = rootPath,
                            template_folder= rootPath + "/front-end/src/Course-Search/templates",
                            static_folder= rootPath + "/front-end/src/static")
