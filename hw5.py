'''
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''
import turtle


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        turtle.title(self.title)
        print('Запуск отрисовки!')
        turtle.pen(pencolor="purple", fillcolor="orange", pensize=10, speed=9)
        turtle.begin_fill()
        turtle.circle(90)
        turtle.end_fill()
        print('Конец отрисовки!')


class Pen(Stationery):
    def draw(self):
        print(f'Отрисовка c помощью {self.title}!')
        turtle.pen(pencolor="red", fillcolor="green", pensize=3, speed=5)
        turtle.begin_fill()
        turtle.circle(90)
        turtle.end_fill()
        print('Конец отрисовки!')


class Pencil(Stationery):
    def draw(self):
        print(f'Используем {self.title}!')
        turtle.pen(pencolor="black", fillcolor="grey", pensize=1, speed=3)
        turtle.begin_fill()
        turtle.circle(90)
        turtle.end_fill()
        print('Конец отрисовки!')


class Handle(Stationery):
    def draw(self):
        print(f'Где ты взял такой хороший {self.title}?')
        turtle.pen(pencolor="brown", fillcolor="blue", pensize=7, speed=8)
        turtle.begin_fill()
        turtle.circle(90)
        turtle.end_fill()
        print('Конец отрисовки!')


a = Pencil('карандаш')
a.draw()
b = Pen('ручка')
b.draw()
c = Handle('маркер')
c.draw()