'''
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''

number = int(input('Введите число: '))
max_number = 0
while True:
    residual = number % 10
    if residual > max_number:
        max_number = residual

    whole_part = number // 10
    if whole_part > 0:
        number = whole_part

    else:
        print(max_number)
        break