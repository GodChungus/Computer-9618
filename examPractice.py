# This is a file containing everything non-OOP that we've done till now in class.
# AKA the things that are coming up in the practical exam.
# Wish me luck. It's tomorrow. Or not. Nobody's reading this anyway.

import random


def linear_search(arr, search_value):
    for i in range(len(arr)):
        if arr[i] == search_value:
            return True
    return False


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def binary_search(arr, search_value):
    first, last = 0, len(arr) - 1
    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == search_value:
            return True
        elif arr[mid] < search_value:
            first = mid + 1
        else:
            last = mid - 1
    return False


test_array = [random.randint(1, 100) for _ in range(20)]
print(f'Here\'s the normal array: {test_array}')
search = int(input("Enter the number you want to search: "))

if not linear_search(test_array, search):
    print("The number was not found.")
else:
    print("The number was found.")

print(f'Here\'s the bubble sort: {bubble_sort(test_array)}')
print(f'Here\'s the insertion sort: {insertion_sort(test_array)}')

print(f'Okay, let\'s take a detour for a bit. Now comes binary search!')

binary_search_value = int(input("Enter the number you want to search: "))

if binary_search(test_array, binary_search_value):
    print("The number was found.")
else:
    print("The number was not found.")
