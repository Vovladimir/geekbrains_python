'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
'''


class ExceptionZeroDivision(Exception):
    def __init__(self, text):
        self.text = text


numbers = input('Введите делимое и делитель через пробел: ')

try:
    numbers_div_list = [int(i) for i in numbers.split()]
    if numbers_div_list[1] == 0:
        raise ExceptionZeroDivision('Ошибка: Ввели отрицательное число!')
except ValueError:
    print(f'Ошибка: вводится число!')
except ExceptionZeroDivision as err:
    print(f'{err}')
else:
    print(numbers_div_list[0] / numbers_div_list[1])
