# This Python file uses the following encoding: utf-8


class Teacher:
    def __init__(self, emp_id, full_name, gender, birthdate, address, phone, subject, experience, *args):
        self.emp_id = emp_id  # табельный номер
        self.full_name = full_name  # ФИО
        self.gender = gender  # Пол
        self.birthdate = birthdate  # Дата рождения
        self.address = address  # Адрес
        self.phone = phone  # Телефон
        self.subject = subject  # Преподаваемая дисциплина
        self.experience = experience  # Стаж работы
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
