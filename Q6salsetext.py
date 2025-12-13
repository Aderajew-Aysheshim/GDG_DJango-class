
valid_sales = []

with open("sales.txt", "r") as file:
    for line in file:
        try:
            number = int(line.strip()) 
            valid_sales.append(number) 
        except ValueError:
            continue

print("Valid sales:", valid_sales)
print("Total sales =", sum(valid_sales))
valid_sales = []

with open("sales.txt", "r") as file:
    for line in file:
        try:
            number = int(line.strip()) 
            valid_sales.append(number)
        except ValueError:

            continue

print("Valid sales:", valid_sales)
print("Total sales =", sum(valid_sales))
