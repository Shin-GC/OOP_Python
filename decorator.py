def add_print_to(original):  # original = print_hello
    def wrapper():
        print("함수 시작")
        original()  # print_hello()
        print("함수 종료")

    return wrapper


@add_print_to
def print_hello():
    print("안녕!")



print_hello()
