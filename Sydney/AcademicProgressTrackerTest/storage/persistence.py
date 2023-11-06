# storage/persistence.py

import pickle
from models.student import Student

def save_student_data(student, filename="student_data.pkl"):
    with open(filename, 'wb') as file:
        pickle.dump(student, file)

def load_student_data(filename="student_data.pkl"):
    with open(filename, 'rb') as file:
        student = pickle.load(file)
    return student
