__week__ = "week2"

def reverse_dict(d):
    out = {}
    for k, v in d.items():
        out.setdefault(v, []).append(k)
    return out


if __name__ == "__main__":
    grades = {"John": "A", "Sara": "B", "Musa": "A"}
    print(reverse_dict(grades))
