import random
import time


def generate_numbers(size):
    numbers = [random.randint(1 , 100) for i in range(size)]
    return numbers


def generate_prime_list(n):
    if n < 2:
        return []

    isPrime = [False] * (n + 1)
    isPrime[0] = True
    isPrime[1] = True

    i = 2
    while i * i <= n:
        if (isPrime[i] == False):
            j = 2
            while (j * i <= n):
                isPrime[j * i] = True
                j += 1
        i += 1

    prime_list = [num for num in range(2, n+1) if  isPrime[i] == False]
    return prime_list

def remove_prime_numbers(numbers):
    # Prime numbers between 1 and 100
    prime_list = generate_prime_list(100)
    new_list = [number for number in numbers if number is not prime_list]

    return new_list


def execution_time(size):

    print("Computing execution time for list size:", size)

    start = time.time()
    numbers = generate_numbers(size)
    end = time.time()
    generation_time = end - start

    start = time.time()
    new_list = remove_prime_numbers(numbers)
    end = time.time()
    remove_time = end - start

    total_time = generation_time + remove_time

    print(f"Time taken to generate random numbers: {generation_time:.6f} seconds")
    print(f"Time taken to remove prime numbers: {remove_time:.6f} seconds")
    print(f"Total execution time: {total_time:.6f} seconds")


sizes = [100, 10000, 100000]

for size in sizes:
    execution_time(size)