'''
Tuple is same as list 
but immutable 

Used only those testcases where only  read of data is allowed 
'''
# <---------------------------------->
'''
# creating just using parenthesis no element 
my_tuple = ()
print(my_tuple)

# homogenous type elements 
my_tuple_homo = (1 ,2 , 3 , 4 )
print(my_tuple_homo)

# diffrenet elements 
my_tuple_hetro = (1 ,2 , True , "Kapil" )
print(my_tuple_hetro)

# nested tuples and list , dictionary
my_tuple_mixed = (1 ,2 , "Kapil" , ("hi" , 3 , 4) , [1 ,2 , 4,"hello"], {"name": "kapil"})
print(my_tuple_mixed)
'''

# <---------------------------------->
'''
#  create a tuple with a single item
# we cannot create single character without , 
# if we still make it , so it will be the type of String
t = ('hello',)
print(t)
'''

'''#Accessing 
my_tuple = (1 ,2 , True , "Kapil" )
my_tuple_mixed = (1 ,2 , "Kapil" , ("hi" , 3 , 4) , [1 ,2 , 4,"hello"], {"name": "kapil"})

print(my_tuple[3])
print(my_tuple[-1])

print(my_tuple_mixed[3][0]) # nested accessing
print(my_tuple_mixed[-1]["name"]) # in dictionary

# slicing 
print(my_tuple[-1 : -3 : -1])
'''

# PROG 1: Creating a Tuple of Squares and Accessing Specific Elements

square_list = [i**2 for i in range(10)]
square_tuple = tuple(square_list)

print(f'The List of Square of Numbers is : {square_tuple}')
print('Use of index for accessing elements in tuple')
print(f'3rd element: {square_tuple[2]}')
print(f'5th element: {square_tuple[4]}')
print(f'7th element: {square_tuple[6]}')

print(f"First three elemts are : {square_tuple[:3]}")








