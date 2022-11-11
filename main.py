"""Функція пошуку найбільшого і найменшого числа з 2-х чисел"""


def min_max():
    print("Введіть число А")
    number_a = input()
    print("Введіть число B")
    number_b = input()
    if number_a > number_b:
        print("Найбільше число А: ", number_a)
    elif number_a == number_b:
        print("Числа А і В онакові")
    else:
        print("Найбільше число B: ", number_b)
    print("\n")


'''Функція пошуку найменшого числа з 3-х чисел'''


def number_min():
    print("Введіть число А")
    number_a = input()
    print("Введіть число B")
    number_b = input()
    print("Введіть число C")
    number_c = input()
    number = [number_a, number_b, number_c]
    print("Найменше число: ", min(number))
    print("\n")


'''Функція  визначення модулю числа '''


def number_module():
    print("Введіть число А")
    number_mod = float(input())
    number_mod = abs(number_mod)
    print("Модуль числа", number_mod)
    print("\n")


'''Функція  визначення сими значень '''


def sum_number():
    print("Введіть перше число")
    first_number = float(input())
    print("Введіть друге число")
    second_number = float(input())
    print("Сума чисел:", first_number + second_number)
    print("\n")


'''Функція  визначення позитивного чи негативного числа'''


def pozitiv_negativ():
    print("Введіть число")
    number = int(input())
    if number > 0:
        print("Число ПОЗИТИВНЕ")
    elif number == 0:
        print("число дорівнює 0")
    else:
        print("число НЕГАТИВНЕ")


if __name__ == "__main__":
    min_max()
    number_min()
    number_module()
    sum_number()
    pozitiv_negativ()
