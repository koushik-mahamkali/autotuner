def tim_sort(arr):
    return sorted(arr)

import math

def intro_sort(arr):
    import sys
    sys.setrecursionlimit(10**6)
    maxdepth = (len(arr).bit_length() - 1) * 2
    return _intro_sort(arr, maxdepth)

def _intro_sort(arr, maxdepth):
    if len(arr) <= 1:
        return arr
    elif maxdepth == 0:
        return heap_sort(arr)
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return _intro_sort(left, maxdepth - 1) + middle + _intro_sort(right, maxdepth - 1)

def smart_sort(arr):
    if len(arr) < 32:
        return insertion_sort(arr)
    elif is_nearly_sorted(arr):
        return binary_insertion_sort(arr)
    else:
        return intro_sort(arr)

def is_nearly_sorted(arr):
    count = sum(1 for i in range(1, len(arr)) if arr[i] < arr[i-1])
    return count / len(arr) < 0.1

def binary_insertion_sort(arr):
    from bisect import bisect_left
    for i in range(1, len(arr)):
        key = arr[i]
        j = bisect_left(arr, key, 0, i)
        arr = arr[:j] + [key] + arr[j:i] + arr[i+1:]
    return arr

def heap_sort(arr):  # reused for intro
    import heapq
    h = []
    for value in arr:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for _ in range(len(h))]

def insertion_sort(arr):  # reused for smart
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr