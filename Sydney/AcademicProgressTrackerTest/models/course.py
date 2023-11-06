# models/course.py

class Course:
    def __init__(self, course_name, grade=None):
        self.course_name = course_name
        self.grade = grade

    def set_grade(self, grade):
        self.grade = grade

    def __str__(self):
        return f"{self.course_name} ({self.grade if self.grade else 'Not Graded'})"
