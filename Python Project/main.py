# main.py
# This is the starting point of the program.
# It shows the menu and calls the right function based on user choice.
# Run this file to start the program:  python main.py

from subject import Subject
from storage import save_subjects, load_subjects
from planner import recommend, ranked_subjects, priority_score
from utils import get_float, get_int, get_future_date, separator, header


# Search for a subject by name in the list
def find_subject(subjects, name):
    name = name.strip().lower()
    for subject in subjects:
        if subject.name.lower() == name:
            return subject
    return None   # return None if not found


# Option 1: Add a new subject
def add_subject(subjects):
    header("ADD SUBJECT")

    name = input("  Subject name      : ").strip()

    if name == "":
        print("  Name cannot be empty.")
        return

    if find_subject(subjects, name) != None:
        print("  That subject already exists.")
        return

    exam_date   = get_future_date("  Exam date (YYYY-MM-DD) : ")
    difficulty  = get_int("  Difficulty (1 to 5)   : ", 1, 5)
    total_hours = get_float("  Total study hours     : ", min_val=1)

    # Create a new Subject object and add it to the list
    new_subject = Subject(name, exam_date, difficulty, total_hours)
    subjects.append(new_subject)

    # Save the updated list to file
    save_subjects(subjects)
    print("\n  Subject added successfully!")


# Option 2: Update how many hours studied for a subject
def update_progress(subjects):
    header("UPDATE PROGRESS")

    if len(subjects) == 0:
        print("  No subjects added yet. Please add a subject first.")
        return

    name = input("  Enter subject name : ").strip()
    subject = find_subject(subjects, name)

    if subject == None:
        print("  Subject not found.")
        return

    hours = get_float("  Hours studied today : ", min_val=0.1)
    subject.add_hours(hours)

    save_subjects(subjects)

    print("\n  Progress updated!")
    print("  Current progress:", subject.get_progress(), "%")
    print("  Completed:", subject.completed_hours, "/", subject.total_hours, "hours")


# Option 3: Show all subjects
def view_subjects(subjects):
    header("ALL SUBJECTS")

    if len(subjects) == 0:
        print("  No subjects added yet.")
        return

    count = 1
    for subject in subjects:
        print("\n  [" + str(count) + "]")
        subject.display()
        count = count + 1


# Option 4: Show the recommended subject and full ranking
def view_recommendation(subjects):
    header("RECOMMENDATION")

    if len(subjects) == 0:
        print("  No subjects to recommend from.")
        return

    # Get the best subject
    best = recommend(subjects)
    score = priority_score(best)

    print("\n  Recommended Subject:", best.name)
    print()
    print("  Reasons:")
    print("    - Exam in", best.days_left(), "day(s)")
    print("    - Difficulty:", best.difficulty, "/ 5")
    print("    - Progress:", best.get_progress(), "%")
    print()
    print("  Priority Score:", score)

    # Show the full ranked list
    print()
    print("  Full Priority Ranking:")
    print()

    ranking = ranked_subjects(subjects)
    rank_number = 1

    for pair in ranking:
        subject = pair[0]
        subject_score = pair[1]

        # Build a simple text progress bar
        filled = int(subject.get_progress() / 5)   # out of 20 characters
        empty = 20 - filled
        bar = "[" + "#" * filled + "." * empty + "]"

        print("  " + str(rank_number) + ".", subject.name)
        print("     Score:", subject_score, "  Progress:", bar, subject.get_progress(), "%")
        print()

        rank_number = rank_number + 1


# Option 5: Delete a subject
def delete_subject(subjects):
    header("DELETE SUBJECT")

    if len(subjects) == 0:
        print("  No subjects to delete.")
        return

    name = input("  Enter subject name to delete : ").strip()
    subject = find_subject(subjects, name)

    if subject == None:
        print("  Subject not found.")
        return

    confirm = input("  Are you sure you want to delete '" + subject.name + "'? (yes/no) : ").strip().lower()

    if confirm == "yes":
        subjects.remove(subject)
        save_subjects(subjects)
        print("  Subject deleted successfully.")
    else:
        print("  Cancelled.")


# Main function - shows the menu and runs the program
def main():
    # Load saved subjects from file when program starts
    subjects = load_subjects()

    print()
    print("=" * 50)
    print("        SMART STUDY PLANNER")
    print("=" * 50)
    print(" ", len(subjects), "subject(s) loaded from saved data.")

    # Keep showing the menu until user chooses to exit
    while True:
        separator()
        print()
        print("  [1] Add Subject")
        print("  [2] Update Study Progress")
        print("  [3] View All Subjects")
        print("  [4] Get Recommendation")
        print("  [5] Delete Subject")
        print("  [6] Exit")
        print()

        choice = input("  Enter choice (1-6) : ").strip()

        if choice == "1":
            add_subject(subjects)
        elif choice == "2":
            update_progress(subjects)
        elif choice == "3":
            view_subjects(subjects)
        elif choice == "4":
            view_recommendation(subjects)
        elif choice == "5":
            delete_subject(subjects)
        elif choice == "6":
            print()
            print("  Goodbye! Good luck with your studies!")
            print()
            break
        else:
            print("  Invalid choice. Please enter a number from 1 to 6.")


# Start the program
if __name__ == "__main__":
    main()
