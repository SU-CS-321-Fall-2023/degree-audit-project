from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
from wtforms import SubmitField 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # You can use a more secure method to generate a secret key

class CourseForm(FlaskForm):
    course_name = StringField('Course Name', validators=[DataRequired()])
    grade = StringField('Grade', validators=[DataRequired()])
    academic_year = SelectField('Academic Year', choices=[('Year 1', 'Year 1'), ('Year 2', 'Year 2'), ('Year 3', 'Year 3'), ('Year 4', 'Year 4')])
    submit = SubmitField('Add Course')  # This is the new line to add

@app.route('/')
def index():
    # This is sample data. In a real-world scenario, you'd likely fetch this data from a database.
    courses_data = [
        {"name": "Math 101", "grade": "A", "academic_year": "Year 1"},
        {"name": "English 101", "grade": "D", "academic_year": "Year 1"},
        {"name": "Physics 101", "grade": "B", "academic_year": "Year 2"},
        {"name": "Computer Science 101", "grade": "A", "academic_year": "Year 3"},
        {"name": "Cybersecurity 101", "grade": "C", "academic_year": "Year 4"},
        # ... you can add more courses as per your requirement ...
    ]
    return render_template('index.html', courses=courses_data)


@app.route('/add_course', methods=['GET', 'POST'])
def add_course():
    form = CourseForm()
    if form.validate_on_submit():
        course_name = form.course_name.data
        grade = form.grade.data
        academic_year = form.academic_year.data

        # Save the data... (like saving to a database or any other storage)

        return redirect(url_for('index'))
    return render_template('add_course.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
