# PROG 1: Full Name With Right Case Structure

def format_full_name(first_name, middle_name, last_name):
    if middle_name:
        name = first_name + " " + middle_name + " " + last_name
        return name.title()
    else:
        name = first_name + " " + last_name
        return name.title()


# Input
first = input("Enter your first name: ")
middle = input("Enter your middle name (if any, else press enter): ")
last = input("Enter your last name: ")

full_name = format_full_name(first, middle, last)
print(f"Formatted Full Name: {full_name}")