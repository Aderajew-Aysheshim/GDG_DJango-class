
__question__ = """
Python Practice Question 1:
A shop gives a discount if a customer buys more than 3 items.
Write a program that asks the user for the number of items they want
to buy and prints:
"Discount applied" if items > 3
"No discount" otherwise
"""

items = int(input("Enter the number of items you want to buy: "))
def discount(items):
   if items > 3:
      print("Discount applied")
   else:
      print("No discount")
    
    discount(items)