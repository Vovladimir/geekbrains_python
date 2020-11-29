'''
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
*** z1 + z2 = (a + c) + (b + d)j ***
**z1 * z2 = (a * c - b * d) + (a * b - c * b)j ***

'''


class ComplexNumber:

    def __init__(self, material_number, imaginary_number):
        self.material_number = material_number
        self.imaginary_number = imaginary_number

    def __add__(self, other):
        a = self.material_number + other.material_number
        b = self.imaginary_number + other.imaginary_number
        if b >= 0:
            return f"{a} + {b}j"
        else:
            return f"{a} - {abs(b)}j"

    def __mul__(self, other):
        a = self.material_number * other.material_number - (self.imaginary_number * other.imaginary_number)
        b = self.material_number * other.imaginary_number + (other.material_number * self.imaginary_number)
        if b >= 0:
            return f"{a} + {b}j"
        else:
            return f"{a} - {abs(b)}j"


z1 = ComplexNumber(-2, -1)
z2 = ComplexNumber(-3, -5)
print(z1 + z2)
print(z1 * z2)
