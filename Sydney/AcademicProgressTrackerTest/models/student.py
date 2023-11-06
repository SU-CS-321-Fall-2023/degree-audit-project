# models/student.py

from .academic_year import AcademicYear

class Student:
    def __init__(self, name):
        self.name = name
        self.academic_years = {}

    def add_academic_year(self, academic_year):
        if not isinstance(academic_year, AcademicYear):
            raise ValueError("The provided object is not an instance of the AcademicYear class.")
        self.academic_years[academic_year.year] = academic_year

    def __str__(self):
        return f"Student: {self.name}\n" + "\n".join(str(year) for year in self.academic_years.values())
