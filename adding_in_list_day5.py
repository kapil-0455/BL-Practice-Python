# append()
# add only one element 
'''
L = [1,2,3,4,5]
L.append('Kapil')
print(L)
'''

# append as a one whole item not add single single items
'''
L = [1,2,3,4,5]
L.append([6,7,8])
print(L)
'''

#<---------------------------------------------------------------------------------->
# EXTEND -> extend()
# add mutliple items in it
'''
L = [1,2,3,4,5]
L.extend([6,7,8])
print(L)
'''

###-> example 
'''
L = [1,2,3,4,5]
L.extend('Guragram')
print(L)
'''
#<---------------------------------------------------------------------------------->
# INSERT -> insert(index , element)
# append element on a particular index

L = [1,2,3,4,5]

L.insert(1,100)
print(L)

