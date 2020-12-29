# Задача 1
# with open("file_1.txt", "w+", encoding="utf-8") as my_file:
#     input_list = []
#    while True:
#         input_data = str(input("Пожалуйста введите любой текст: "))
#         if input_data == "":
#             break
#         input_list.append(f"{input_data}\n")
#     my_file.writelines(input_list)
#     print(f"Запись файла завершена! Пожалуйста откройте файл {my_file.name}")
#
# Задача 2
# with open("file_1.txt", "r", encoding="utf-8") as my_file:
#     import_list = my_file.readlines()
#     print(f"Всего строк в файле: {len(import_list)}")
#     counter = 1
#     for i in import_list:
#         print(f'В {counter}-й строке всего слов: {str(i).count(" ") + 1}')
#         counter += 1
#
# Задача 3
# with open("file_3.txt", "r", encoding="utf-8") as my_file:
#     import_list = my_file.readlines()
#     data_dict = {}
#     salaries = []
#
#     for i in import_list:
#         data_dict = data_dict | dict([str(i).split()])
#     for key, vlu in data_dict.items():
#         data_dict[key] = float(vlu)
#     print("Сотрудники с окладом менее 20 тыс.: ")
#     for key, vlu in data_dict.items():
#         if vlu < 20000:
#             print(key)
#         salaries.append(vlu)
#     print(f"Средний доход сотрудников: {sum(salaries) / len(salaries)}")
#
# Задача 4
# english_russian_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять', 'Six': 'Шесть', 'Seven': 'Семь', 'Eight': 'Восемь', 'Nine': 'Один', 'Ten': 'Десять'}
# data_dict = {}
#
# with open("file_4.txt", "r", encoding="utf-8") as my_file:
#
#     import_list = my_file.readlines()
#     new_vlu_list = []
#
#     for i in import_list:
#         new_vlu_list.append(i.split())
#     counter = 0
#     while counter != len(new_vlu_list):
#         new_vlu_list[counter].remove('-')
#         counter += 1
#     for i in new_vlu_list:
#         data_dict[i[1]] = i[0]
#     counter = 1
#     while counter != len(data_dict) + 1:
#         data_dict[str(counter)] = english_russian_dict[data_dict[str(counter)]]
#         counter += 1
#
# with open("file_4_translated.txt", "w+", encoding="utf-8") as my_new_file:
#     for key, vlu in data_dict.items():
#         my_new_file.writelines(f"{vlu} - {key}\n")
#
# Задача 5
# with open("file_5.txt", "w+", encoding="utf-8") as my_file:
#     input_str = ''
#     input_data = int(input("Введите любое число, чтобы записать диапазон в файл: "))
#
#     for i in range(1, input_data + 1):
#         input_str += f"{i} "
#     my_file.write(input_str)
#     print(f"Значения записаны в файл: {input_str}")
#     my_file.seek(0)
#     print(f"Сумма значений в файле: {sum(map(float, (my_file.read()).split()))}")
#
# Задача 6
# with open("file_6.txt", "r", encoding="utf-8") as my_file:
#     import_list = my_file.readlines()
#     data_dict = {}
#     for i in import_list:
#         counter = 0
#         new_string = i.split()
#         new_string[0] = new_string[0].replace(":", "")
#         if new_string.count('-') != 0:
#             while counter <= new_string.count('-'):
#                 new_string.remove('-')
#                 counter += 1
#         counter = 1
#         for n in new_string:
#             if n.count('(') != 0:
#                 new_string[counter] = int(n[:n.index('(')])
#                 counter += 1
#         data_dict = data_dict | dict([(new_string[0], sum(new_string[1:]))])
#     print(data_dict)
#
# Задача 7
# import json
#
# with open("file_7.txt", "r", encoding="utf-8") as my_file:
#     import_list = my_file.readlines()
#     data_dict = {}
#     mean_dict = {}
#     final_list = []
#     mean = 0
#     counter = 0
#
#     for i in import_list:
#         new_string = i.split()
#         data_dict = data_dict | dict([(new_string[0], int(new_string[2]) - int(new_string[3]))])
#         if int(new_string[2]) - int(new_string[3]) > 0:
#             mean += int(new_string[2]) - int(new_string[3])
#             counter += 1
#     mean_dict = {'average_profit': mean / counter}
#     final_list = [data_dict, mean_dict]
#
# with open("file_7.json", "w") as write_f:
#     json.dump(final_list, write_f)
