
def merge_two_dict(personal_details , virtual_details):
    # using update mehtod 
    merge_update = personal_details.copy()
    merge_update.update(virtual_details)

    # using unpacking 
    merge_unpacking = {**personal_details , **virtual_details}

    # using union opertor 
    merge_union = personal_details | virtual_details

    # using Ior 
    merge_ior = personal_details.copy()
    merge_ior |= virtual_details

    print_dict(merge_update)
    print_dict(merge_unpacking)
    print_dict(merge_union)
    print_dict(merge_ior)

def print_dict(details):
    print('\n')
    print(f'Using key method : {details.keys()}')
    print(f'Using Values method : {details.values()}')
    print(f'Using Items method : {details.items()}')



n = int(input("Enter number of persons: "))

for i in range(n):

    print(f"\nEnter details of Person {i+1}")
    
    personal_details = {}
    personal_details["name"] = input("Enter Name: ")
    personal_details["age"] = int(input("Enter Age: "))
    personal_details["city"] = input("Enter City: ")

    virtual_details = {}
    virtual_details["email"] = input("Enter Email: ")
    virtual_details["phone"] = input("Enter Phone Number: ")

    # Merge and Print
    merge_two_dict(personal_details, virtual_details)