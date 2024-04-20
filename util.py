from datetime import datetime


def calculate_average(data):
    """
    Calculates the average of a list of numbers.

    Args:
        data: A list of numbers.

    Returns:
        The average of the numbers in the list, or None if the list is empty.
    """
    if not data:
        return None
    return sum(data) / len(data)


def filter_courses_by_Lecturer(courses, Lecturer_id):
    """
    Filters a list of courses based on the Lecturer ID.

    Args:
        courses: A list of course dictionaries or objects.
        Lecturer_id: The ID of the Lecturer to filter by.

    Returns:
        A list of courses taught by the specified Lecturer.
    """
    return [course for course in courses if course.get('Lecturer_id', None) == Lecturer_id]


def save_file(file, filename):
    """
    Saves a file to the specified location.

    Args:
        file: A file object containing the data to be saved.
        filename: The name of the file to save.

    Raises:
        IOError: If there is an error saving the file.
    """
    try:
        with open(filename, 'wb') as f:
            f.write(file.read())
    except IOError as e:
        raise IOError(f"Error saving file: {e}") from e


def format_date_for_display(date):
    """
    Formats a datetime object for user-friendly display.

    Args:
        date: A datetime object.

    Returns:
        A string representing the date in the format 'YYYY-MM-DD'.
    """
    return date.strftime('%Y-%m-%d')


def compute_overall_marks_from_parsed_data(parsed_data):
    """
Computes the overall marks from parsed data.

    Args:
        parsed_data: A list of dictionaries containing the marks of students.

    Returns:
        A list of overall marks for each student.
    """
    overall_marks = []
    for data in parsed_data:
        student_marks = data['marks']
        total_marks = sum(student_marks.values())
        overall_marks.append(total_marks)
    return overall_marks
