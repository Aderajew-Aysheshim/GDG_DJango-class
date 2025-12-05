scores = {"John": 85, "Sara": 92, "Fraol": 78}

name = input("Enter student name: ")

try:
    print("Score:", scores[name])
except KeyError:
    print("Student not found!")
