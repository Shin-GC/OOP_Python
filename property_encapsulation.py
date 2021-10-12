class Citizen:
    def __init__(self, name, age, resident_id):
        """name: 이름, _age : 나이, _resident_id : 주민등록번호"""
        self.name = name
        self.age = age  # @age.setter 로 인해 자동으로 encapsulation 변수가 되어 self._age로 변경된다.
        self._resident_id = resident_id

    @property
    def age(self):
        """_age 값을 리턴해주는 property getter 메소드
        Return:
            _age"""
        print("나이를 리턴합니다.")
        return self._age

    @age.setter
    def age(self, value):
        """_age 값을 설정해주는 property setter 메소드
        Parameter:
            value (int) : 설정할 나이 값
        """
        if value < 0:
            print("나이는 0보다 작을 수 없습니다. 기본 값 0로 나이를 설정합니다.")
            self._age = value
        else:
            self._age = value


shin = Citizen("Shin", 25, "1234-5678")
print(shin.age)
shin.age = 26
print(shin.age)

help(Citizen)
#     def get_age(self):
#         """encapsulation 한 변수 _age 의 값을 받아오는 getter 메소드"""
#         return self._age
#
#     def set_age(self, value):
#         """encapsulation 한 변수 _age 의 값을 설정하는 setter 메소드"""
#         if value < 0:
#             print("나이는 0보다 작을 수 없습니다. 기본 값 0로 나이를 설정합니다.")
#             self._age = value
#         else:
#             self._age = value
#
#
# shin = Citizen('Shin', 25, '12345-6789')
# print(shin.get_age())
#
# shin.set_age(27)
# print(Citizen.get_age(shin))



