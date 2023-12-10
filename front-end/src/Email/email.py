from flask import Blueprint, render_template, redirect, url_for
from flask import flash, request

from flask_mail import Mail, Message

from weblet import rootPath, passwordTA, passwordTC, app

# app.register_blueprint(email_bp, url_prefix='/email')


email_bp = Blueprint('email', __name__,
                  root_path = rootPath,
                  template_folder= rootPath + "/front-end/src/Email/templates",
                  static_folder= rootPath + "/front-end/src/static")


students = {
    'pshelly@stetson.edu': {'has_hold': True, 'name': 'Peyton Shelly'},
    'asmith@stetson.edu': {'has_hold': False, 'name': 'Alice Smith'},
}

app.config['MAIL_SERVER'] = 'smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = "pshelly@stetson.edu"
app.config['MAIL_PASSWORD'] = "Hattercheer01$prs"

mail = Mail(app)


@email_bp.route('/')
def index():
    return render_template('email.html')


@email_bp.route('/send_alert', methods=['POST'])
def send_alert():
    student_email = request.form.get('email')  # Update 'email' to match the actual name attribute in your form
    has_hold = check_hold_status(student_email)

    if has_hold:
        flash('You have a hold on your account. Please remove it to register for classes.', 'warning')

        send_email(student_email, 'Hold Alert',
                   'You have a hold on your account. Please remove it to register for classes.')

    else:
        flash('No holds on your account. You can proceed with class registration.', 'success')

    return redirect(url_for('index'))



def check_hold_status(student_email):
    # Check if the student email exists in the fake database
    student = students.get(student_email)

    if student:
        return student['has_hold']
    else:
        # If the student is not found in the fake database, consider them as having a hold for this example
        app.logger.warning(f"Student with email {student_email} not found in the fake database.")
        return True


def send_email(to, subject, body):
    msg = Message(subject, sender="pshelly@stetson.edu", recipients=[to], body=body)
    mail.send(msg)
