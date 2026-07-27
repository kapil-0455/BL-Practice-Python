# PROG 1.1: By Using Hard-Coded List
def custom_sum(numbers):
    total_sum = 0
    for i in numbers:
        total_sum += i
    return total_sum

numbers = [29, 45, 32, 49, 37]

print(f'Original List : {numbers}')

custom = custom_sum(numbers)
print(f'The Sum of the list using Custom function is {custom}')

built_in_sum = sum(numbers)
print(f'The Sum of the list using Builtin function is {built_in_sum}')

#comparing 
print(f'Comparing the results of Custom function and Builtin function: {custom == built_in_sum}')