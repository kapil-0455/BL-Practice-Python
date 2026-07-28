import re

def email_validator(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        return True
    else:
        return False

email = input("Enter email: ")

if email_validator(email):
    print("Valid Email")
else:
    print("Invalid Email")