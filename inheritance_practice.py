
class Car:
    def __init__(self, name, color, h_speed):
        self.name = name
        self.color = color
        self.h_speed = h_speed

    def drive(self, hour):
        return self.h_speed * hour


class Benz(Car):
    def __str__(self):
        return "벤츠차 이름: " + self.name + "차량 색상: " + self.color


s_class = Benz("붕붕이", "black", 140)
print(s_class)
print(s_class.drive(5))
