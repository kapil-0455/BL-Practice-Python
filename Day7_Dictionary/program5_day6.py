def get_friend_detail():
    friends = {
        "Friend1": [{"City": "Delhi", "Pincode": "110001"},{"Email": "friend1@example.com", "PhoneNumber": "1234567890"}],
        "Friend2": [{"City": "Los Angeles", "Pincode": "90001"},{"Email": "friend2@example.com", "PhoneNumber": "2345678901"}],
        "Friend3": [{"City": "Mumbai", "Pincode": "400001"},{"Email": "friend3@example.com", "PhoneNumber": "3456789012"}],
        "Friend4": [{"City": "Chandigarh", "Pincode": "160017"},{"Email": "friend4@example.com", "PhoneNumber": "4567890123"}],
        "Friend5": [{"City": "New York", "Pincode": "33101"},{"Email": "friend5@example.com", "PhoneNumber": "5678901234"}]
    }

    friend_name = input("Enter friend's name (Friend1/Friend2/Friend3/Friend4/Friend5): ")
    detail = input("Enter detail type (City/Pincode/Email/PhoneNumber): ")

    if friend_name in friends:
        
        if detail in friends[friend_name][0] or friends[friend_name][1]:
            if(detail in friends[friend_name][0]):
                print(f"{friend_name}'s {detail} : {friends[friend_name][0][detail]}")
            else :
                print(f"{friend_name}'s {detail} : {friends[friend_name][1][detail]}")

        else:
            print("Invalid detail type!")

    else:
        print("Friend not found!")


get_friend_detail()