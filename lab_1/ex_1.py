# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 08:41:38 2023

@author: Egor
"""

import math as m

# Ввод значений с клавиатуры и проверка на ошибки
try:
    n = float(input("Введите значение n: "))
    x = float(input("Введите значение x: "))
except ValueError:
    print("Ошибка: Введите корректные числовые значения.")
    exit(1)
if x != 1 and x != m.e:
    pass
else:
    print("Ошибка: Введите корректные числовые значения.")
    exit(1)

result = m.sqrt(abs(m.cos(x))**n + (m.e**(n**3))/(m.log(x)) + (abs(m.sin(x)))**(1/n))
print(result)