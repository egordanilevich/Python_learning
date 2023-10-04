def show_list(my_list):
    print("Список:", my_list)

def add_element(my_list): 
   var_type = input("Выберите тип значения (int, float, string): ")
   value = None
   
   if var_type == 'int':
       value = int(input("Введите целочисленный элемент: "))
       my_list.append(value)

   elif var_type == 'float':
       value = float(input("Введите вещественный элемент: "))
       my_list.append(value)

   elif var_type == 'string':
       value = input("Введите символьный элемент: ")
       my_list.append(value)
   else:
       print("Неверный тип.")
       return

def remove_element(my_list):
    var_type = input("Выберите тип значения (int, float, string): ")
    value = None
    
    if var_type == 'int':
        element = int(input("Введите элемент для удаления: "))
        if element in my_list:
            my_list.remove(element)
        else:
            print("Такой элемент не найден в списке.")

    elif var_type == 'float':
        element = float(input("Введите элемент для удаления: "))
        if element in my_list:
            my_list.remove(element)
        else:
            print("Такой элемент не найден в списке.")

    elif var_type == 'string':
        element = input("Введите элемент для удаления: ")
        if element in my_list:
            my_list.remove(element)
        else:
            print("Такой элемент не найден в списке.")
    else:
        print("Неверный тип.")
        return
        
    
    
   

def create_float_tuple(my_list):
    float_elements = tuple([x for x in my_list if( isinstance(x,float) and x > 0)])
    print("Кортеж вещественных положительных элементов:", float_elements)

def calculate_product(my_list):
    product = 1
    for element in my_list:
        if isinstance(element, int):
            product *= element
    print("Произведение всех целочисленных элементов:", product)

def find_word_count(my_list):
    word = input("Введите слово для поиска в строке: ")
    joined_string = ' '.join(my_list)
    count = joined_string.count(word)
    print("Строка:", joined_string)
    print(f"Слово '{word}' встречается {count} раз(а) в строке.")

def symmetric_difference(my_list):
    
    temp_list = []
    print("Введите множество:")
    
    while 1 :
        var_type = input("Выберите тип значения (int, float, string) иначе выход: ")
        value = None
        if var_type == 'int':
            value = int(input("Введите целочисленный элемент: "))
            temp_list.append(value)
    
        elif var_type == 'float':
            value = float(input("Введите вещественный элемент: "))
            temp_list.append(value)
    
        elif var_type == 'string':
            value = input("Введите символьный элемент: ")
            temp_list.append(value)
        else:
            break
        
    m1 = set(temp_list)
    m2 = set(my_list)
    symmetric_diff = m1.symmetric_difference(m2)
    print("Симметричная разница множеств M1 и M2:", symmetric_diff)

def create_dict_with_odd_keys(my_list):
    my_dict = {i: element for i, element in enumerate(my_list, 1) if i % 2 != 0}
    print("Словарь с элементами, у которых нечетные ключи:")
    for key, value in my_dict.items():
        print(f"{key}: {value}")

my_list = [1.2,5.3,"str",1,2,3,-1]

while True:
    print("Список команд:")
    print("1 - Показать значения списка")
    print("2 - Добавить элемент в список")
    print("3 - Удалить элемент из списка")
    print("4 - Сформировать кортеж из вещественных положительных элементов")
    print("5 - Найти произведение всех целочисленных элементов")
    print("6 - Сформировать строку и посчитать вхождения слова")
    print("7 - Задать множество M1 и найти симметричную разницу с M2")
    print("8 - Сформировать словарь и отобразить элементы с нечетными ключами")
    print("9 - Выйти из программы")
    
    command = input("Выберите действие: ")
    
    if command == "1":
        show_list(my_list)
    elif command == "2":
        add_element(my_list)
    elif command == "3":
        remove_element(my_list)
    elif command == "4":
        create_float_tuple(my_list)
    elif command == "5":
        calculate_product(my_list)
    elif command == "6":
        find_word_count(my_list)
    elif command == "7":
        symmetric_difference(my_list)
    elif command == "8":
        create_dict_with_odd_keys(my_list)
    elif command == "9":
        break
    else:
        print("Команда не определена")
    print(" ")