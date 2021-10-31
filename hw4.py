'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.

'''

# ------------------------------------- некорректное решение --------------------------

rus_number = ['Один', 'Два', 'Три', 'Четыре']

with open('text_4.txt', 'r', encoding='utf-8') as file:
    for i in file:
        print(i, end='')


with open('new_text4.txt', 'w', encoding='utf-8') as new_file:
    for i in range(len(rus_number)):
        new_file.writelines(f'{rus_number[i]} - {i}\n')


# ------------------------------------- решение 2 ----------------------------------


rus_num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

new_file = []

with open('text_4.txt', 'r', encoding='utf-8') as file:
    for i in file:
        print(i, end='')
        i = i.split(' ', 1)
        new_file.append(f'{rus_num[i[0]]} {i[1]}')

with open('text_4_new.txt', 'w', encoding='utf-8') as file_2:
    file_2.writelines(new_file)
