'''
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
'''
from abc import ABC, abstractmethod


class Cloth(ABC):
    @abstractmethod
    def __init__(self, style):
        self.style = style


class Coat(Cloth):
    def __init__(self, size):
        super().__init__(self)
        self.size = size

    @property
    def fabric_consumption(self):
        return f'Расход ткани пальто {self.size} размера = {round(self.size / (6.5 + 0.5), 2)} м2.'


class Suit(Cloth):
    def __init__(self, growth):
        super().__init__(self)
        self.growth = growth

    @property
    def growth(self):
        return self.__growth

    @growth.setter
    def growth(self, growth):
        if growth > 100:  # если пользователь ввёл сантиметры - преобразовать их в метры
            self.__growth = growth / 100
        else:
            self.__growth = growth

    @property
    def fabric_consumption(self):
        return f'Расход ткани костюма при росте {self.growth} метров = {round((self.growth * 2 + 0.3), 2)} м2.'


coat_1 = Coat(50)
print(coat_1.fabric_consumption)
suit_1 = Suit(180)
print((suit_1.fabric_consumption))
