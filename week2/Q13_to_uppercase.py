__week__ = "week2"

def print_uppercase(filename="message.txt"):
    try:
        with open(filename, "r") as f:
            for line in f:
                print(line.strip().upper())
    except FileNotFoundError:
        print("File not found")


if __name__ == "__main__":
    print_uppercase("message.txt")
