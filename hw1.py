'''
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''
while True:
    program_title = input('Программа принимает два числа.\n'
                          'Результатом работы является деление этих чисел.\n'
                          'Всё понятно? (N/Y): ').upper()
    if program_title == 'N':
        print('Всё познаётся на опыте, давайте попробуем!')
        break
    elif program_title == 'Y':
        break
    else:
        print('Будем считать, что всё понятно!')
        break

x = float(input('Введите делимое: '))
y = float(input('Введите делитель: '))

"""решение через if else"""


def division(divisible_number, divider):
    if divider == 0:
        result = "'Ошибка: попытка деления на ноль!'"
    else:
        result = divisible_number / divider
    return result


print(f'Ответ: {division(x, y)}')

"""решение через try except"""


def division_var(div_num, divider):
    try:
        return div_num / divider
    except ZeroDivisionError:
        print(f'Ошибка: попытка деления на ноль!')


print(division_var(x, y))
