# анкета
name = input('Введите Ваше имя: ')
surname = input('Введите Вашу фамилию: ')
age = int(input('Ваш возраст: '))

print(f'Добро пожаловать, {name} {surname}! Перед Вами бета-версия нашего калькулятора.'
      f' Ознакомьтесь и оставьте Ваши пожелания!')

# калькулятор

a = float(input(f'Введите первое число, может {age} ;): '))
b = float(input('Введите второе число: '))
oper = str(input('Введите символ операции(*, /, - , +, //, %, **): '))
result = None
if b == 0 and (oper == "/" or oper == 'mod' or oper == "div"):
    print('Ошибка: Деление на 0!')
elif oper == "+":
    result = a + b
elif oper == "-":
    result = a - b
elif oper == "/":
    result = a / b
elif oper == '*':
    result = a * b
elif oper == '%':
    a = int(a)
    b = int(b)
    result = a % b
elif oper == '**':
    result = a ** b
elif oper == '//':
    result = a // b
else:
    print(f'{name} {surname}, я Вас не понял!')

print(f'Ответ: {result}.')

comment = input('Оставьте Ваш комментарий: ')

print(f'{name} {surname}, спасибо за отзыв!')
