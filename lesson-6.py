# Задача 1
# from time import sleep
#
# class TrafficLight:
#    __color = "Отсутствует"
#
#     def running(self):
#         while True:
#             print('Красный цвет - ДВИЖЕНИЕ ЗАПРЕЩЕНО!')
#             sleep(7)
#             print('Желтый цвет - ДВИЖЕНИЕ ЗАПРЕЩЕНО, приготовиться к смене цвета!')
#             sleep(2)
#             print('Зеленый цвет - ДВИЖЕНИЕ РАЗРЕШЕНО')
#             sleep(7)
#
# trafficlight = TrafficLight()
# trafficlight.running()
#
# Задача 2
# class Road:
#
#     def __init__(self, length, width):
#         self._l = length
#         self._w = width
#
#     def calculation(self):
#         result = (self._l * self._w * 25 * 5) / 1000
#         return f"{self._l}м * {self._w}м * 25кг * 5 см = {result} тонн"
#
# length_input = int(input("Пожалуйста введите длину дорожного полотона (м): "))
# width_input = int(input("Пожалуйста введите ширину дорожного полотона (м): "))
#
# road_calc = Road(length_input, width_input)
# print(road_calc.calculation())
#
# Задча 3
# class Worker:
#
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": wage, "bonus": bonus}
#
# class Position(Worker):
#     def get_full_name(self):
#         return f'{self.surname} {self.name}'
#
#     def get_total_income(self):
#         return f'{sum(self._income.values())}'
#
#
# print("Заполните данные сотрудника с позицией Аналитик")
# surname_input = input("Пожалуйста, введите фамилию сотрудника: ")
# name_input = input("Пожалуйста, введите имя сотрудника: ")
# wage_input = float(input("Пожалуйста, введите зарплату сотрудника (за год): "))
# bonus_input = float(input("Пожалуйста, введите премию сотрудника (за год): "))
#
# Analyst = Position(name_input, surname_input, "Аналитик", wage_input, bonus_input)
#
# print(f'{Analyst.get_full_name()} ({Analyst.position}) - доход f{Analyst.get_total_income()}')
#
# Задача 4
# class Car:
#
#     def __init__(self, speed, color, name, is_police=False):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self):
#         return f'{self.name} ({self.color}) - поехала!'
#
#     def stop(self):
#         return f'{self.name} ({self.color}) - остановилась!'
#
#     def turn(self, direction):
#         direction_calc = ""
#         if direction == "r" or "R":
#             direction_calc = "направо"
#         if direction == "l" or "L":
#             direction_calc = "налево"
#         return f'Машина повернула {direction_calc}'
#
#     def show_speed(self):
#         return f'Текущая скорость автомобиля {self.name}: {self.speed} км/ч'
#
# class TownCar(Car):
#     def show_speed(self):
#         if self.speed > 60:
#             return f'Текущая скорость автомобиля {self.name}: {self.speed} км/ч. ПРЕВЫШЕНИЕ!'
#         else:
#             return f'Текущая скорость автомобиля {self.name}: {self.speed} км/ч.'
#
# class WorkCar(Car):
#     def show_speed(self):
#         if self.speed > 40:
#             return f'Текущая скорость автомобиля {self.name}: {self.speed} км/ч. ПРЕВЫШЕНИЕ!'
#         else:
#             return f'Текущая скорость автомобиля {self.name}: {self.speed} км/ч.'
#
# class SportCar(Car):
#     pass
#
# class PoliceCar(Car):
#     def __init__(self, speed, color, name, is_police=False):
#         super().__init__(speed, color, name, is_police)
#
# print("Введите запрашиваемую информацию по городскому автомобилю: ")
# name_input = input('Введите название машины: ')
# color_input = input('Введите цвет машины: ')
# speed_input = int(input('Введите скорость движения машины: '))
# turn_input = input('Куда повернула машина? (для поворота налево введите букву L, для поворота направо R) ')
# town_car = TownCar(speed_input, color_input, name_input)
# print(town_car.go())
# print(town_car.turn(turn_input))
# print(town_car.show_speed())
# print(town_car.stop())
#
# print("---------------------------------------------------")
# print("Введите запрашиваемую информацию по рабочему автомобилю: ")
# name_input = input('Введите название машины: ')
# color_input = input('Введите цвет машины: ')
# speed_input = int(input('Введите скорость движения машины: '))
# turn_input = input('Куда повернула машина? (для поворота налево введите букву L, для поворота направо R) ')
# work_car = WorkCar(speed_input, color_input, name_input)
# print(work_car.go())
# print(work_car.turn(turn_input))
# print(work_car.show_speed())
# print(work_car.stop())
#
# print("---------------------------------------------------")
# print("Введите запрашиваемую информацию по спортивному автомобилю: ")
# name_input = input('Введите название машины: ')
# color_input = input('Введите цвет машины: ')
# speed_input = int(input('Введите скорость движения машины: '))
# turn_input = input('Куда повернула машина? (для поворота налево введите букву L, для поворота направо R) ')
# sport_car = SportCar(speed_input, color_input, name_input)
# print(sport_car.go())
# print(sport_car.turn(turn_input))
# print(sport_car.show_speed())
# print(sport_car.stop())
#
# print("---------------------------------------------------")
# print("Введите запрашиваемую информацию по полицейскому автомобилю: ")
# name_input = input('Введите название машины: ')
# color_input = input('Введите цвет машины: ')
# peed_input = int(input('Введите скорость движения машины: '))
# turn_input = input('Куда повернула машина? (для поворота налево введите букву L, для поворота направо R) ')
# police_car = PoliceCar(speed_input, color_input, name_input)
# print(police_car.go())
# print(police_car.turn(turn_input))
# print(police_car.show_speed())
# print(police_car.stop())
# print("---------------------------------------------------")
#
# Задача 5
# class Stationery:
#
#     def __init__(self, title=input("Введите цвет: ")):
#         self.title = title
#
#     def draw(self):
#         print(f'Запуск отрисовки.')
#
# class Pen(Stationery):
#     def draw(self):
#         print(f"Рисую ручкой с цветом - {self.title}")
#         print()
#
# class Pencil(Stationery):
#     def draw(self):
#         print(f"Рисую карандашом с цветом - {self.title}")
#         print()
#
# class Handle(Stationery):
#     def draw(self):
#         print(f"Рисую маркером с цветом - {self.title}")
#         print()
#
# message = Stationery()
# message.draw()
#
# pen = Pen()
# pen.draw()
# pen = Pencil()
# pen.draw()
# pen = Handle()
# pen.draw()