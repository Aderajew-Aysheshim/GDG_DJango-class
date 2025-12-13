def read_sales_file(name="sales.txt"):
    with open(name, "r") as file:
        for line in file:
            print(line.strip())


read_sales_file()
