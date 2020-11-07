"""Задания по ветвлениям, итерациям и вводу данных."""

# напиши функцию, которая принимает на вход любое
# количество чисел и сообщает, есть ли среди них чётное

def hasEven(number_array):
    if any(i % 2 == 0 for i in number_array): print('has an even number')
    else: print('has no even number')

# используй тернарный оператор, чтобы вызвать функцию
# если возраст больше 21 года, в противном случае верни
# сообщение "Мы не продаём алкоголь несовершеннолетним."

age = 17
sell_alcohol() if age >= 21 else print('Мы не продаём алкоголь несовершеннолетним.')

# напиши функцию, которая проверит, является ли строка ключевым словом в Питоне
# тебе понадобится модуль keyword, импортируй его и изучи с помощью dir()

import keyword
def is_kw(str):
    return str in keyword.kwlist

# напиши функцию, которая возвращает тип данных на русском языке:
# число, строка, булевый, None, список, кортеж, множество, словарь
# пример: get_type("что-то") возвращает "Это строка."
# пример2: get_type(42) возвращает "Это словарь."

def rus_type(object):
    if type(object) == "<class 'int'>": print('число')
    elif type(object) == "<class 'float'>": print('число')
    elif type(object) == "<class 'bool'>": print('булевый')
    elif type(object) == "<class 'str'>": print('строка')
    elif type(object) == "<class 'NoneType'>": print('None')
    elif type(object) == "<class 'list'>": print('список')
    elif type(object) == "<class 'tuple'>": print('кортеж')
    elif type(object) == "<class 'set'>": print('множество')
    elif type(object) == "<class 'dict'>": print('словарь')