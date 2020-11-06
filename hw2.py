'''
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
'''

my_list = list(input('Введите значения через запятую (например, 1,2,3,4): ').split(','))
mutate_list = []

if len(my_list) % 2 == 0:
    for i in range(len(my_list)):
        if i % 2 == 0:
            mutate_list.append(my_list[i + 1])
        else:
            mutate_list.append(my_list[i - 1])
else:
    for i in range(len(my_list) - 1):
        if i % 2 == 0:
            mutate_list.append(my_list[i + 1])
        else:
            mutate_list.append(my_list[i - 1])
    mutate_list.append(my_list[-1])

print(mutate_list)
