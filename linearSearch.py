import random
import time


def linearSearch(array, searchValue):
    for i in range(len(array)):
        if array[i] == searchValue:
            return i
    return -1

arr = [random.randint(1, 100) for _ in range(50)]
start = time.perf_counter()
print(linearSearch(arr, random.randint(1, 100)))
end = time.perf_counter()
print(end - start)