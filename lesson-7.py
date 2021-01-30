# Задача 1
# class Matrix:
#     def __init__(self, matrix):
#         self.matrix = matrix
#
#     def __str__(self):
#         return '\n'.join(map(lambda i: '    '.join(map(str, i)), self.matrix)) + '\n'
#
#     def __add__(self, other):
#         return Matrix(map(lambda v1, v2: map (lambda a, b: a + b, v1, v2), self.matrix, other.matrix))
#
# matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
# matrix_2 = Matrix([[1, 2], [3, 4], [5, 6]])
# print(matrix_1 + matrix_2)
#
#
# Задача 2
# from abc import ABC, abstractmethod
#
# class Clothing(ABC):
#     def __init__(self, input_data):
#         self.input_data = input_data
#
#     @property
#     @abstractmethod
#     def material_flow(self):
#         pass
#
#     def __add__(self, other):
#         return self.material_flow + other.material_flow
#
#
# class Coat(Clothing):
#     @property
#     def material_flow(self):
#         return self.input_data / 6.5 + 0.5
#
# class Suit(Clothing):
#     @property
#     def material_flow(self):
#         return (2 * self.input_data + 0.3) / 100
#
# coat_input = int(input("Подалуйста, введите размер пальто: "))
# suit_input = int(input("Подалуйста, введите рот для костюма: "))
#
# coat = Coat(coat_input)
# suit = Suit(suit_input)
# ttl = coat + suit
# print(f"Общий расход такни - {ttl:.2f}")
#
# Задача 3
class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return self.cell

    def __add__(self, other):
        return f'Сумма клеток: {self.cell + other. cell}'

    def __sub__(self, other):
        return self.cell - other.cell if self.cell - other.cell > 0 \
            else f'Ошибка! Первое значение меньше второго!'

    def __mul__(self, other):
        return f'Умножение клеток: {self.cell * other. cell}'

    def __floordiv__(self, other):
        return f'Деление клеток: {self.cell // other. cell}'

    def make_order(self, row):
        return '\n'.join(['*' * row for i in range(self.cell // row)]) + '\n' + '*' * (self.cell % row)

cell_1 = Cell(12)
cell_2 = Cell(13)
print(cell_1 + cell_2)
print(cell_2.make_order(5))