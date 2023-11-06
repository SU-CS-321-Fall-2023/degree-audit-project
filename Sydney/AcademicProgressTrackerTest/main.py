# main.py

from models.student import Student
from storage.persistence import load_student_data
from gui.main_window import run_app

def main():
    # Try to load student data, if it exists
    try:
        student = load_student_data()
    except:
        student = None

    run_app(student)

if __name__ == "__main__":
    main()
