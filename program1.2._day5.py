# PROG 1.2: Taking List From The User
def custom_sum(numbers):
    total_sum = 0
    for i in numbers:
        total_sum += i
    return total_sum


n = int(input('Enter the number of elements in the list: '))
numbers = []

for _ in range(n):
    while True:
        try:
            number = int(input('Enter a number: '))
            numbers.append(number)
            break
        except ValueError :
            print('Invalid input, please enter a valid number.')

print(f'Original List : {numbers}')

custom = custom_sum(numbers)
print(f'The Sum of the list using Custom function is {custom}')

built_in_sum = sum(numbers)
print(f'The Sum of the list using Builtin function is {built_in_sum}')

#comparing 
print(f'Comparing the results of Custom function and Builtin function: {custom == built_in_sum}')

