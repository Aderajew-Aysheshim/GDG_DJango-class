__question__ = """
Python Practice Question 6:
Write a program that:
a, Reads every line in sales.txt
b, Converts valid lines into integers
c, Skips invalid lines (like "abc") using exception handling
d, Stores the valid numbers in a list
e, Calculates and prints the total sales
"""

valid_sales = []

with open("sales.txt", "r") as file:
    for line in file:
        try:
            number = int(line.strip())  # convert to integer
            valid_sales.append(number)  # store valid number
        except ValueError:
            continue

print("Valid sales:", valid_sales)
print("Total sales =", sum(valid_sales))
valid_sales = []

with open("sales.txt", "r") as file:
    for line in file:
        try:
            number = int(line.strip())  # convert to integer
            valid_sales.append(number)  # store valid number
        except ValueError:

            continue

print("Valid sales:", valid_sales)
print("Total sales =", sum(valid_sales))
