def take_highest_note(students):
    """
    :param students: a list of dictionaries with "name" and "notes" keys
    :type students: list
    :return: a list of dictionaries with "name" and "top_note" keys,
    where the "top_note" is the highest note for that student
    If a student has no notes (an empty list), returns top_note: 0.
    :rtype: list
    """

    if not isinstance(students, list):
        raise TypeError("students must be a list of dictionaries")

    students_top_notes = []
    for student in students:
        if not isinstance(student, dict):
            raise TypeError("each student must be a dictionary")
        if "name" not in student or "notes" not in student:
            raise ValueError("each student dictionary must have 'name' and 'notes' keys")
        top_note = max(student["notes"]) if student["notes"] else 0
        student_top_note = {"name": student["name"], "top_note": top_note}
        students_top_notes.append(student_top_note)
    return students_top_notes


def main():
    students = [
        {"name": "John", "notes": [3, 5, 4]},
        {"name": "Mich", "notes": [-1, 3, 5.5]},
        {"name": "Michal", "notes": []},  # empty notes lists will return 0
        # {"name": "Tamir"},  # missing 'notes' key
        # "not a dictionary"  # not a dictionary
    ]
    try:
        students_top_notes = take_highest_note(students)
    except (TypeError, ValueError) as e:
        print("Error:", e)
    else:
        print(students_top_notes)


if __name__ == "__main__":
    main()
