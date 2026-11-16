import random
import time


def linear_search(array, searchValue):
    for i in range(len(array)):
        if array[i] == searchValue:
            return i
    return -1

arr = [random.randint(1, 100) for _ in range(20)]
start = time.perf_counter()
print(linear_search(arr, random.randint(1, 100)))
end = time.perf_counter()
print(f'Time taken: {end - start} seconds.')