
# len/min/max/sorted
# not change permanently in list
'''
L = [7,3,5,6,2,1]
print(len(L))
print(min(L))
print(max(L))
print(sorted(L))
print(sorted(L , reverse=True)) # sorted in reverse 
'''


# count -> return count of elements 
'''
L = [2,4,5,6,5,5,5]
L.count(5)
'''


# index -> return index of count
'''
L = [2,4,5,6,1,5,5,5]
L.index(1)
'''


# reverse -> reverse the list 
'''
L = [2,4,5,6,1,5,5,5]
# permanently reverses the list
L.reverse()
print(L)
'''


# sort (vs sorted)

L = [2,4,5,6,1,5,5,5]
print(L)
print(sorted(L)) # not do permanently changes 
print(L)

L.sort()
print(L)

