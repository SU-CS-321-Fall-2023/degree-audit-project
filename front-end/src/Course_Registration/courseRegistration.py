from flask import Blueprint, render_template

from weblet import rootPath, passwordTA, passwordTC, app

# app.register_blueprint(courseRegistration_bp, url_prefix='/course-registration')


courseRegistration_bp = Blueprint('courseRegistration', __name__,
                                  root_path = rootPath,
                                  template_folder= rootPath + "/front-end/src/Course-Registration/templates",
                                  static_folder= rootPath + "/front-end/src/static")


@courseRegistration_bp.route('/course-registration')
def courseRegistration():
    return render_template('course_registration.html')
