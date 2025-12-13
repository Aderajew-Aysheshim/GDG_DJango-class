valid_sales = []

with open("sales.txt", "r") as file:
    for line in file:
        try:
            number = int(line.strip())   # convert to integer
            valid_sales.append(number)   # store valid number
        except ValueError:
           
           continue

print("Valid sales:", valid_sales)
print("Total sales =", sum(valid_sales))
