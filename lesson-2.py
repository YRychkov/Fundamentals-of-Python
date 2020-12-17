# Задача 1
#list = [False, 1, 2.2, "3", [3, 4], (5, 6), {"g": 7, "h": 8}]
#
#for num in list:
#    print(type(num))

# Задача 2
#list = [1, 2, 3, 4, 5, 6, 7]
#
#for i in range(1, len(list), 2):
#    list.insert(i - 1, list.pop(i))
#print(list)

# Задача 3 - Решение через словарь
#month_num = int(input("Пожалуйста, введите месяц в виде целого числа от 1 до 12: "))
#if month_num < 1 or month_num > 12:
#    print("Неверный ввод! Пожалуйста измените вводимое значение.")
#month_in_dict = {1: "Зима", 2: "Зима",3: "Весна",4: "Весна",5: "Весна",6: "Лето",7: "Лето",8: "Лето",9: "Осень",10: "Осень",11: "Осень",12: "Зима"}
#print(month_in_dict.get(month_num))

# Задача 3 - Решение через список
#month_num = int(input("Пожалуйста, введите месяц в виде целого числа от 1 до 12: "))
#if month_num < 1 or month_num > 12:
#    print("Неверный ввод! Пожалуйста измените вводимое значение.")
#month_in_list = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]
#print(month_in_list[month_num - 1])

# Задача 4
#input_data = input("Пожалуйста, введите строку из нескольких слов, разделённых пробелами: ")
#
#if " " in list(input_data):
#    for num, vlu in enumerate(input_data.split()):
#        print(num, vlu[:10])
#else:
#    print("Пожалуйста, введите больше одного слова!")

#Задача 5
#my_list = [7, 5, 3, 3, 2]
#
#while True:
#    print("Для выхода введите exit")
#    new_value = input("Пожалуйста, введите целое число: ")
#    if new_value == "exit":
#        break
#    else:
#        new_value = int(new_value)
#        if new_value in my_list:
#            my_list.insert(my_list.index(new_value) + my_list.count(new_value), new_value)
#            print(my_list)
#        elif new_value not in my_list and max(my_list) < new_value:
#            my_list.insert(0, new_value)
#            print(my_list)
#        elif new_value not in my_list and min(my_list) > new_value:
#            my_list.append(new_value)
#            print(my_list)
#        elif new_value not in my_list:
#           my_list.append(new_value)
#           my_list.sort(reverse=True)
#           print(my_list)
#        else:
#            print("Введите верное значение!")

# Задача 6
print("ДЛЯ ВЫХОДА ВВЕДИТЕ - exit")
print("ЧТОБЫ ПОСМОТРЕТЬ ИТОГОВЫЙ СПИСОК  ВВЕДИТЕ - list")
print("АНАЛИТИКА АВТОМАТИЧЕСКИ БУДЕТ ПОДГРУЖАТЬСЯ!")
print()

goods = []
dict_list = {"название": "", "цена": "", "количество": "", "eд": ""}
dict_analytics = {"название": [], "цена": [], "количество": [], "eд": []}
number = 0


while True:
    na = 0
    na_2 = 0

    print("Пожалуйста введите харектиристики товара через точку с запятой (;). Пример - (название;цена;количество;единица измерения)")
    enter_value = input("Пожалуйста введите значение ")
    if enter_value == "exit":
        break
    elif enter_value == "list":
        print(goods)
        continue
    enter_value_list = enter_value.split(";")
    if len(enter_value_list) != 4:
        print("НЕВЕРНЫЙ ФОРМАТ ВВОДА!")
        continue
    number += 1
    for i in dict_list.keys():
        dict_list[i] = enter_value_list[na]
        na += 1
    for i in dict_analytics.keys():
        dict_analytics[i].append(enter_value_list[na_2])
        na_2 += 1
    goods.append((number, dict_list))
    for key, value in dict_analytics.items():
        print(f'{key} : {value}')
