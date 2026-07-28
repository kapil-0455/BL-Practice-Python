import re

def check_password(password):
    if len(password) < 8:
        return "Password is invalid."

    if not re.match(r'^[A-Za-z]', password):
        return "Password is invalid."

    if not re.search(r'[a-z]', password):
        return "Password is invalid."

    if not re.search(r'[A-Z]', password):
        return "Password is invalid."

    if not re.search(r'\d', password):
        return "Password is invalid."

    if not re.search(r'[@#$%^&*]', password):
        return "Password is invalid."

    return "Password is valid."


password = input("Enter your password: ")
print(check_password(password))