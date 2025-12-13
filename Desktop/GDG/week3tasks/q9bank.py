class BankAccount:
    def __init__(self):
        self.__balance = 0 

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance! Withdrawal denied.")
        elif amount <= 0:
            print("Withdrawal amount must be positive")
        else:
            self.__balance -= amount
            print(f"Withdrew: {amount}")

    def get_balance(self):
        return self.__balance


# Testing
account = BankAccount()
account.deposit(1000)
account.withdraw(500)  
account.withdraw(600)     
print("Current Balance:", account.get_balance())
account.withdraw(-100)    
account.deposit(-200)     