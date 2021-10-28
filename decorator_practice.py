def deco(func):
    def wrapper(*args, **kwargs):
        print(f"함수 이름: {func.__name__} 실행!")
        print(f"Arguments were : {args, kwargs}")
        return func(*args, **kwargs)
    return wrapper


@deco
def add(a, b):
    return a + b


print(add(30, 50))


class Car:
    def __init__(self, name, color, h_speed):
        self.name = name
        self.color = color
        self.h_speed = h_speed

    def drive(self, hour):
        return self.h_speed * hour


class Benz(Car):
    @deco
    def __str__(self):
        return "벤츠차 이름: " + self.name + "차량 색상: " + self.color


s_class = Benz("붕붕이", "black", 140)
print(s_class)
print(s_class.drive(5))