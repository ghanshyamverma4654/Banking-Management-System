import random
import string

def generate_account_number():
    alpha = random.choices(string.ascii_letters, k=3)
    num = random.choices(string.digits, k=5)
    return ''.join(alpha + num)

def validate_pin(pin):
    return len(str(pin)) in range(4, 7)

def validate_age(age):
    return age >= 18