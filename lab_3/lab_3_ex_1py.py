class Teacher:
    def __init__(self, emp_id, full_name, gender, birthdate, address, phone, subject, experience, *args):
        self.emp_id = emp_id # табельный номер
        self.full_name = full_name  # ФИО
        self.gender = gender # Пол
        self.birthdate = birthdate # Дата рождения
        self.address = address # Адрес
        self.phone = phone # Телефон
        self.subject = subject # Преподаваемая дисциплина
        self.experience = experience # Стаж работы
        self.additional_info = args  # Сохраняем

    def display_info(self):
        print(f"Табельный номер: {self.emp_id}")
        print(f"ФИО: {self.full_name}")
        print(f"Пол: {self.gender}")
        print(f"Дата рождения: {self.birthdate}")
        print(f"Адрес: {self.address}")
        print(f"Телефон: {self.phone}")
        print(f"Преподаваемая дисциплина: {self.subject}")
        print(f"Стаж работы: {self.experience} лет")
        print(self.additional_info)

teachers_list = [] # Список для хранения объектов "Преподаватель"


def add_teacher():
    """
    1. Добавление записи о преподавателе

    Returns
    -------
    None.

    """
    emp_id = input("Введите табельный номер: ")
    full_name = input("Введите ФИО: ")
    gender = input("Введите пол: ")
    birthdate = input("Введите дату рождения: ")
    address = input("Введите адрес: ")
    phone = input("Введите телефон: ")
    subject = input("Введите преподаваемую дисциплину: ")
    experience = input("Введите стаж работы: ")
    another = input("Введите дополнительную информацию: ")
    
    teacher = Teacher(emp_id, full_name, gender, birthdate, address, phone, subject, experience, another)
    teachers_list.append(teacher)
    print("Информация о преподавателе добавлена.")

def remove_teacher():
    """
    2. Удаление записи о преподавателе

    Returns
    -------
    None.

    """
    if not teachers_list:
        print("Список преподавателей пуст.")
        return
    
    emp_id = input("Введите табельный номер преподавателя, которого нужно удалить: ")
    
    for teacher in teachers_list:
        if teacher.emp_id == emp_id:
            teachers_list.remove(teacher)
            print(f"Преподаватель с табельным номером {emp_id} удален.")
            return
    
    print(f"Преподаватель с табельным номером {emp_id} не найден.")

def display_all_teachers():
    """
    3. вывести список преподавателей

    Returns
    -------
    None.

    """
    if not teachers_list:
        print("Список преподавателей пуст.")
        return
    
    print("Информация о всех преподавателях:")
    for teacher in teachers_list:
        teacher.display_info()
        print()

def search_teachers_by_subject():
    """
    4. поиск преподавателей по предмету

    Returns
    -------
    None.

    """
    subject = input("Введите дисциплину для поиска преподавателей: ")
    found_teachers = [teacher for teacher in teachers_list if teacher.subject == subject]
    
    if not found_teachers:
        print(f"Преподавателей, преподающих дисциплину '{subject}', не найдено.")
    else:
        print(f"Преподаватели, преподающие дисциплину '{subject}':")
        for teacher in found_teachers:
            teacher.display_info()
            print()

# Главное меню программы
while True:
    print("\n  Меню программы:")
    print("1. Добавление информации о преподавателе")
    print("2. Удаление информации о преподавателе")
    print("3. Отображение информации обо всех преподавателях")
    print("4. Поиск преподавателей по дисциплине")
    print("5. Выход")
    
    command = input("Выберите действие: ")
    
    if command == "1":
        add_teacher()
    elif command == "2":
        remove_teacher()
    elif command == "3":
        display_all_teachers()
    elif command == "4":
        search_teachers_by_subject()
    elif command == "5":
        print("Программа завершена.")
        break
    else:
        print("Неверный выбор.")
