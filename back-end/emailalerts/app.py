import os

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = os.urandom(24)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
students = {
    'pshelly@stetson.edu': {'has_hold': True, 'name': 'Peyton Shelly'},
    'asmith@stetson.edu': {'has_hold': False, 'name': 'Alice Smith'},
}
# db = SQLAlchemy(app)


# class Student(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#  email = db.Column(db.String(120), unique=True, nullable=False)
# has_hold = db.Column(db.Boolean, default=False)


app.config['MAIL_SERVER'] = 'smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = "pshelly@stetson.edu"
app.config['MAIL_PASSWORD'] = "Hattercheer01$prs"

mail = Mail(app)


@app.route('/')
def index():
    return render_template('email-index.html')


@app.route('/send_alert', methods=['POST'])
def send_alert():
    student_email = request.form.get('email')  # Update 'email' to match the actual name attribute in your form

    has_hold = check_hold_status(student_email)

    if has_hold:
        flash('You have a hold on your account. Please remove it to register for classes.', 'warning')

        send_email(student_email, 'Hold Alert',
                   'You have a hold on your account. Please remove it to register for classes.')

    else:
        flash('No holds on your account. You can proceed with class registration.', 'success')

    return redirect(url_for('email-index'))



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


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run(debug=True)
