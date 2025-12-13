

def sum_numbers_from_file(filename="numbers.txt"):
    total = 0
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                try:
                    total += int(line)
                except ValueError:
                    continue
    except FileNotFoundError:
        return None
    return total


if __name__ == "__main__":
    res = sum_numbers_from_file("numbers.txt")
    if res is None:
        print("numbers.txt missing")
    else:
        print("Sum =", res)
