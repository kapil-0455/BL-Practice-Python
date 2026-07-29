def friend_type_print(n):
    for i in range(n):
        print(f'\nEnter details of Friend {i+1}')

        friend_details = {}

        friend_details['Name'] = input('Enter Name: ')
        friend_details['City of Stay'] = input('Enter City of Stay: ')
        friend_details['Pincode'] = input('Enter Pincode: ')

        # Add default values
        friend_details.setdefault('Country', 'India')
        friend_details.setdefault('Friend-Type', '')

        print('\nDictionary after adding default values:')
        print_dict(friend_details)

        friend_type = ['School' , 'College' , 'Neighbourhood' ]
        print('\n Select Friend Type')
        for idx , option in enumerate(friend_type , start=1):
            print(f'{idx}, {option}')

        choice = int(input('Enter the number corresponding to the Friend Type: '))

        if choice >= 1 and choice <= len(friend_type):
            friend_details['Friend-Type'] = friend_type[choice-1]
        else :
            print('Enter a valid choice')

        print("\nDictionary after setting 'Friend-Type':")
        print_dict(friend_details)

def print_dict(friend_details):
    print('\nKeys:', friend_details.keys())
    print('Values:', friend_details.values())
    print('Items:', friend_details.items())


n = int(input('Enter number of friends: '))
friend_type_print(n)

