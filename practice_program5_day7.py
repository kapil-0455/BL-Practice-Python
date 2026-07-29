def update_access(access, current):
    set1 = set()
    for name in access.split(","):
        set1.add(name.strip().lower())

    set2 = set()
    for name in current.split(","):
        set2.add(name.strip().lower())

    set1.intersection_update(set2)

    print("Updated Access Rights List:")
    for name in set1:
        print(name.capitalize())


access = input("Enter the employees with access rights (comma-separated): ")
current = input("Enter the current employees (comma-separated): ")

update_access(access, current)