import random


def buket_size_print(total_numbers):
    numbers = []

    for i in range(total_numbers):
        num = random.uniform(0.0, 100.0)
        numbers.append(num)

    bucket1 = 0   
    bucket2 = 0  
    bucket3 = 0   
    bucket4 = 0   
    bucket5 = 0 

    for number in numbers:
        if(number >=0 and number <= 20):
            bucket1 += 1
        elif (number >=20 and number <= 40):
            bucket2 += 1
        elif (number >=40 and number <= 60):
            bucket3 += 1
        elif (number >=60 and number <= 80):
            bucket4 += 1
        elif (number >=80 and number <= 100):
            bucket5 += 1
        

    print("Bucket 0 to 20 :", bucket1, "numbers")
    print("Bucket 20 to 40:", bucket2, "numbers")
    print("Bucket 40 to 60:", bucket3, "numbers")
    print("Bucket 60 to 80:", bucket4, "numbers")
    print("Bucket 80 to 100:", bucket5, "numbers")

total_numbers = int(input('Enter a number : '))
buket_size_print(total_numbers)