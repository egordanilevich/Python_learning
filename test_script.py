
# Открываем файл для записи с явным указанием кодировки
with open('example.txt', 'w', encoding='utf-8') as file:
    # Записываем строку в файл
    file.write('Это строка, которую мы записываем в файл.')

# Открываем файл для чтения с указанием кодировки
with open('example.txt', 'r', encoding='utf-8') as file:
    # Читаем содержимое файла
    file_content = file.read()

# Выводим содержимое файла на экран
print(file_content)