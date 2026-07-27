# PROG 2.1: By Using Slicing

# [start: stop : steps] -> slicing values
# we can also give negative indeices too
# [-2 : -6] -> first paramter always bigger 

def reverse_list (numbers):
    return numbers[::-1]

numbers = [29, 45, 32, 49, 37]

reversed_list = reverse_list(numbers)
print(f'The Original List is {numbers}')
print(f'The Reversed List using slicing is {reversed_list}')