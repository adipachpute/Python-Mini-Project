# subject.py
# This file contains the Subject class.
# Every subject the student adds becomes one Subject object.

from datetime import date


class Subject:

    # This runs automatically when a new subject is created
    def __init__(self, name, exam_date, difficulty, total_hours):
        self.name = name
        self.exam_date = exam_date        # stored as a string like "2026-06-10"
        self.difficulty = difficulty      # number from 1 to 5
        self.total_hours = total_hours    # how many hours planned in total
        self.completed_hours = 0          # starts at 0, increases as student studies

    # Calculate progress percentage
    def get_progress(self):
        if self.total_hours == 0:
            return 100
        progress = (self.completed_hours / self.total_hours) * 100
        progress = round(progress, 1)
        return progress

    # Add study hours to this subject
    def add_hours(self, hours):
        self.completed_hours = self.completed_hours + hours
        # Make sure completed hours never goes above total hours
        if self.completed_hours > self.total_hours:
            self.completed_hours = self.total_hours

    # Calculate how many days are left until the exam
    def days_left(self):
        exam = date.fromisoformat(self.exam_date)   # convert string to date
        today = date.today()
        difference = exam - today
        days = difference.days
        # Minimum 1 day to avoid dividing by zero in the formula
        if days < 1:
            days = 1
        return days

    # Convert this object into a dictionary so it can be saved to a file
    def to_dict(self):
        data = {
            "name": self.name,
            "exam_date": self.exam_date,
            "difficulty": self.difficulty,
            "total_hours": self.total_hours,
            "completed_hours": self.completed_hours
        }
        return data

    # Create a Subject object from a dictionary loaded from the file
    def load_from_dict(self, data):
        self.name = data["name"]
        self.exam_date = data["exam_date"]
        self.difficulty = data["difficulty"]
        self.total_hours = data["total_hours"]
        self.completed_hours = data["completed_hours"]

    # This controls what prints when you do print(subject)
    def display(self):
        print("  Name       :", self.name)
        print("  Exam Date  :", self.exam_date, " (", self.days_left(), "days left )")
        print("  Difficulty :", self.difficulty, "/ 5")
        print("  Progress   :", self.get_progress(), "%  (", self.completed_hours, "/", self.total_hours, "hrs )")
