import time
import random


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr


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
print(f'The sorted array is {array}.')
value = int(input("Enter the value you want to search for: "))
start = time.perf_counter()
if binary_search(array, value):
    print(f'The value {value} was found.')
else:
    print(f'The value {value} was not found.')
end = time.perf_counter()
print(f'Time taken to search: {end - start} seconds.')