# models/academic_year.py

from .course import Course

class AcademicYear:
    def __init__(self, year):
        self.year = year
        self.courses = []

    def add_course(self, course):
        if not isinstance(course, Course):
            raise ValueError("The provided object is not an instance of the Course class.")
        self.courses.append(course)

    def __str__(self):
        return f"{self.year}:\n" + "\n".join(str(course) for course in self.courses)
