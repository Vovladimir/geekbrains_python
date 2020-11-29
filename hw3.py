'''
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные
и заполнять список только числами.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована.
Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
При этом скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить
соответствующее сообщение.
При этом работа скрипта не должна завершаться.

'''


class OnlyNumbersError(Exception):
    def __init__(self, text):
        self.text = text


while True:
    program_title = input('Программа запрашивает у пользователя данные (числа и строки).\n'
                          'При нажатии Enter идёт проверка ввода на наличие числа.\n'
                          'Только числа вносятся в итоговый список.\n'
                          'Если вместо числа вводится "stop", выполнение программы завершается.\n'
                          'Всё понятно? (N/Y): ').upper()
    if program_title == 'N':
        print('Всё познаётся на опыте, давайте попробуем!')
        break
    elif program_title == 'Y':
        break
    else:
        print('Будем считать, что всё понятно!')
        break

result_list = []
condition = True

while condition:
    input_data = input('Поле ввода: ')
    if input_data == 'stop':
        condition = False
    else:
        try:
            if not input_data.isnumeric():
                raise OnlyNumbersError('Напоминаю: Добавится в список только число!')
        except OnlyNumbersError as err:
            print(f'{err}')
        else:
            result_list.append(input_data)

print(result_list)


