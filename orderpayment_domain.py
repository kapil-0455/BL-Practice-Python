from abc import ABC, abstractmethod
from typing import Iterable


# Abstract Base Class
class DicountPolicy(ABC):

    @abstractmethod
    def apply_discount(self, order_total: float) -> float:
        pass


# No Discount
class NoDiscount(DicountPolicy):

    def apply_discount(self, amount: float) -> float:
        return amount


# Percentage Discount
class PercentageDiscount(DicountPolicy):

    def __init__(self, percentage: float):
        if not (0 <= percentage <= 100):
            raise ValueError("Percentage must be between 0 and 100.")
        self.percentage = percentage

    def apply_discount(self, amount: float) -> float:
        return amount * (1 - self.percentage / 100)


# Product Class
class Product:

    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

    def __str__(self) -> str  :
        return f"{self.name} - {self.__price}"


# Order Class
class Order:

    def __init__(self, products, discount: DicountPolicy):
        self.products = list(products)
        self.discount = discount

    # Calculate Total
    def total(self):
        return sum(product.get_price() for product in self.products)

    # Applied polymorphism
    def final_total(self):
        return self.discount.apply_discount(self.total())

    def __str__(self) -> str:
        result = "Order Details\n"

        for product in self.products:
            result += str(product) + "\n"

        result += f"\nTotal Amount : ₹{self.total()}"
        result += f"\nFinal Amount : ₹{self.final_total()}"

        return result


    # using dunder methods

    # obj[index] → obj.__getitem__(index)
    # len(obj) → obj.__len__()
    # print(obj) → obj.__str__()


    # Number of Items
    def __len__(self):
        return len(self.products)

    # Particular Product Finding
    def __getitem__(self, index):
        return self.products[index]




p1 = Product("Laptop", 50000)
p2 = Product("Mouse", 1200)
p3 = Product("Keyboard", 2500)

# Encapsulation
print("Old Mouse Price :", p2.get_price())
p2.set_price(1500)
print("New Mouse Price :", p2.get_price())



# Without Discount
order1 = Order([p1, p2, p3], NoDiscount())
print("\nORDER 1")
print(order1)
print("Number of Items :", len(order1))
print("Second Product :", order1[1])



# percentage discount 
order2 = Order([p1, p2, p3], PercentageDiscount(20))
print("\nORDER 2")
print(order2)
print("Number of Items :", len(order2))
print("First Product :", order2[0])