from insertionSort import insertion_sort
import time
import random


def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False


array = insertion_sort([random.randint(1, 100) for _ in range(20)])
value = int(input("Enter the value you want to search for: "))
start = time.perf_counter()
if binary_search(array, value):
    print(f'The value {value} was found.')
else:
    print(f'The value {value} was not found.')
end = time.perf_counter()
print(f'Time taken to search: {end - start} seconds.')