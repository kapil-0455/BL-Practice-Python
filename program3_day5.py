# PROG 3: Lambda Function


'''
A lambda function is a small,anonymous (nameless)
function that can have any number of arguments but only one expression.
'''

'''
map can iterate over a list , tuple , dictionary 
mostly used with lambda 
take two argumnets (function() , anything where you can iterate )
it return map not list tuple or anything likewise 
'''


'''
eg -> 
maximum = lambda a, b: a if a > b else b
print(maximum(15, 20))
'''

'''
# it can also take single value 

upper_case = lambda string : string.upper()
print(upper_case('hi my name is kapil'))
'''

org_list = [1, 2, 3, 4, 5]
print(f'Original list is {org_list}')


doubled_list = list(map(lambda x : x * 2 , org_list))
print(f'Doubled list is {doubled_list}')
