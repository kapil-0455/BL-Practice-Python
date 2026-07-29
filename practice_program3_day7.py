def update_members(current, renewed):
    set1 = set()
    for name in current.split(","):
        set1.add(name.strip().lower())

    set2 = set()
    for name in renewed.split(","):
        set2.add(name.strip().lower())


    set1.symmetric_difference_update(set2)

    return set1


current = input("Enter the names of current members (comma-separated): ")
renewed = input("Enter the names of renewed members (comma-separated): ")

updated = update_members(current, renewed)

print("Updated club members list:")
for name in updated:
    print(name.capitalize())