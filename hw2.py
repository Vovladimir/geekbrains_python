'''
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''
count = 1
word = 1

with open('text.txt', 'r') as file:
    x = file.read()

    for el in x:
        if el == '\n':
            count += 1
    print(f'В файле {count} строк.')
    str_x = x.split('\n')

    for i in range(len(str_x)):
        word = len(str_x[i].split())
        print(f'В {i + 1} строчке количество слов = {word}.')


