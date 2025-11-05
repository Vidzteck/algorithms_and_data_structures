def reverse_string(s):
    # Базовый случай: если строка пустая или состоит из одного символа
    if len(s) <= 1:
        return s
    # Рекурсивный случай: последний символ + рекурсивный вызов для остальной части
    return s[-1] + reverse_string(s[:-1])

# Тестирование
test_str = "hello"
print(f"Оригинал: {test_str}")
print(f"Перевёрнутая: {reverse_string(test_str)}")

#Вывод
#Оригинал: hello
#Перевёрнутая: olleh
