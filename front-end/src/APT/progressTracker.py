from flask import Blueprint, render_template

import os

progressTracker_bp = Blueprint('progressTracker', __name__,
                               root_path = rootPath,
                               template_folder= rootPath + "/front-end/src/APT/templates",
                               static_folder= rootPath + "/front-end/src/static")
