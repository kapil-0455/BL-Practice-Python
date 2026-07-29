def check_emails(current, new):
    set1 = set()
    for email in current.split(","):
        set1.add(email.strip())

    set2 = set()
    for email in new.split(","):
        set2.add(email.strip())

    if set1.isdisjoint(set2):
        print("There are no common email addresses between current subscribers and new sign-ups.")
    else:
        print("The following email addresses are present in both lists:")
        common = set1.intersection(set2)
        for email in common:
            print(email)


current = input("Enter the current subscribers' emails (comma-separated): ")
new = input("Enter the new sign-ups' emails (comma-separated): ")

check_emails(current, new)