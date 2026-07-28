import re

def remove_digits(string):
    pattern = r'\D'
    return re.findall(pattern, string)

string = input('Enter a String : ')
new_string = remove_digits(string)
new_string = "".join(new_string)

print(f'Input String : {string}')
print(f'Output String without numbers : {new_string}')



