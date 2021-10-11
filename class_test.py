class User:
    count = 0  # 유저 인스턴스의 수를 저장하는 count 클래스 변수 할당

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        User.count += 1

    @staticmethod
    def is_valid_email(email_address):
        return "@" in email_address  # 이메일에 @가 존재하는지 파악하는 정적메소드


user1 = User('Shin', 'naver.com', '1234')

print(User.is_valid_email("Shinnaver.com"))
print(User.is_valid_email("Shin@naver.com"))
print(user1.is_valid_email("Shin@naver.com"))
print(user1.is_valid_email(user1.email))
