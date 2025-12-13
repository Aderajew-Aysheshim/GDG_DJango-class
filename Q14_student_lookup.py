
def lookup_student(scores, name):
    try:
        return scores[name]
    except KeyError:
        return "Student not found!"


if __name__ == "__main__":
    scores = {"John": 85, "Sara": 92, "Fraol": 78}
    print(lookup_student(scores, "Mark"))
    print(lookup_student(scores, "Sara"))
