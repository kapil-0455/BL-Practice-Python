in_stock = {'apple', 'watermelon', 'mango'}
out_of_stock = {'banana', 'orange', 'melon'}


def update_stock(fruit, status):
    fruit = fruit.lower()

    if status == "in":
        out_of_stock.discard(fruit)
        in_stock.add(fruit)
        print(f"\n{fruit.title()} has been added to in-stock.")

    elif status == "out":
        in_stock.discard(fruit)
        out_of_stock.add(fruit)
        print(f"\n{fruit.title()} has been moved to out-of-stock.")

    else:
        print("\nInvalid status! Enter 'in' or 'out'.")

while True:
    print("\n--- Fruit Store Inventory Management ---")
    print("1. Check if a fruit is in stock")
    print("2. List all items in the store")
    print("3. Update stock (add/remove item)")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        fruit = input("Enter the name of the fruit to check: ").lower()

        if fruit in in_stock:
            print(f"{fruit.title()} is in stock.")
        else:
            print(f"{fruit.title()} is not in stock.")

    elif choice == "2":
        print("\nThe possible items that the store keeps are:")
        all_items = in_stock.union(out_of_stock)

        for item in sorted(all_items):
            print(item.title())

    elif choice == "3":
        fruit = input("Enter the name of the fruit: ")
        status = input("Enter 'in' if the item is now in stock or 'out' if it is out of stock: ").lower()

        update_stock(fruit, status)

    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")