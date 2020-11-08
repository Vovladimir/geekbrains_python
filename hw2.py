'''
.
Реализовать вывод данных о пользователе одной строкой.
'''

# --------------------------------------- Решение 1 ---------------------------------------

def profile_form(name, surname, year_of_birth, city, email, phone_number):
    '''Функция принимает несколько параметров,
    описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
    Функция должна принимать параметры как именованные аргументы'''
    return (f'{name} {surname}, {year_of_birth} года рождения, проживает в городе {city}. '
            f'E-mail: {email}, номер телефона: {phone_number}')


my_profile = profile_form(name="Владимир", surname='Смирнов', year_of_birth=1987, city='Ростов-на-Дону',
                          email='vovladimir@gmail.com',
                          phone_number='+7(928)628-12-10.')

print(my_profile)


# ------------------------------------- решение 2 ----------------------------------------

def foo(**kwarg):
    for key, val in kwarg.items():
        print(f'{key}: {val}', end=', ')


my_form = foo(name="Владимир", surname='Смирнов', year_of_birth=1987, city='Ростов-на-Дону',
              email='vovladimir@gmail.com',
              phone_number='+7(928)628-12-10.')


