''' # Dictionary 

# -> it is a collectuion of key : value pairs
# store data like map 

example :
dict = { 'name' : 'Kapil' , 'age' :22 , 'gender' : 'male' }

characterstics :
1> Mutable
2. No Indexing 
3. Ordered 
3. keys cannot be mutable 
4.keys cannot be duplicate
'''

'''
dict = { 'name' : 'Kapil' , 'age' :22 , 'gender' : 'male' }
# Accessing 
print(dict['name'])
print(dict.get('name'))
'''

'''
Operations

'name' in s -> check name is present in dictionary 


we can iterate over it:
for i in dict:
  print(i,d[i])
'''

''' # retreving components 
.keys() -> returns a dict_keys object containing all the keys of the dictionary
.values() -> retunrs a dict_keys object containning all the values of the dictionary
.items() -> returns a dict_items object containing all the key-value pairs of the dictionary as tuples.


'''


'''### Adding  , update """

dict = { 'name' : 'Kapil' , 'age' :22 , 'gender' : 'male' }

#update
dict['age'] = '23'
print(dict)

# add
dict['weight'] = 72
print(dict)

'''

''' # delete from dictionary

dict = { 'name' : 'Kapil' , 'age' :22 , 'gender' : 'male' }

# delete using del
del dict['age']

# delete using pop remove 
dict.pop('gender')

# delete using popitem -> delete last one
dict.popitem()

print(dict)

'''


# program 1.1 printing friends details 
'''
def print_friend_details(friend_details):

    print('Print details using key')
    for key in friend_details:
        print(f'{key} : {friend_details[key]}')

    print('\nPrint using items')
    # tuple unpacking
    for key , value in friend_details.items():
        print(f'{key} : {value}')
    

friend_details = {'name' : 'Lakshit' , 'place' : 'Rajpura' , 'pincode' : 140401}
print_friend_details(friend_details)
'''

# program 1.2 printing  multiple friends details 

def print_friend_details(friend_details):

    print("\nPrint details using key")
    for key in friend_details:
        print(f"{key} : {friend_details[key]}")

    print("\nPrint using items")
    for key, value in friend_details.items():
        print(f"{key} : {value}")


friends = []

n = int(input("Enter number of friends: "))

for i in range(n):
    print(f"\nEnter details of Friend {i+1}")

    friend_details = {}
    friend_details["name"] = input("Enter name: ")
    friend_details["place"] = input("Enter place: ")
    friend_details["pincode"] = int(input("Enter pincode: "))

    friends.append(friend_details)

print("\n----- Friend Details -----")

for friend in friends:
    print_friend_details(friend)



