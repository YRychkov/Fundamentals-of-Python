# Задача 1
# class Date(object):
#
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split('-'))
#         date1 = cls(day, month, year)
#         return date1
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         day, month, year = map(int, date_as_string.split('-'))
#         return day <= 31 and month <= 12 and year <= 3999
#
# date2 = Date.from_string('28-01-2021')
# is_date = Date.is_date_valid('28-01-2021')
#
# Задача 2
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.
#
# class MyOwnErr(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
# in_data_1 = int(input("Введите делимое: "))
# print(f"{in_data_1} / ? = ")
# print()
# in_data_2 = int(input("Введите делитель: "))
#
# try:
#     if in_data_2 == 0:
#         raise MyOwnErr("Деление на ноль - невозможно!")
# except (ValueError, MyOwnErr) as err:
#     print(err)
# else:
#     print()
#     print(f"{in_data_1} / {in_data_2} = {in_data_1 / in_data_2}")
#
# Задача 3
# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить
# работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.
#
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, команду «stop». При этом скрипт завершается, сформированный список с числами выводится на
# экран.
#
# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. Во время ввода
# пользователем очередного элемента необходимо реализовать проверку типа элемента. Вносить его в список, только если
# введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее
# сообщение. При этом работа скрипта не должна завершаться.
#
# class MyOwnErr(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
#
# final_list = []
#
# print("Для выхода введите q")
#
# while True:
#     in_data = input("Введите число: ")
#
#     try:
#         if in_data == "q":
#             raise MyOwnErr("Конец цикла")
#         in_data = int(in_data)
#     except ValueError:
#         print("Можно вводить ТОЛЬКО числа!")
#     except (MyOwnErr) as err:
#         print()
#         print(err)
#         break
#     else:
#         final_list.append(in_data)
#         continue
#
# print("Сформированный список: ")
# print(final_list)
#
# Задача 7
class ComplexNumber:
    a_list = []
    b_list = []

    def __init__(self):
        self.a = None
        self.a = None

    def getinput(self):
        self.a = input("Введите первое комплексное число: ")
        self.b = input("Введите второе комплексное число: ")

    def formatting(self):
        print(ComplexNumber.a_list.append(self.a[1:len(self.b)-1].split()))
        print(ComplexNumber.b_list.append(self.a[1:len(self.b) - 1].split()))

    def __add__(self, other, sum_result=''):
        sum_result = f'({int(self.a_list[0]) + int(self.b_list[0])} + {int(self.a_list[2].replace("j", "")) + int(self.b_list[2].replace("j", ""))}j)'
        return sum_result

one = ComplexNumber()
one.getinput()
one.formatting()
print()



#
#
# num = '(1 + 2j)'
# action = input('Please choose action (+ or *): ')
# num_new = num[1:len(num)-1]
# num_list = num_new.split()
# print(num_list)
#
# num2 = '(10 + 3j)'
# num_new2 = num2[1:len(num2)-1]
# num_list2 = num_new2.split()
# print(num_list2)
#
# if action == '+':
#     sum_result = f'({int(num_list[0]) + int(num_list2[0])} + {int(num_list[2].replace("j", "")) + int(num_list2[2].replace("j", ""))}j)'
#     print(f'A + B = {num} + {num2} = ({num_list[0]} + {num_list2[0]}) + ({num_list[2].replace("j", "")} + {num_list2[2].replace("j", "")})j = {sum_result}')
#
# if action == '*':
#     prod_result = f'({int(num_list[0]) * int(num_list2[0]) - int(num_list[2].replace("j", "")) * int(num_list2[2].replace("j", ""))} + {int(num_list[2].replace("j", ""))*int(num_list2[0]) + int(num_list[0])*int(num_list2[2].replace("j", ""))}j)'
#     print(f'A * B = {num} * {num2} = ({num_list[0]} * {num_list2[0]} - {num_list[2].replace("j", "")} * {num_list2[2].replace("j", "")}) + ({num_list[2].replace("j", "")}*{num_list2[0]} + {num_list[0]}*{num_list2[2].replace("j", "")})j = {prod_result}')
