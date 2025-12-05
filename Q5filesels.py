# Just open and read the sales.txt file (no calculations yet)
with open("sales.txt", "r") as file:
    for line in file:
        print(line.strip())
