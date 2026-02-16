import json #

json_string = """
{
"product": "Laptop",
"price": 75000,
"available": true
}
""" #

# Convert it into a Python dictionary
data = json.loads(json_string) #

# Print the product name and price
print(f"Product Name: {data['product']}")
print(f"Price: {data['price']}")
