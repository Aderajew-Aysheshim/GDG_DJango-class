from abc import ABC, abstractmethod

class Account(ABC): #
    @abstractmethod
    def get_account_type(self): #
        pass

class SavingsAccount(Account): #
    def get_account_type(self):
        return "Savings Account"

class CurrentAccount(Account): #
    def get_account_type(self):
        return "Current Account"
import json

# Account types are stored in JSON
accounts_json = """
[
{"type": "SavingsAccount"},
{"type": "CurrentAccount"},
{"type": "SavingsAccount"}
]
"""
account_data = json.loads(accounts_json)
created_accounts = []

for account in account_data:
    account_type = account["type"]
    if account_type == "SavingsAccount":
        created_accounts.append(SavingsAccount())
    elif account_type == "CurrentAccount":
        created_accounts.append(CurrentAccount())

# Access polymorphically
for acc in created_accounts:
    print(f"Processing: {acc.get_account_type()}")
