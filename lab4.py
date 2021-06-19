
import math
import random
print('Возможные операторы: +, -, *, /')
print('^ - возведение в степень, m - модуль, r - рандом, fac - факториал, arc - арккосинус')
operator1 = input("Введите оператор : ")
if operator1 == 'r':
    print("Случайное число = ", random.uniform(-999999, 999999))
else:
    num1 = float(input("Введите первое число : "))
    if operator1 == 'm':
        print("Модуль числа = ", abs(num1))
    elif operator1 == 'fac':
        num3 = int(abs(num1))
        print("Факториал определен на множестве целых неотрицательных чисел.")
        print("Поэтому посчитаем факториал от ", num3)
        print(num3,"! = ", math.factorial(num3))
    elif operator1 == 'arc':
        if num1 < -1 or num1 > 1:
            print("Аргумент должен быть в диапазоне от -1 до 1")
        else: print("Арккосинус", num1, "=", math.acos(num1), "рад")
    else:
        num2 = float(input("Введите второе число : "))
        if operator1 == '+':
            print("Сумма = ", num1 + num2)
        elif operator1 == '-':
            print("Разность = ", num1 - num2)
        elif operator1 == '*':
            print("Произведение = ", num1 * num2)
        elif operator1 == '/':
            if num2 == 0:
                print("На 0 делить нельзя!")
            else: print("Частное = ", num1 / num2)
        elif operator1 == '^':
            print(num1, "в степени", num2, "=", num1 ** num2)