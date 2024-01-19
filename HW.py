import timeit
import random

def merge_sort(arr):
    # Реалізація сортування злиттям
    pass

def insertion_sort(arr):
    # Реалізація сортування вставками
    pass

def timsort(arr):
    # Використання вбудованого Timsort в Python
    sorted_arr = sorted(arr)
    return sorted_arr

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

# Замір часу для сортування злиттям
merge_sort_time = timeit.timeit(lambda: merge_sort(generate_random_array(1000)), number=1000)

# Замір часу для сортування вставками
insertion_sort_time = timeit.timeit(lambda: insertion_sort(generate_random_array(1000)), number=1000)

# Замір часу для Timsort
timsort_time = timeit.timeit(lambda: timsort(generate_random_array(1000)), number=1000)

# Виведення результатів
print(f"Сортування злиттям: {merge_sort_time} секунд")
print(f"Сортування вставками: {insertion_sort_time} секунд")
print(f"Timsort: {timsort_time} секунд")
