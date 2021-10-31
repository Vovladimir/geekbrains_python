'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

'''
while True:
    program_title = input('Программа принимает набор чисел, разделённых пробелами и записывает их в файл.\n'
                          'Результатом служит сумма чисел в файле.\n'
                          'Всё понятно? (N/Y): ').upper()
    if program_title == 'N':
        print('Всё познаётся на опыте, давайте попробуем!')
        break
    elif program_title == 'Y':
        break
    else:
        print('Будем считать, что всё понятно!')
        break

with open('text5.txt', 'w+', encoding='utf-8') as file:
    try:
        lines = [int(el) for el in input('Введите число через пробел: ').split()]
        for i in lines:
            print(i, file=file, end=' ')
        print(f'Сумма введённых чисел = {sum(lines)}')
    except ValueError or IOError:
        print('Ошибка: неверный ввод!')
