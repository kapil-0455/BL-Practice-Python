import random

SHOP_NAME = "Retail Invoicing App"

HOUSEHOLD_GST = 0.05
PROCESSED_FOOD_GST = 0.12

items = ["Rice", "Wheat Flour", "Sugar", "Salt", "Tea","Coffee", "Biscuits", "Soap", "Shampoo","Toothpaste","Cooking Oil", "Tomato", "Banana", "Masala", "Milk"
]

prices = [60, 45, 50, 20, 180,250, 40, 35, 180, 95,160, 10, 15, 200, 30]

gst_category = [HOUSEHOLD_GST, HOUSEHOLD_GST, HOUSEHOLD_GST, HOUSEHOLD_GST, PROCESSED_FOOD_GST,PROCESSED_FOOD_GST, PROCESSED_FOOD_GST, HOUSEHOLD_GST, HOUSEHOLD_GST, HOUSEHOLD_GST,HOUSEHOLD_GST, HOUSEHOLD_GST, HOUSEHOLD_GST, PROCESSED_FOOD_GST, HOUSEHOLD_GST
]


def select_items():
    selected = []

    while len(selected) < 3:
        index = random.randint(0, len(items) - 1)
        if index not in selected:
            selected.append(index)

    return selected


def print_bill(buyer_name, selected_items):
    total = 0
    gst = 0

    print("\n" + SHOP_NAME)
    print("-" * 40)
    print(f"Buyer Name: {buyer_name}")
    print("-" * 40)
    print(f"| {'Item':^15} | {'Qty':^5} | {'Price':^8} |")
    print("-" * 40)

    for i in selected_items:
        qty = random.randint(1, 5)
        amount = prices[i] * qty
        total += amount
        gst += amount * gst_category[i]

        print(f"| {items[i]:<15} | {qty:^5} | {prices[i]:>8} |")

    print("-" * 40)
    print(f"{'Total':<28} Rs {total:.2f}")
    print(f"{'GST':<28} Rs {gst:.2f}")
    print("-" * 40)
    print(f"{'Total Billing':<28} Rs {total + gst:.2f}")
    print("-" * 40)


buyer_name = input("Enter Buyer Name: ")
selected_items = select_items()
print_bill(buyer_name, selected_items)