def get_grade(student_grades, student_name):
    try:
        return student_grades[student_name]
    except KeyError:
        return "Student not found in the system"

# Tests
grades = {"John": 85, "Sara": 92, "Fraol": 78}
print(get_grade(grades, "Sara"))   # 92
print(get_grade(grades, "Mark"))   # "Student not found in the system"
print(get_grade(grades, "John"))   # 85
print(get_grade(grades, "Fraol"))  # 78
print(get_grade(grades, "Anna"))   # "Student not found in the system"

print(get_grade(grades, "Sara"))   # 92
print(get_grade(grades, "Mark"))   # "Student not found in the system"