__week__ = "week2"
def get_grade(student_grades, student_name):
    try:
        return student_grades[student_name]
    except KeyError:
        return "Student not found in the system"

if __name__ == "__main__":
    students = {"John": 85, "Sara": 92}
    print(get_grade(students, "Sara"))
    print(get_grade(students, "Mark"))
