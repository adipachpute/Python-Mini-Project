# utils.py
# This file contains helper functions.
# These are small reusable functions used across the project
# mainly for taking safe input from the user.

from datetime import date


# Ask user for a decimal number, keep asking until they enter a valid one
def get_float(prompt, min_val=0):
    while True:
        user_input = input(prompt)
        try:
            number = float(user_input)
            if number < min_val:
                print("  Please enter a number greater than", min_val)
            else:
                return number
        except ValueError:
            print("  That is not a valid number. Please try again.")


# Ask user for a whole number between min_val and max_val
def get_int(prompt, min_val=1, max_val=5):
    while True:
        user_input = input(prompt)
        try:
            number = int(user_input)
            if number < min_val or number > max_val:
                print("  Please enter a number between", min_val, "and", max_val)
            else:
                return number
        except ValueError:
            print("  That is not a valid number. Please try again.")


# Ask user for a date in YYYY-MM-DD format that is today or in the future
def get_future_date(prompt):
    while True:
        user_input = input(prompt).strip()
        try:
            exam_date = date.fromisoformat(user_input)
            if exam_date < date.today():
                print("  Exam date must be today or in the future.")
            else:
                return user_input
        except ValueError:
            print("  Please use the format YYYY-MM-DD  for example: 2026-06-10")


# Print a horizontal line
def separator():
    print("-" * 50)


# Print a section header with lines above and below
def header(title):
    separator()
    print(" ", title)
    separator()
