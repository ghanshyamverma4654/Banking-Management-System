import json
from pathlib import Path
from models.account import Account
from utils.helpers import generate_account_number, validate_pin, validate_age

class BankService:
    def __init__(self, db_path=r"D:\Banking-Management-System\data\database.json"):
        self.db_path = db_path
        self.data = self.load_data()

    def load_data(self):
        if Path(self.db_path).exists():
            with open(self.db_path, "r") as f:
                return json.load(f)
        return []

    def save_data(self):
        with open(self.db_path, "w") as f:
            json.dump(self.data, f, indent=4)

    def create_account(self, name, age, email, pin):
        if not validate_age(age):
            raise ValueError("Age must be 18+")

        if not validate_pin(pin):
            raise ValueError("Pin must be 4–6 digits")

        account_no = generate_account_number()

        account = Account(name, age, email, pin, account_no)

        self.data.append(account.to_dict())
        self.save_data()

        return account_no

    def deposit(self, account_no, pin, amount):
        user = self._find_user(account_no, pin)
        if amount <= 0:
            raise ValueError("Invalid amount")

        user["balance"] += amount
        self.save_data()

        return user["balance"]

    def withdraw(self, account_no, pin, amount):
        user = self._find_user(account_no, pin)

        if amount > user["balance"]:
            raise ValueError("Insufficient balance")

        user["balance"] -= amount
        self.save_data()

        return user["balance"]

    def get_account(self, account_no, pin):
        return self._find_user(account_no, pin)

    def delete_account(self, account_no, pin):
        user = self._find_user(account_no, pin)
        self.data.remove(user)
        self.save_data()
        return True

    def _find_user(self, account_no, pin):
        for user in self.data:
            if user["account_no"] == account_no and user["pin"] == pin:
                return user
        raise ValueError("Invalid credentials")
    
    def get_statistics(self):
        if not self.data:
            return {}

        balances = [user["balance"] for user in self.data]

        return {
            "total_users": len(self.data),
            "total_balance": sum(balances),
            "average_balance": sum(balances)/len(balances),
            "max_balance": max(balances),
            "min_balance": min(balances)
        }    