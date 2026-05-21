# storage.py
# This file handles saving and loading data.
# All subject data is saved to a JSON file on disk
# so it is not lost when the program closes.

import json
import os
from subject import Subject

DATA_FILE = "study_data.json"


# Save all subjects to the JSON file
def save_subjects(subjects):
    # Convert each Subject object into a dictionary
    list_of_dicts = []
    for subject in subjects:
        dictionary = subject.to_dict()
        list_of_dicts.append(dictionary)

    # Write the list of dictionaries to the file
    file = open(DATA_FILE, "w")
    json.dump(list_of_dicts, file, indent=2)
    file.close()


# Load all subjects from the JSON file
def load_subjects():
    # If the file does not exist yet, return an empty list
    if os.path.exists(DATA_FILE) == False:
        return []

    # Try to read and load the file
    try:
        file = open(DATA_FILE, "r")
        list_of_dicts = json.load(file)
        file.close()

        # Convert each dictionary back into a Subject object
        subjects = []
        for data in list_of_dicts:
            # Create a blank Subject object
            subject = Subject(data["name"], data["exam_date"], data["difficulty"], data["total_hours"])
            # Fill in the completed hours from saved data
            subject.completed_hours = data["completed_hours"]
            subjects.append(subject)

        return subjects

    except:
        print("  Warning: Data file could not be read. Starting fresh.")
        return []
