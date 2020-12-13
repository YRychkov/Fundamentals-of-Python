#Задача 1
#print("Добро пожаловать в калькулятор!")
#a = int(input("Введите первую перменную (перменную a): "))
#b = int(input("Введите вторую перменную (перменную b): "))
#print("Пожалуйста, выберите маетматическое действие из списка: сложение(+), вычетание(-), умножение(*) или деление(/)")
#mathematical_operation = input("Введите значение: ")
#if mathematical_operation == "+":
#    print(f"Результат: {a + b:.2f}")
#elif mathematical_operation == "-":
#    print(f"Результат: {a - b:.2f}")
#elif mathematical_operation == "*":
#    print(f"Результат: {a * b:.2f}")
#elif mathematical_operation == "/":
#    print(f"Результат: {a / b:.2f}")
#else:
#    print("Введено неизвестное значние!")

#Задача 2
#seconds_input = int(input("Введите количество секунд: "))
#hours = int(seconds_input / 3600)
#minutes = int((seconds_input - hours * 3600) / 60)
#seconds = int(seconds_input - hours * 3600 - minutes * 60)
#print(f"{hours:02}:{minutes:02}:{seconds:02}")

#Задача 3
#n = int(input("Введите любое число: "))
#nn = str(n) + str(n)
#nnn = str(n) + str(n) + str(n)
#
#print(n + int(nn) + int(nnn))

#Задача 4
#num = int(input("Введите целое положительное число: "))
#result = -1
#if num <= 9:
#    print(num)
#else:
#    while num > 10:
#        max_num = num % 10
#        num //= 10
#        if max_num > result:
#            result = max_num
#    print(result)

#Задача 5
#income = int(input("Пожалуйста, введите значение выручки:"))
#outcome = int(input("Пожалуйста, введите значение издержек:"))
#
#if income - outcome > 0:
#    print("Ваша компания работает в ПРИБЫЛЬ!")
#    print(f"Рентабильность Вашей компании: {(income - outcome) / income:.2f}")
#    employees_number = int(input("Пожалуйста, введите количество сотрудников: "))
#    print(f"Прибыль в расчете на одного чловека равна: {(income - outcome) / employees_number:.2f}")
#if income - outcome < 0:
#    print("Ваша компания работает в УБЫТОК!")
#if income - outcome == 0:
#    print("Ваша компания работает в НОЛЬ!")

#Задача 6
a = float(input("Введите результат первого дня: "))
b = float(input("Введите желаемый результат: "))

if a <= 0 or b <= 0:
    print("Введите положительное значение!")
else:
    i = 1
    print("РЕЗУЛЬТАТ:")
    print(f"{i}-й день: {a:.2f}")
    while True:
        a = a + (a * 0.1)
        i += 1
        if a >= b:
            print (f"{i}-й день: {a:.2f}")
            break
        print(f"{i}-й день: {a:.2f}")
    print(f"Ответ: на {i}-й день спортсмен достиг результата — не менее {b} км.")