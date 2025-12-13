# Just open and read the sales.txt file (no calculations yet)
__question__ = """
Python Practice Question 5:
You receive a file called sales.txt where each line should contain a sales number.
Example:
200
450
abc
700
"""


# Just open and read the sales.txt file (no calculations yet)
def read_sales_file(name="sales.txt"):
    with open(name, "r") as file:
        for line in file:
            print(line.strip())


read_sales_file()
