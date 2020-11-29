'''
 Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
 В рамках класса реализовать два метода.
 Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
 Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
 Проверить работу полученной структуры на реальных данных.
'''


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def get_data(cls, data):
        try:
            date_list = [int(i) for i in data.split('-')]
        except ValueError:
            return f'Error: На вход ожидаются цифры!'
        else:
            return cls(day=date_list[0], month=date_list[1], year=date_list[2])

    @staticmethod
    def valid_date(data):

        try:
            date_list = [int(i) for i in data.split('-')]
            if (date_list[0] < 1 or date_list[0]) > 31 or (0 > date_list[1] or date_list[1] > 12) \
                    or 0 > date_list[2]:
                raise ValueError
        except ValueError:
            return f'Ошибка: некорректный ввод данных! ' \
                   f'Убедитесь, что данные введены в формате "день-месяц-год".'
        else:
            return f'Данные введены корректно!'


date = input('Введите дату в формате «день-месяц-год»: ')

date_1 = Date.get_data(date)
print(f"Day: {date_1.day} Month: {date_1.month} Year: {date_1.year}")
print(Date.valid_date(date))
