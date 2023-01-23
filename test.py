# Задача: Написать программу, которая из имеющегося массива строк формирует массив из строк, длина которых меньше либо равна 3 символа. Первоначальный массив можно ввести с клавиатуры, либо задать на старте выполнения алгоритма. При решении не рекомендуется пользоваться коллекциями, лучше обойтись
# исключительно массивами.
# Примеры:
# ["hello", "2", "world", ":-)"] -> ["2", ":-)"]
# ['1234", "1567", "-2", "computer science"] -> ["-2"]
# ["Russia", "Denmark", "Kazan"] -> []


# 1-ый Вариант

# def some_func(array):
#     result = []
#     for word in array:
#         if 0 < len(word) <= 3:
#             result.append(word)
#     return result


# print(some_func(["hello", "2", "world", ":-)"]))
# print(some_func(["1234", "1567", "-2", "computer science"]))
# print(some_func(["Russia", "Denmark", "Kazan"]))


# 2-ой Вариант

# def some_func_2(array):
#     return [word for word in array if 0 < len(word) <= 3]


# print(some_func_2(["hello", "2", "world", ":-)"]))
# print(some_func_2(["1234", "1567", "-2", "computer science"]))
# print(some_func_2(["Russia", "Denmark", "Kazan"]))


# 3-ий Вариант

def some_func_3(array):
    return list(filter(lambda x: 0 < len(x) <= 3, array))


print(some_func_3(["hello", "2", "world", ":-)"]))
print(some_func_3(["1234", "1567", "-2", "computer science"]))
print(some_func_3(["Russia", "Denmark", "Kazan"]))
