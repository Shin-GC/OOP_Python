def add(value1=0, value2=0):
    """ 두 수를 더해준다.
    Parameters:
        value1 (int, float) : 더할 첫번째 값
        (기본 값 : 0)
        value2 (int, float) : 더할 두번째 값
        (기본 값 : 0)
    Return:
        int, float : 두 수를 더한 값
    """
    return value1 + value2


help(add)
print(add(5.2, 10))