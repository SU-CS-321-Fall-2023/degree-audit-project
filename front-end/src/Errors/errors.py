from flask import Blueprint, render_template

import os

errors_bp = Blueprint('errors', __name__,
                      root_path = rootPath,
                      template_folder= rootPath + "/front-end/src/Errors/templates",
                      static_folder= rootPath + "/front-end/src/static")
