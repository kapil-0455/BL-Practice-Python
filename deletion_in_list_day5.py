"""## Deleting items from a List"""

# <---------------------------------------------------------------------------->
# del -> delete item using del keyword 
#L = [1,2,3,4,5]

# indexing
#del L[2]

# slicing -> delete mutliple elements 
'''
del L[1:3]
print(L)
'''

#<------------------------------------------------------------------------------>
# REMOVE -> remove(element)
# use when we dont know the index of element
'''
L = [1,2,3,4,5]
L.remove(5)
print(L)
'''


#<------------------------------------------------------------------------------>

# POP -> pop(index) as del with index
'''
L = [1,2,3,4,5]
L.pop(3)
print(L)
'''
# if we write without index it delete last index element 
'''
L = [1,2,3,4,5]
L.pop()
print(L)

'''

#<------------------------------------------------------------------------------>

# CLEAR -> clear() 
# remove all elements from list

L = [1,2,3,4,5]
L.clear()
print(L)

