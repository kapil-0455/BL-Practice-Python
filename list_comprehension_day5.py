'''
List Comprehension provides a concise way of creating lists.


Advantages of List Comprehension
- More time-efficient and space-efficient than loops.
- Require fewer lines of code.
- Transforms iterative statement into a formula.
'''
#newlist = [expression for item in iterable if condition == True]
'''
L = [i for i in range(1,11)]
print(L)
'''

basket = ['apple','guava','cherry','banana']
my_fruits = ['apple','kiwi','grapes','banana']
new_list = [fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a')]
print(new_list)

# just same like 
'''

# just include fruit and then these conditions
for fruit in my_fruits:
    if fruit in basket:
        if fruit.startswith('a'):
            new_list.append(fruit)
'''

