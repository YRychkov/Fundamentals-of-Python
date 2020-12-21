# Задача 1
# def my_func(v1, v2):
#    try:
#        ttl = v1 / v2
#        return f"{v1} / {v2} = {ttl}"
#    except ZeroDivisionError:
#        return "Деление на ноль - запрещено"
#
# print(my_func(float(input("Введите делимое: ")), float(input("Введите делитель: "))))

# Задача 2
# def my_func(first_name, last_name, date_of_birth, city, email, phone_numbr):
#    return f"{first_name} {last_name} {date_of_birth} {city} {email} {phone_numbr}"
# print(my_func(first_name=input("Введите имя: "), last_name=input("Введите фамилию: "), date_of_birth=input("Введите дату рождения: "), city=input("Введите город проживания: "), email=input("Введите email: "), phone_numbr=input("Введите номер телефона: ")))

# Задача 3
# def my_func(v1, v2, v3):
#    if v1 == v2 == v3:
#        return "Хотя-бы один аргумент должен быть различным!"
#    vlu_list = [v1, v2, v3]
#    vlu_list.remove(min(vlu_list))
#    vlu_sum = sum(vlu_list)
#    return f"Сумма наибольших двух аргументов = {vlu_sum}"
#
# print(my_func(float(input("Введите первое значение: ")), float(input("Введите второе значение: ")), float(input("Введите третье значение: "))))

# Задача 4 - Способ 1
# def my_func(x, y):
#    if x > 0 and y < 0:
#        ttl = x ** y
#        return f"{ttl}"
#    return "Основние должно быть положительным, а показатель отрецательным!"
#
# print(my_func(int(input("Введите основание: ")), int(input("Введите показатель: "))))

# Задача 4 - Способ 2
# def my_func(x, y):
#    if x > 0 and y < 0:
#        count = 1
#        while True:
#            if count != abs(y):
#                x = x * x
#                count += 1
#                continue
#            else:
#                break
#        ttl = 1 / x
#        return f"{ttl}"
#    return "Основние должно быть положительным, а показатель отрецательным!"
#
# print(my_func(int(input("Введите основание: ")), int(input("Введите показатель: "))))

# Задача 5
#def my_func():
#    sum_of_numbers = 0
#    while True:
#        v1 = input("Введите строку чисел, разделенных пробелом: ")
#        if v1.find("q") != -1:
#            input_list = list(v1.split())
#            input_list = input_list[:input_list.index("q")]
#            input_list = [int(i) for i in input_list]
#            sum_of_numbers += sum(input_list)
#            break
#        else:
#            input_list = [int(i) for i in v1.split()]
#            sum_of_numbers += sum(input_list)
#            print(sum_of_numbers)
#    print(f"Финальное значение: {sum_of_numbers}")
#
#
#print("Для выхода введите символ 'q'")
#my_func()

# Задача 6
# def int_func(v1):
#    check_vlu = True
#    check_list = list(v1)
#    for i in check_list:
#        if 97 > ord(i) < 122:
#            if ord(i) != 32:
#                check_vlu = False
#                break
#    if check_vlu == False:
#        return "Все символы должны быть маленькими латинскими буквами"
#    else:
#        return v1.title()
#
#
# print(int_func(input("Введите слово: ")))
