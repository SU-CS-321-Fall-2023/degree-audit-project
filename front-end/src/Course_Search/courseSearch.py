from flask import Blueprint, render_template

from weblet import rootPath, passwordTA, passwordTC, app

# app.register_blueprint(courseSearch_bp, url_prefix='/course-search')


courseSearch_bp = Blueprint('courseSearch', __name__,
                            root_path = rootPath,
                            template_folder= rootPath + "/front-end/src/Course-Search/templates",
                            static_folder= rootPath + "/front-end/src/static")


@courseSearch_bp.route('/course-search')
def courseSearch():
    return render_template('course_search.html')
