import time
import random

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1

        while j>=0 and array[j]>key:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = key

    return array


if __name__ == '__main__':
    arr = [random.randint(1, 1000) for _ in range(20)]
    start = time.perf_counter()
    print(f'Unsorted array: {arr}')
    print(f'Sorted array: {insertion_sort(arr)}')
    end = time.perf_counter()
    print(f'Time taken: {end - start} seconds.')