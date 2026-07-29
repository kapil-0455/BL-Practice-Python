''' # Set
characterstics -:
1. mutable
2. No duplicate value
3. Unordered
4. cannot have mutable datatypes 
'''
#<---------------------------------------------------------------------->
'''
# Converting a list to a set using the set() method
    my_list = [1, 2, 3]
    s1 = set(my_list)
    print(s1)
'''

#<---------------------------------------------------------------------->
'''
# not allowed mean cannot have mutables in it
    my_set = {1 , 2 , 3 , 4 , {'name' : 'kapil'}}
    print(my_set)
'''

'''
# prove it is unordered
    my_set2 = {1 ,2 ,3}
    my_set3 = {3 , 2 ,1 }
    print(my_set2 == my_set3) # return true means unordered 
'''


#<---------------------------------------------------------------------->
'''
# Adding a single integer to a set
    s1 = {1, 2, 3}
    s1.add(6)
    print(s1)

# Updating a set with a list and another set
    s1 = {1, 2, 3}
    s2 = {2, 3, 4, 5}
    s1.update(s2, [7, 8, 9])
    print(s1)
'''

#<---------------------------------------------------------------------->
'''
# Removing an element using remove()
    s1 = {1, 2, 3, 4, 5}
    s1.remove(5)
    print(s1)

# Using discard() to prevent key errors if an element doesn't exist
    s1 = {1, 2, 3, 4, 5}
    s1.discard(10) # Does not raise an error
    s1.discard(3)  # Removes 3

    s1.pop() # remove randomly in set
    print(s1)
'''

#<---------------------------------------------------------------------->
'''

# Initializing sets for operations
    s1 = {1, 2, 3}
    s2 = {2, 3, 4}
    s3 = {3, 5}

# Intersection between two sets -> find out commons
    s4 = s1.intersection(s2) -> take list also
    print(s4) # {2, 3}

# Intersection among three sets
    print(s1.intersection(s2, s3)) # {3}

# Difference (s1 relative to s2) -> not include s2 
    s4 = s1.difference(s2)
    print(s4) # {4}

# Difference (s2 relative to s1) -> not include s1 
    s4 = s2.difference(s1)
    print(s4)

# Symmetric Difference (uncommon elements across both sets)
    s4 = s1.symmetric_difference(s2) 
    print(s4) # {1, 4}

# Union (all elements combined from both sets)
    s4 = s1.union(s2)
    print(s4) #{1, 2, 3, 4}

'''

'''
# Union(|)
s1 | s2
# Intersection(&)
s1 & s2
# Difference(-)
s1 - s2
s2 - s1
# Symmetric Difference(^)
s1 ^ s2
'''

#<---------------------------------------------------------------------->
''' # frozenset it is immutable set type

# Creating an immutable frozen set
    friends = frozen_set(["Alice", "Bob"]) # Note: standard syntax is frozenset()

# Attempting to add an element to a frozen set (Raises an AttributeError)
    friends.add("Charlie")
    print(friends)
'''

'''

# PROG 3.1: Swapping Variables Using Traditional Method
    a = int(input('Enter first Numeber : '))
    b = int(input('Enter Second Numeber : '))

    print(f'Initial Value of a & b are \na = {a} \nb = {b}')
    temp = a
    a = b
    b = temp
    print(f'After traditional swapping: \na = {a} \nb = {b}')
'''

'''
# PROG 3.2: Swapping Variables Using Pythonic Method
    a = int(input('Enter first Numeber : '))
    b = int(input('Enter Second Numeber : '))

    print(f'Initial Value of a & b are \na = {a} \nb = {b}')

    a , b = b , a
    print(f'After traditional swapping: \na = {a} \nb = {b}')
'''

# PROG 3.3: Swapping Variables Using Tuple Packing and Unpacking
def swap(x, y):
    return y, x

# Taking user input
a = input("Enter value of a: ")
b = input("Enter value of b: ")

print(f'Initial Value of a & b are \na = {a} \nb = {b}')
# Calling the function and unpacking the returned values
m, n = swap(a, b)

print(f'After traditional swapping: \na = {a} \nb = {b}')

