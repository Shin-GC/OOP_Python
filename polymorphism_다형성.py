from math import sqrt
from abc import ABC, abstractmethod


class Shape(ABC):
    """도형 클래스"""

    @abstractmethod
    def area(self) -> float:
        """도형의 넓이를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        print("도형의 넓이: ")  # super 를 통해 print 상속받기

    @abstractmethod
    def perimeter(self) -> float:
        """도형의 둘레를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        print("도형의 둘레: ")  # super 를 통해 print 상속받기

    @property
    @abstractmethod
    def x(self) -> int:
        pass


class Paint:
    """그림판 프로그램 클래스"""

    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        """도형 인스턴스만 그림판에 추가한다"""
        if isinstance(shape, Shape):
            self.shapes.append(shape)
        else:
            print("도형 클래스가 아닌 인스턴스는 추가할 수 없습니다!")

    def total_area_of_shapes(self):
        """그림판에 있는 모든 도형의 넓이의 합을 구한다"""
        return sum([shape.area() for shape in self.shapes])

    def total_perimeter_of_shapes(self):
        """그림판에 있는 모든 도형의 둘레의 합을 구한다"""
        return sum([shape.perimeter() for shape in self.shapes])


class RightTriangle(Shape):
    def __init__(self, base, height, x):
        self.base = base
        self.height = height
        self.x = x

    def area(self) -> float:
        super().area()
        return self.base * (self.height / 2)

    def perimeter(self) -> float:
        super().area()
        return (self.base ** 2 + self.height ** 2) ** (1 / 2) + self.base + self.height

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value


right_triangle_1 = RightTriangle(3, 4, 2)

paint_program = Paint()

paint_program.add_shape(right_triangle_1)

print(paint_program.total_area_of_shapes())
print(paint_program.total_perimeter_of_shapes())
print(right_triangle_1.x)
