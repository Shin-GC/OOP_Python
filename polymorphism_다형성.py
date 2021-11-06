from math import pi


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return (self.height + self.width) * 2

    def __str__(self):
        return f"밑변 : {self.width}, 높이 : {self.height} 인 직사각형"


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * pi

    def perimeter(self):
        return self.radius * 2 * pi

    def __str__(self):
        return f"반지름 : {self.radius} 인 원"


class Paint:
    def __init__(self):
        self.shape = []

    def add_shape(self, shape):
        self.shape.append(shape)

    def total_area_of_shapes(self):
        return sum([shape.area() for shape in self.shape])

    def total_perimeter_of_shapes(self):
        return sum([shape.perimeter() for shape in self.shape])

    def __str__(self):
        res_str = "그림판 내부 도형들 \n"
        for shape in self.shape:
            res_str += str(shape) + "\n"
        return res_str


rectangle = Rectangle(5, 7)
circle = Circle(3)
paint = Paint()

paint.add_shape(rectangle)
paint.add_shape(circle)

print(paint.total_area_of_shapes())
print(paint.total_perimeter_of_shapes())
print(paint)