import timeit
import sys

L = list(range(1000))
T = tuple(range(1000))

print('List size',sys.getsizeof(L))
print('Tuple size',sys.getsizeof(T))

# timeit take two argumnets one if function and other is how many numbers of times it will run 
list_time = timeit.timeit(lambda: list(range(100000)), number=3)
tuple_time = timeit.timeit(lambda: tuple(range(100000)), number=4)
print(f'Tuple creation time : {tuple_time}')
print(f'List creation time : {list_time}')
