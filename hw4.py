'''
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''

from time import sleep
import math
import turtle
s = turtle.getscreen()

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        turtle.color(self.color)
        turtle.speed(int(math.log(self.speed)))

    def car_go(self, distance):
        turtle.forward(distance)
        print(f'Машина проехала вперёд на {distance} метров!')
        sleep(2)

    def car_stop(self):
        print('Машина остановилась!')

    def car_turn(self, direction, angle):
        print(f'Машина повернула {direction} на {angle} градусов!')
        if direction == 'left':
            turtle.left(angle)
            sleep(2)
        elif direction == 'right':
            turtle.right(angle)
            sleep(2)

    def show_speed(self):
        print(f'Текущая скорость = {self.speed} км/ч!')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Внимание: превышение скорости! Текущая скорость: {self.speed}!')
        else:
            print(f'Текущая скорость = {self.speed} км/ч!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Внимание: превышение скорости! Текущая скорость: {self.speed} км/ч!')
        else:
            print(f'Текущая скорость = {self.speed} км/ч!')


class PoliceCar(Car):
    pass




car1 = Car(100, 'blue', 'Volvo', False)
car1.car_turn('left', 90)
car1.car_go(150)
car1.car_turn('left', 45)
car1.car_go(200)
car1.car_turn('right', 45)
car1.car_go(50)
car1.car_go(50)
car1.car_turn('left', 120)
car1.car_go(50)
car1.car_turn('left', 100)
car1.car_go(200)
car1.car_stop()
car1.show_speed()

turtle.done()
