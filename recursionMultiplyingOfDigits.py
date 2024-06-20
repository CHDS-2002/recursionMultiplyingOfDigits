# Python 3.8
# os - библиотека для работы с консолью
# random - библиотека для работы со случайными данными

import os
import random

# Зададим цвет шрифта консоли
os.system('COLOR B')


# get_multiplied_digits - функция для произведения цифр числа
def get_multiplied_digits(number):
    str_number = str(number)  # конвертация числа в строку
    first = int(str_number[0])  # первая цифра числа

    # Процесс произведения
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


LEFT = 0  # LEFT - левая граница
RIGHT = 100000  # RIGHT - правая граница

number = random.randint(LEFT, RIGHT)
# number - случайное целое число
result = get_multiplied_digits(number)
# result - произведение цифр числа number

# Вывод результата произведения цифр result числа number
print(f'\nПроизведение цифр числа {number}: {result}.\n')

try:
    os.system('PAUSE')  # Остановка работы программы
    os.system('CLS')  # Очищение экрана консоли
except:
    os.system('CLS')  # Очищение экрана консоли
