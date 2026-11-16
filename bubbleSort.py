import time
import random

def bubble_sort(array):
    swap = True
    while swap:
        swap = False
        for i in range(len(array)):
            for j in range(len(array) - i - 1):
                if array[j + 1] < array[j]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    swap = True
    return array

numArray = [random.randint(1, 1000) for _ in range(10)]
start = time.perf_counter()
print(f'Unsorted array: {numArray}')
print(f'Sorted array: {bubble_sort(numArray)}')
end = time.perf_counter()
print(f'Time taken: {end - start} seconds.')