import random
import timeit


sizes = [100, 1000, 5000]
results = {}

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j]:
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_i = 0
    right_i = 0

    while left_i < len(left) and right_i < len(right):
        if left[left_i] <= right[right_i]:
            merged.append(left[left_i])
            left_i += 1
        else:
            merged.append(right[right_i])
            right_i += 1

    while left_i < len(left):
        merged.append(left[left_i])
        left_i += 1

    while right_i < len(right):
        merged.append(right[right_i])
        right_i += 1

    return merged

def tim_sort(arr):
    return sorted(arr)

for size in sizes:
    arr = [random.randint(0, size) for _ in range(size)]
    results[size] = {
        'insertion': timeit.timeit(lambda: insertion_sort(arr.copy()), number=1),
        'merge': timeit.timeit(lambda: merge_sort(arr.copy()), number=1),
        'timsort': timeit.timeit(lambda: tim_sort(arr.copy()), number=1),
    }

for size in sizes:
    print(f"\nМасив розміру: {size}")
    for k, v in results[size].items():
        print(f"{k.title()} sort: {v:.6f} сек.")