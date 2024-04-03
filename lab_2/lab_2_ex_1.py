import math as m
from sys import exit

def get_float_input(prompt):
    try:
        value = float(input(prompt))
        return value
    except ValueError:
        print("Ошибка: Введите корректные числовые значения.")
        exit(1)

def compute_result(get_float_input):
    
    n = get_float_input("Введите значение n: ")
    x = get_float_input("Введите значение x: ")
    try:
        return m.sqrt(abs(m.cos(x))**n + (m.e**(n**3))/(m.log(x)) + (abs(m.sin(x)))**(1/n))
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль.")
        exit(1)



result = compute_result(get_float_input)
print(result)
