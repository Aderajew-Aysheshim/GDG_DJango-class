grades = {"John": "A", "Sara": "B", "Musa": "A"}

reversed_dict = {}

for name, grade in grades.items():
    if grade not in reversed_dict:
        reversed_dict[grade] = []
    reversed_dict[grade].append(name)

print(reversed_dict)
