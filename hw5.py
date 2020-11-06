'''
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
'''

my_list = [7, 5, 3, 3, 2]
el_index = 0
new_element = int(input('Введите число: '))

if new_element in my_list:
    my_list.insert(my_list.index(new_element), new_element)
else:
    for el in my_list:
        if new_element <= el:
            el_index += 1

    my_list.insert(el_index, new_element)
print(my_list)

# !!!!!!!!!!!!!!!!!!!запрещенный метод!!!!!!!!!!!!!!!!!!!!!!

# my_list.append(new_element)
# my_list.sort(reverse=True)
# print(my_list)
