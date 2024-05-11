def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    iterations = 0

    while left <= right:
        mid = (left + right) // 2
        iterations += 1

        if arr[mid] == target:
            return iterations, arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # Якщо цільовий елемент не знайдено, повертаємо кількість ітерацій та верхню межу
    if right < 0:
        return iterations, arr[0]
    elif left >= len(arr):
        return iterations, None
    else:
        return iterations, arr[left]

# Приклад використання:
sorted_array = [0.1, 0.3, 0.5, 0.7, 0.9, 1.2, 1.6, 3.4]
target = 1.5
iterations, upper_bound = binary_search(sorted_array, target)
print("Кількість ітерацій:", iterations)
print("Верхня межа:", upper_bound)