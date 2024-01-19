import timeit
import random

def merge_sort(arr):
    # Реалізація сортування злиттям
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def insertion_sort(arr):
    # Реалізація сортування вставками
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def timsort(arr):
    # Використання вбудованого Timsort в Python
    sorted_arr = sorted(arr)
    return sorted_arr

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

# Реалізація тестування на різних розмірах масивів
array_sizes = [100, 500, 1000, 5000, 10000]

for size in array_sizes:
    # Замір часу для сортування злиттям
    merge_sort_time = timeit.timeit(lambda: merge_sort(generate_random_array(size)), number=1000)

    # Замір часу для сортування вставками
    insertion_sort_time = timeit.timeit(lambda: insertion_sort(generate_random_array(size)), number=1000)

    # Замір часу для Timsort
    timsort_time = timeit.timeit(lambda: timsort(generate_random_array(size)), number=1000)

    # Виведення результатів
    print(f"Розмір масиву: {size}")
    print(f"Сортування злиттям: {merge_sort_time} секунд")
    print(f"Сортування вставками: {insertion_sort_time} секунд")
    print(f"Timsort: {timsort_time} секунд")
    
    # Виведення відношення часу Timsort до інших алгоритмів
    print(f"Відношення часу Timsort до сортування злиттям: {timsort_time/merge_sort_time}")
    print(f"Відношення часу Timsort до сортування вставками: {timsort_time/insertion_sort_time}")
    print("---------------")
