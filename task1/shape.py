import math


class Shape:
    def square(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        if type(radius) not in [int, float]:
            raise TypeError('Недопустимый тип')
        if radius <= 0:
            raise ValueError('Недопустимое значение радиуса')
        self.radius = radius
    
    def square(self):
        return math.pi * self.radius**2


class Triangle(Shape):
    def __init__(self, a, b, c):
        if type(a) not in [int, float] or type(b) not in [int, float] or type(c) not in [int, float]:
            raise TypeError('Недопустимый тип')
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError('Недопустимое значение сторон треугольника')
        if a+b < c or a+c < b or b+c < a:
            raise ValueError('Треугольник с заданными сторонами не существует')
        self.a = a
        self.b = b
        self.c = c
    
    def square(self):
        hp = (self.a + self.b + self.c) / 2
        return math.sqrt(hp * (hp - self.a) * (hp - self.b) * (hp - self.c))

    def is_rectangular(self):
        if self.a**2 + self.b**2 == self.c**2 \
                or self.a**2 + self.c**2 == self.b**2 \
                or self.b**2 + self.c**2 == self.a**2:
            return True
        return False


def calculate_area(shape):
    return shape.square()
