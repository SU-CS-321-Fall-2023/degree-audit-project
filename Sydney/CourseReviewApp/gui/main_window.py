import tkinter as tk
from tkinter import ttk, messagebox
from models.course import Course
from models.review import Review
from storage.persistence import save_data, load_data


class ReviewApp(tk.Tk):
    def __init__(self, courses):
        super().__init__()
        self.title("Course Review App")
        
        self.courses = courses

        self.course_var = tk.StringVar()
        self.rating_var = tk.StringVar()
        self.review_var = tk.StringVar()

        ttk.Label(self, text="Select Course:").pack(pady=10)
        self.course_dropdown = ttk.Combobox(self, textvariable=self.course_var, values=[course.name for course in courses])
        self.course_dropdown.pack(pady=10)

        ttk.Label(self, text="Rating (1-5):").pack(pady=10)
        self.rating_entry = ttk.Entry(self, textvariable=self.rating_var)
        self.rating_entry.pack(pady=10)

        ttk.Label(self, text="Review:").pack(pady=10)
        self.review_entry = ttk.Entry(self, textvariable=self.review_var)
        self.review_entry.pack(pady=10)

        self.submit_btn = ttk.Button(self, text="Submit Review", command=self.submit_review)
        self.submit_btn.pack(pady=10)

        self.review_display = tk.Text(self)
        self.review_display.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.course_dropdown.bind("<<ComboboxSelected>>", self.update_reviews_display)

    def submit_review(self):
        course_name = self.course_var.get()
        try:
            rating = int(self.rating_var.get())
            if not 1 <= rating <= 5:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Rating should be a number between 1 and 5.")
            return

        review_text = self.review_var.get()

        for course in self.courses:
            if course.name == course_name:
                course.add_review(Review(rating, review_text))
                break

        save_data(self.courses)
        self.update_reviews_display()

    def update_reviews_display(self, event=None):
        self.review_display.delete(1.0, tk.END)

        course_name = self.course_var.get()
        for course in self.courses:
            if course.name == course_name:
                for review in course.reviews:
                    self.review_display.insert(tk.END, f"Rating: {review.rating}\nReview: {review.comment}\n\n")

def run_app(courses):
    app = ReviewApp(courses)
    app.mainloop()
