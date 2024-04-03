import tkinter as tk
from tkinter import messagebox, filedialog

class Teacher:
    def __init__(self, emp_id, full_name, gender, birthdate, address, phone, subject, experience, additional_info):
        self.emp_id = emp_id
        self.full_name = full_name
        self.gender = gender
        self.birthdate = birthdate
        self.address = address
        self.phone = phone
        self.subject = subject
        self.experience = experience
        self.additional_info = additional_info

    def display_info(self):
        return f"Табельный номер: {self.emp_id}\nФИО: {self.full_name}\nПол: {self.gender}\nДата рождения: {self.birthdate}\n" \
               f"Адрес: {self.address}\nТелефон: {self.phone}\nПреподаваемая дисциплина: {self.subject}\n" \
               f"Стаж работы: {self.experience} лет\nДополнительная информация: {self.additional_info}\n"

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Система управления преподавателями")

        self.teachers_list = []

        # Создание элементов интерфейса
        self.label_emp_id = tk.Label(self, text="Табельный номер:")
        self.entry_emp_id = tk.Entry(self)

        self.label_full_name = tk.Label(self, text="ФИО:")
        self.entry_full_name = tk.Entry(self)

        self.label_gender = tk.Label(self, text="Пол:")
        self.entry_gender = tk.Entry(self)

        self.label_birthdate = tk.Label(self, text="Дата рождения:")
        self.entry_birthdate = tk.Entry(self)

        self.label_address = tk.Label(self, text="Адрес:")
        self.entry_address = tk.Entry(self)

        self.label_phone = tk.Label(self, text="Телефон:")
        self.entry_phone = tk.Entry(self)

        self.label_subject = tk.Label(self, text="Преподаваемая дисциплина:")
        self.entry_subject = tk.Entry(self)

        self.label_experience = tk.Label(self, text="Стаж работы:")
        self.entry_experience = tk.Entry(self)

        self.label_additional_info = tk.Label(self, text="Дополнительная информация:")
        self.entry_additional_info = tk.Entry(self)

        self.button_add_teacher = tk.Button(self, text="Добавить преподавателя", command=self.add_teacher)
        self.button_remove_teacher = tk.Button(self, text="Удалить преподавателя", command=self.remove_teacher)
        self.button_display_teachers = tk.Button(self, text="Отобразить преподавателей", command=self.display_all_teachers)
        self.button_search_teachers = tk.Button(self, text="Поиск по дисциплине", command=self.search_teachers_by_subject)
        self.button_exit = tk.Button(self, text="Выход", command=self.quit)

        # Расположение элементов интерфейса на сетке
        self.label_emp_id.grid(row=0, column=0, sticky="e")
        self.entry_emp_id.grid(row=0, column=1)

        self.label_full_name.grid(row=1, column=0, sticky="e")
        self.entry_full_name.grid(row=1, column=1)

        self.label_gender.grid(row=2, column=0, sticky="e")
        self.entry_gender.grid(row=2, column=1)

        self.label_birthdate.grid(row=3, column=0, sticky="e")
        self.entry_birthdate.grid(row=3, column=1)

        self.label_address.grid(row=4, column=0, sticky="e")
        self.entry_address.grid(row=4, column=1)

        self.label_phone.grid(row=5, column=0, sticky="e")
        self.entry_phone.grid(row=5, column=1)

        self.label_subject.grid(row=6, column=0, sticky="e")
        self.entry_subject.grid(row=6, column=1)

        self.label_experience.grid(row=7, column=0, sticky="e")
        self.entry_experience.grid(row=7, column=1)

        self.label_additional_info.grid(row=8, column=0, sticky="e")
        self.entry_additional_info.grid(row=8, column=1)

        self.button_add_teacher.grid(row=9, column=0, columnspan=2)
        self.button_remove_teacher.grid(row=10, column=0, columnspan=2)
        self.button_display_teachers.grid(row=11, column=0, columnspan=2)
        self.button_search_teachers.grid(row=12, column=0, columnspan=2)
        self.button_exit.grid(row=13, column=0, columnspan=2)

        # Создание главного меню
        self.menu_bar = tk.Menu(self)

        # Меню "Файл"
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Создать", command=self.clear_entries)
        self.file_menu.add_command(label="Открыть", command=self.open_file)
        self.file_menu.add_command(label="Сохранить", command=self.save_file)
        self.file_menu.add_command(label="Сохранить как...", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Выход", command=self.quit)

        # Меню "Справка"
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="О программе", command=self.show_about)

        # Добавление меню в главное меню
        self.menu_bar.add_cascade(label="Файл", menu=self.file_menu)
        self.menu_bar.add_cascade(label="Справка", menu=self.help_menu)

        # Привязка главного меню
        self.config(menu=self.menu_bar)

    def add_teacher(self):
        emp_id = self.entry_emp_id.get()
        full_name = self.entry_full_name.get()
        gender = self.entry_gender.get()
        birthdate = self.entry_birthdate.get()
        address = self.entry_address.get()
        phone = self.entry_phone.get()
        subject = self.entry_subject.get()
        experience = self.entry_experience.get()
        additional_info = self.entry_additional_info.get()

        teacher = Teacher(emp_id, full_name, gender, birthdate, address, phone, subject, experience, additional_info)
        self.teachers_list.append(teacher)

        self.clear_entries()
        messagebox.showinfo("Информация", "Информация о преподавателе добавлена.")

    def remove_teacher(self):
        emp_id = self.entry_emp_id.get()
        for teacher in self.teachers_list:
            if teacher.emp_id == emp_id:
                self.teachers_list.remove(teacher)
                messagebox.showinfo("Информация", f"Информация о преподавателе {teacher.full_name} удалена.")
                break
        else:
            messagebox.showinfo("Информация", f"Преподаватель с табельным номером {emp_id} не найден.")

    def display_all_teachers(self):
        if not self.teachers_list:
            messagebox.showinfo("Информация", "Список преподавателей пуст.")
            return

        info = "\n\n".join([teacher.display_info() for teacher in self.teachers_list])
        messagebox.showinfo("Информация о преподавателях", info)

    def search_teachers_by_subject(self):
        subject = self.entry_subject.get()
        found_teachers = [teacher for teacher in self.teachers_list if teacher.subject == subject]

        if not found_teachers:
            messagebox.showinfo("Информация", f"Преподавателей, преподающих дисциплину '{subject}', не найдено.")
        else:
            info = "\n\n".join([teacher.display_info() for teacher in found_teachers])
            messagebox.showinfo("Информация о преподавателях", info)

    def clear_entries(self):
        self.entry_emp_id.delete(0, tk.END)
        self.entry_full_name.delete(0, tk.END)
        self.entry_gender.delete(0, tk.END)
        self.entry_birthdate.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_subject.delete(0, tk.END)
        self.entry_experience.delete(0, tk.END)
        self.entry_additional_info.delete(0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    self.teachers_list = []  # Очищаем текущий список
                    data = file.read()
                    lines = data.split("\n")
                    for line in lines:
                        info_parts = line.split(" ", maxsplit=3)
                        additional_info = info_parts[3] if len(info_parts) > 3 else ""
                        teacher = Teacher(*info_parts[:3], additional_info)
                        self.teachers_list.append(teacher)

                messagebox.showinfo("Информация", f"Данные успешно загружены из файла {file_path}")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка при чтении файла: {e}")

    def save_file(self):
        if not self.teachers_list:
            messagebox.showinfo("Информация", "Список преподавателей пуст. Нечего сохранять.")
            return

        # Если уже существует путь к файлу, используем его, иначе вызываем save_file_as
        if hasattr(self, 'file_path') and self.file_path:
            file_path = self.file_path
        else:
            self.save_file_as()
            return

        try:
            with open(file_path, "w", encoding="utf-8") as file:
                for teacher in self.teachers_list:
                    file.write(f"{teacher.emp_id} {teacher.full_name} {teacher.gender} {teacher.birthdate} "
                               f"{teacher.address} {teacher.phone} {teacher.subject} {teacher.experience} "
                               f"{teacher.additional_info}\n")

            messagebox.showinfo("Информация", f"Данные успешно сохранены в файл {file_path}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при сохранении файла: {e}")

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

        if file_path:
            self.file_path = file_path
            self.save_file()

    def show_about(self):
        about_text = "Система управления преподавателями\n\n" \
                     "Разработчик: Ваше Имя\n" \
                     "Дата: 2023"
        messagebox.showinfo("О программе", about_text)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
