'''
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
'''

my_list = [
    'hello', 42, True, 36.6, None, 2 + 3j,
    {'a': '2'}, (1, 2, 3), {'Вася', 'Маша', 'Петя'},
    ['Moscow', 'St.-Petersburg', 'Rostov-on-Don'],
    ValueError, print
]

for element in my_list:
    print(type(element))
