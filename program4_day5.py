'''
enumerate() is a built-in Python function that adds a counter (index) to an
iterable (such as a list, tuple, or string) and returns an enumerate object.
'''

# enumerate(iterable, start=0)

'''
iterable → List, tuple, string, etc.
start (optional) → The starting value of the index. By default, it is 0.
'''

# without enumerator 
'''
fruits = ["Apple", "Banana", "Mango"]

index = 0

for fruit in fruits:
    print(index, fruit)
    index += 1
'''

# with enumerator
'''
fruits = ["Apple", "Banana", "Mango"]

# indexing start from 1
for index, fruit in enumerate(fruits , start = 1):
    print(index, fruit)
'''


# PROG 4: To Remove Elements From The List
colors_list = ['Red', 'Green', 'Pink', 'Blue', 'Black', 'Purple', 'Yellow', 'Magenta', 'Brown']

removable_indices = [0 , 2 , 4]
removed_color_list = []
for index , color in enumerate(colors_list):
    if (index not in removable_indices):
        removed_color_list.append(color)
    
print(f'Colors List :  {colors_list} \n')
print(f'List After Removing Particular Elements : {removed_color_list}')