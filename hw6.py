'''
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                     Физика:   30(л)   —   10(лаб)
                     Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

'''


def sum_number_from_str(arg):
    string = str(arg)
    number = []
    i = 0
    while i < len(string):
        string_num = ''
        string_index = string[i]
        while string_index.isnumeric():
            string_num += string_index
            i += 1
            if i < len(string):
                string_index = string[i]
            else:
                break
        i += 1
        if string_num != '':
            number.append(int(string_num))

    return sum(number)


with open('text_6.txt', 'r', encoding='utf-8') as file:
    #
    file = file.readlines()
    keys = [i.rsplit(':')[0] for i in file]
    values = [sum_number_from_str(i) for i in file]
    d = {}
    for el in range(len(keys)):
        d[keys[el]] = values[el]

print(d)
