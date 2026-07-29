'''

def merge_two_dict(personal_details , virtual_details):
    # using union opertor 
    merge_union = personal_details | virtual_details
    print_dict_after_dict(merge_union)

def print_dict_after_dict(details):
    print('\nMerged Dictionary after removing pincode using del:')
    del details['pincode']
    print(details)



n = int(input("Enter number of persons: "))

for i in range(n):

    print(f"\nEnter details of Person {i+1}")
    
    personal_details = {}
    personal_details["name"] = input("Enter Name: ")
    personal_details["City of Stay"] = input("Enter City: ")
    personal_details["pincode"] = input("Enter pincode: ")

    virtual_details = {}
    virtual_details["Email"] = input("Enter Email: ")
    virtual_details["Phone"] = input("Enter Phone Number: ")

    # Merge and Print
    merge_two_dict(personal_details, virtual_details)
'''


# 3.2 o Remove Data From Dictionary Using pop

def merge_two_dict(personal_details , virtual_details):
    # using union opertor 
    merge_union = personal_details | virtual_details
    print_dict_after_dict(merge_union)

def print_dict_after_dict(details):
    print('\nMerged Dictionary after removing pincode using del:')
    details.pop('pincode')
    print(details)



n = int(input("Enter number of persons: "))

for i in range(n):

    print(f"\nEnter details of Person {i+1}")
    
    personal_details = {}
    personal_details["name"] = input("Enter Name: ")
    personal_details["City of Stay"] = input("Enter City: ")
    personal_details["pincode"] = input("Enter pincode: ")

    virtual_details = {}
    virtual_details["Email"] = input("Enter Email: ")
    virtual_details["Phone"] = input("Enter Phone Number: ")

    # Merge and Print
    merge_two_dict(personal_details, virtual_details)