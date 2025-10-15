def binary_search(arr, target):
    """
    Функция бинарного поиска.
    Принимает отсортированный массив и искомое значение.
    Возвращает индекс элемента или -1, если не найден.
    """
    left = 0  # Левая граница поиска
    right = len(arr) - 1  # Правая граница поиска

    while left <= right:
        # Находим середину массива
        mid = left + (right - left) // 2 # Избегаем переполнения

        # Проверяем средний элемент
        if arr[mid] == target:
            return mid  # Элемент найден, возвращаем индекс
        # Если искомый элемент меньше среднего
        elif arr[mid] > target:
            right = mid - 1  # Перемещаемся влево, искомое в левой половине
        else: # arr[mid] < target
            left = mid + 1   # Перемещаемся вправо, искомое в правой половине

    return -1  # Элемент не найден

def print_result(arr, target, index):
    """Функция для вывода результата поиска."""
    print(f"Массив: {arr}")
    print(f"Ищем: {target}")
    if index != -1:
        print(f"Элемент найден на позиции: {index}")
    else:
        print("Элемент не найден")

# Пример использования
if __name__ == "__main__":
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7

    result_index = binary_search(sorted_array, target)
    print_result(sorted_array, target, result_index)
