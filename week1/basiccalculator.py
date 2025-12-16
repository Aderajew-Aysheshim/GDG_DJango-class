print("basic calculator")
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b
def power(a, b):
    return a ** b
def modulus(a, b): 
    return a % b
def floor_divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a // b
def square_root(a):
    if a < 0:
        return "Error: Cannot take square root of negative number"
    return a ** 0.5
def cube_root(a):
    return a ** (1/3)
def percentage(a, b):
    return (a / b) * 100
  
def factorial(n):
    if n < 0:
        return "Error: Factorial of negative number not defined"
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
while True:
    print("\nBasic Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("7. Floor Divide")
    print("8. Square Root")
    print("9. Cube Root")
    print("10. Percentage")
    print("11. Factorial")
    print("12. Exit")

    choice = input("Choose an option: ")

    if choice == '12':
        print("Calculator closed.")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))

    elif choice == '2':
        print("Result:", subtract(num1, num2))

    elif choice == '3':
        print("Result:", multiply(num1, num2))

    elif choice == '4':
        print("Result:", divide(num1, num2))
    elif choice == '5':
        print("Result:", power(num1, num2))
        
    elif  choice=='6':
      print("Result:", modulus(num1, num2))
    elif choice=='7':
        print("Result:", floor_divide(num1, num2))
        
    num3 = input("Enter the number: ")
    if choice=='8':
        print("Result:", square_root(float(num3)))
    elif choice=='9':
        print("Result:", cube_root(float(num3)))
    elif choice=='10':
        print("Result:", percentage(num1, num2))
    elif choice=='11':
        print("Result:", factorial(int(num3)))        
    else:
        print("Invalid choice")
        
