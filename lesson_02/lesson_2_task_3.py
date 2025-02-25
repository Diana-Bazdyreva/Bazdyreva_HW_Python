import math


def square(side):
    return math.ceil(side*side)


lenght_side = int(input("Введите сторону квадрата: "))
print(f"Площадь квадрата: {square(lenght_side)}")
