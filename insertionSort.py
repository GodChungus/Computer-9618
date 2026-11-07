import time
import random

def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1

        while j>=0 and array[j]>key:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = key

    return array

arr = [random.randint(1, 1000) for _ in range(50)]
start = time.perf_counter()
print(insertionSort(arr))
end = time.perf_counter()
print(end - start)