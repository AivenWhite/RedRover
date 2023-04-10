"""4.1 Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
периметр квадрата, площадь квадрата и диагональ квадрата."""
from math import sqrt

def square(side) -> tuple:
    perimetr = (side + side) * 2
    square_of_square = side ** 2
    diagonal = sqrt(2 * square_of_square)
    return perimetr, square_of_square, diagonal

print(square(5))

"""4.5 Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра"""
from time import perf_counter

def function_time(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        func(*args, **kwargs)
        print(f'function time = {perf_counter()} - {start}')
    return wrapper

"""4.2 Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно 
    в формате аргумент: значение. Например:
	name: John
	last_name: Smith
	age: 35 
	position: web developer"""
@function_time
def print_names(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print_names(name='John', last_name='Smith', age=35, position='web developer')

"""4.3 Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только 
положительные числа
"""
my_list = [20, -3, 15, 2, -1, -21]
new_list = list(filter(lambda x: x > 0, my_list))
# print(new_list)


"""4.4 Используя лямбда выражение, получите результат перемножения значений в предыдущем списке """
# from functools import reduce
# print(reduce(lambda x, y: x * y, my_list))
