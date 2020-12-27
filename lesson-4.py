# Задача 1
# from sys import argv
#
# name, work_hours, rate_per_hour, bonus = argv
# try:
#     salary = (float(work_hours) * float(rate_per_hour)) + float(bonus)
#     print(f"заработная плата сотрудника: {salary:.2f}")
# except ValueError:
#     print("Все вводимые переменные должны быть числами!")
#
# Задача 2
# initial_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# print([initial_list[num] for num in range(1, len(initial_list)) if initial_list[num] > initial_list[num -1]])

# Задача 3
# print([i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0])
#
# Задача 4
# my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# print([i for i in my_list if my_list.count(i) <= 1])
#
# Задача 5
# from functools import reduce
# print(reduce(lambda v1, v2: v1 * v2, [i for i in range(100, 1001) if i % 2 == 0]))
#
# Задача 6
# from itertools import count, cycle
#
# start_value = int(input("Пожалуйста, введите любое число с которого вы хотите сгенерировать список: "))
# stop_value = int(input("Пожалуйста, введите любое число до которого вы хотите сгенерировать список: "))
# input_list = []
#
# for i in count(start_value):
#     if i > stop_value:
#         break
#     input_list.append(i)
# print(input_list)
#
# cycle_times = int(input("Сколько раз повторить элементы списка? "))
# counter = 1
#
# for n in cycle(input_list):
#     if counter > cycle_times:
#         break
#     print(n)
#     counter += 1
#
# Задача 7
# from itertools import count
# from math import factorial
#
# factorial_dict = {}
#
# n = int(input("Введите число: "))
#
# def fact_gen():
#     for v1 in count(1):
#         yield factorial(v1)
# counter = 0
# for v2 in fact_gen():
#     if counter == n:
#         break
#     else:
#         counter += 1
#         factorial_dict[counter] = v2
#
# print(factorial_dict)