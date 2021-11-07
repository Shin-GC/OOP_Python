from math import pi


class Shape:
    def area(self):
        """도형의 넓이를 리턴 : 자식 클래스가 오버라이딩할 것"""
        pass

    def perimeter(self):
        """도형의 둘레를 리턴 : 자식 클래스가 오버라이딩할 것"""
        pass


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return (self.height + self.width) * 2

    def __str__(self):
        return f"밑변 : {self.width}, 높이 : {self.height} 인 직사각형"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * pi

    def perimeter(self):
        return self.radius * 2 * pi

    def __str__(self):
        return f"반지름 : {self.radius} 인 원"


class Cylinder:
    """원통 클래스"""
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def __str__(self):
        """원통의 정보를 문자열로 리턴"""
        return f"밑면 반지름 : {self.radius}, 높이 : {self.height} 인 원기둥"


class Paint:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        if isinstance(shape, Shape):  # shape 에 들어온 값이 Shape 값을 상속하고 있는지 확인
            self.shapes.append(shape)
        else:
            print("넓이, 둘레를 구하는 메소드가 없는 도형은 추가할 수 없습니다.")

    def total_area_of_shapes(self):
        return sum([shape.area() for shape in self.shapes])

    def total_perimeter_of_shapes(self):
        return sum([shape.perimeter() for shape in self.shapes])

    def __str__(self):
        res_str = "그림판 내부 도형들 \n"
        for shape in self.shapes:
            res_str += str(shape) + "\n"
        return res_str


cylinder = Cylinder(7, 4)
rectangle = Rectangle(3, 7)
circle = Circle(4)

paint_program = Paint()
paint_program.add_shape(cylinder)
paint_program.add_shape(rectangle)
paint_program.add_shape(circle)

print(paint_program.total_area_of_shapes())
print(paint_program.total_perimeter_of_shapes())



