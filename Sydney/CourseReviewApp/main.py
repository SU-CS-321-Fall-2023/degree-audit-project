from models.course import Course
from models.review import Review
from storage.persistence import load_data, save_data
from gui.main_window import run_app

def main():
    try:
        courses = load_data()
    except:
        # Sample course setup; can be expanded
        courses = [Course("Mathematics"), Course("Physics"), Course("Chemistry")]
        save_data(courses)

    run_app(courses)

if __name__ == "__main__":
    main()
