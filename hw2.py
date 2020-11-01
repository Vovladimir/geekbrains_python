'''
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
'''

time_seconds = int(input('Введите время в секундах: '))

hours = time_seconds // 3600
rest_hour = time_seconds % 3600
minutes = rest_hour // 60
seconds = rest_hour % 60

if len(str(hours)) == 2 and len(str(minutes)) == 2 and len(str(seconds)) == 2:
    print(f'{hours}:{minutes}:{seconds}')
elif len(str(hours)) == 2 and len(str(minutes)) == 1 and len(str(seconds)) == 1:
    print(f'{hours}:0{minutes}:0{seconds}')
elif len(str(hours)) == 2 and len(str(minutes)) == 2 and len(str(seconds)) == 1:
    print(f'{hours}:{minutes}:0{seconds}')
elif len(str(hours)) == 2 and len(str(seconds)) == 2 and len(str(minutes)) == 1:
    print(f'{hours}:0{minutes}:{seconds}')
elif len(str(hours)) == 1 and len(str(seconds)) == 1 and len(str(minutes)) == 2:
    print(f'0{hours}:{minutes}:0{seconds}')
elif len(str(hours)) == 1 and len(str(minutes)) == 1 and len(str(seconds)) == 1:
    print(f'0{hours}:0{minutes}:0{seconds}')
elif len(str(hours)) == 1 and len(str(minutes)) == 1 and len(str(seconds)) == 2:
    print(f'0{hours}:0{minutes}:{seconds}')
else:
    print(f'0{hours}:{minutes}:{seconds}')
