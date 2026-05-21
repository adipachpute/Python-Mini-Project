# planner.py
# This file contains the recommendation logic.
# It calculates a priority score for each subject
# and returns the one the student should study first.

from subject import Subject


# Calculate the priority score for one subject
def priority_score(subject):
    urgency    = 10 / subject.days_left()         # higher when exam is close
    importance = subject.difficulty * 2            # higher when subject is hard
    remaining  = (1 - subject.get_progress() / 100) * 5  # higher when less is studied

    score = importance + urgency + remaining
    score = round(score, 2)
    return score


# Find and return the subject with the highest priority score
def recommend(subjects):
    if len(subjects) == 0:
        return None

    best_subject = subjects[0]
    best_score = priority_score(subjects[0])

    # Loop through all subjects and find the one with highest score
    for subject in subjects:
        score = priority_score(subject)
        if score > best_score:
            best_score = score
            best_subject = subject

    return best_subject


# Return all subjects sorted from highest to lowest priority score
def ranked_subjects(subjects):
    # First create a list of pairs: (subject, score)
    scored_list = []
    for subject in subjects:
        score = priority_score(subject)
        pair = (subject, score)
        scored_list.append(pair)

    # Sort the list by score, highest first
    # Using a simple bubble sort so it is easy to understand
    n = len(scored_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if scored_list[j][1] < scored_list[j + 1][1]:
                # Swap the two pairs
                temp = scored_list[j]
                scored_list[j] = scored_list[j + 1]
                scored_list[j + 1] = temp

    return scored_list
