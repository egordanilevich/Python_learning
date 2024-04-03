from functools import reduce
from math import pi, tan


def S(values):
    print(L)
    try:
        side = values.pop(0)
        area = side * side
        print("Площадь квадрата: ", area)
        return True
    except:
        print("Заданы неверные значения!")


def T(values):
    print(L)

    try:
        base1, base2, height = values.pop(0), values.pop(0), values.pop(0)
        area = 0.5 * (base1 + base2) * height
        print("Площадь трапеции: ", area)
        return True
    except:
        print("Заданы неверные значения!")


def P(values):
    print(L)

    try:
        base, height = values.pop(0), values.pop(0)
        area = base * height
        print("Площадь параллелограмма: ", area)
        return True
    except:
        print("Заданы неверные значения!")


def E():
    exit(0)


L = [['S', 'T', 'P', 'E'], [2], [2, 3, 4], [3, 2],]

reduce(lambda a, b: ((L[0][0].upper() == "S" and S(b))
                     or (L[0][0] == "T".upper() and T(b)) 
                     or (L[0][0] == "P".upper() and P(b)) 
                     or (L[0][0] == "E".upper() and E())) 
       and (L[0].pop(0)), L[1:], True)