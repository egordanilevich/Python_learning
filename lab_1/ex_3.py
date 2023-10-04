def square_area(side):
    return side * side

def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def parallelogram_area(base, height):
    return base * height

while True:
    print("\nВыберите фигуру для вычисления площади:")
    print("S - Квадрат")
    print("T - Трапеция")
    print("P - Параллелограмм")
    print("E - Выход")

    command = input("Введите команду выбора: ").upper()

    if command == 'S':
        try:
            side = float(input("Введите длину стороны квадрата: "))
            area = square_area(side)
            print(f"Площадь квадрата: {area}")
        except ValueError:
            print("Ошибка: Неверный ввод. Введите число.")
    elif command == 'T':
        try:
            base1 = float(input("Введите длину большей основы трапеции: "))
            base2 = float(input("Введите длину меньшей основы трапеции: "))
            height = float(input("Введите высоту трапеции: "))
            area = trapezoid_area(base1, base2, height)
            print(f"Площадь трапеции: {area}")
        except ValueError:
            print("Ошибка: Неверный ввод. Введите число.")
    elif command == 'P':
        try:
            base = float(input("Введите длину основания параллелограмма: "))
            height = float(input("Введите высоту параллелограмма: "))
            area = parallelogram_area(base, height)
            print(f"Площадь параллелограмма: {area}")
        except ValueError:
            print("Ошибка: Неверный ввод. Введите число.")
    elif command == 'E':
        break
    else:
        print("Ошибка: Неверный выбор. Попробуйте еще раз.")