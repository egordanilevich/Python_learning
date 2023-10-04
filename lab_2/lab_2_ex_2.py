
import math

def square_area(side):
    return side * side

def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def parallelogram_area(base, height):
    return base * height

def menu(L):
    figure = L[0].pop(0)
    values = L[1]

    result = menu_options.get(figure, lambda values: "Нет такого пункта меню.")(values)
    L[1] = values

    return f"{figure} := {result}"

menu_options = {
    'S': lambda values: square_area(values[0]),
    'T': lambda values: trapezoid_area(values[0], values[1], values[2]),
    'P': lambda values: parallelogram_area(values[0], values[1]),
}

L = []
figures = input("Введите названия фигур через пробел: ").upper().split()
L.append(figures)

while L[0]:
    inputs = input("Введите входные данные через пробел: ").split()
    L.append([float(prompt) for prompt in inputs])

    result = menu(L)
    print(result)
