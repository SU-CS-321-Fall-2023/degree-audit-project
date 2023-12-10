from flask import Blueprint, render_template
from flask import request

from weblet import rootPath


errors_bp = Blueprint('errors', __name__,
                      root_path = rootPath,
                      template_folder= rootPath + "/front-end/src/Errors/templates",
                      static_folder= rootPath + "/front-end/src/static")


@errors_bp.errorhandler(404)
def page_not_found(e):
    # if a page does not exist
    if request.path.startswith('/'):
        # we return a generic 404 page
        return render_template("Errors/404.html"), 404
    else:
        # otherwise we return a generic 404 page
        return render_template("Errors/404.html"), 404
@errors_bp.errorhandler(405)
def method_not_allowed(e):
    # if a request has the wrong method to our API
    if request.path.startswith('/'):
        # we return a generic 405 page
        return render_template("Errors/405.html"), 405
    else:
        # otherwise we return a generic 405 page
        return render_template("Errors/405.html"), 405
