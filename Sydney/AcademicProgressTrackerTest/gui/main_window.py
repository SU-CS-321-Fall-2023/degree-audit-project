# gui/main_window.py

import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from models.student import Student
from models.course import Course
from models.academic_year import AcademicYear
from storage.persistence import save_student_data, load_student_data
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_academic_progress(window, student):
    # Sample data
    years = list(student.years.keys())
    courses_taken = [len(student.years[year]) for year in years]

    figure = plt.Figure(figsize=(6, 5), dpi=100)
    ax = figure.add_subplot(111)
    ax.bar(years, courses_taken, color='blue')
    ax.set_title('Courses Taken Over the Years')
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of Courses')

    canvas = FigureCanvasTkAgg(figure, window)
    canvas.draw()
    canvas.get_tk_widget().pack()



messagebox.showinfo("Academic Progress Tracker", "Stetson Student")

def run_app(student):
    window = ThemedTk(theme="arc")
    window.title("Academic Progress Tracker")
    progress = ttk.Progressbar(window, orient="horizontal", length=200, mode="determinate")
    progress.pack()
    progress["value"] = 50  # Example: set progress to 50%

    plot_academic_progress(window, student)

    window.mainloop()


class AcademicTrackerApp(tk.Tk):
    def __init__(self, student=None):
        super().__init__()
        self.title("Academic Progress Tracker (Sydney)")

        self.student = student if student else Student("Unknown")

        # Create GUI elements
        self.name_label = ttk.Label(self, text=f"Student: {self.student.name}")
        self.name_label.pack(pady=10)

        self.course_entry_label = ttk.Label(self, text="Enter Course Name:")
        self.course_entry_label.pack(pady=10)
        self.course_entry = ttk.Entry(self)
        self.course_entry.pack(pady=10)
        
        self.grade_entry_label = ttk.Label(self, text="Enter Grade:")
        self.grade_entry_label.pack(pady=10)
        self.grade_entry = ttk.Entry(self)
        self.grade_entry.pack(pady=10)

        self.year_entry_label = ttk.Label(self, text="Enter Academic Year:")
        self.year_entry_label.pack(pady=10)
        self.year_entry = ttk.Entry(self)
        self.year_entry.pack(pady=10)

        self.add_button = ttk.Button(self, text="Add Course", command=self.add_course_data)
        self.add_button.pack(pady=10)

        self.display = tk.Text(self, wrap=tk.WORD)
        self.display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.refresh_display()

    def add_course_data(self):
        course_name = self.course_entry.get()
        grade = self.grade_entry.get()
        year = int(self.year_entry.get())

        if year not in self.student.academic_years:
            self.student.add_academic_year(AcademicYear(year))
        
        course = Course(course_name, grade)
        self.student.academic_years[year].add_course(course)

        save_student_data(self.student)
        self.refresh_display()

    def refresh_display(self):
        self.display.delete(1.0, tk.END)
        self.display.insert(tk.END, str(self.student))

def run_app(student=None):
    app = AcademicTrackerApp(student)
    app.mainloop()
