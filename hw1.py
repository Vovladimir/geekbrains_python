'''Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
и метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
https://all-python.ru/osnovy/tsvetnoj-vyvod-teksta.html
https://en.wikipedia.org/wiki/ANSI_escape_code
https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
turtle
Tkinter
'''
from termcolor import colored, cprint
from time import sleep
from itertools import cycle
import turtle


class Trafficlight:
    __color = ['red', 'yellow', 'green']

    def start(self):
        for i in cycle([0, 1, 2]):

            cprint(f'Светофор в режиме: {Trafficlight.__color[i]}', Trafficlight.__color[i], attrs=['reverse', 'blink'])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            else:
                sleep(7)


tl = Trafficlight()
tl.start()


# ============================turtle========================


class TurtleTrafficlight:
    __color = ['red', 'yellow', 'green']

    def start(self):

        for i in cycle([0, 1, 2]):
            turtle.title("Turtle-Trafficlight")
            turtle.bgcolor("black")
            turtle.pen(pencolor=TurtleTrafficlight.__color[i], fillcolor=TurtleTrafficlight.__color[i],
                       pensize=10, speed=0)
            turtle.begin_fill()
            turtle.circle(150)
            turtle.end_fill()
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            else:
                sleep(7)


ttl = TurtleTrafficlight()
ttl.start()
