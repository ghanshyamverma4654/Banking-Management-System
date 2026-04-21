class Account:
    def __init__(self, name, age, email, pin, account_no, balance=0):
        self.name = name
        self.age = age
        self.email = email
        self.pin = pin
        self.account_no = account_no
        self.balance = balance

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "pin": self.pin,
            "account_no": self.account_no,
            "balance": self.balance
        }