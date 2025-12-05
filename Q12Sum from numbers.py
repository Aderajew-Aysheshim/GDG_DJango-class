total = 0

with open("numbers.txt", "r") as file:
    for line in file:
        try:
            total += int(line.strip())
        except:
            pass  # ignore invalid lines

print("Sum =", total)
