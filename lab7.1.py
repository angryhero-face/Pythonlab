import math
import random


def plus(num1, num2):
    print(float(num1 + num2))


def minus(num1, num2):
    print(float(num1 - num2))


def multi(num1, num2):
    print(float(num1 * num2))


def div(num1, num2):
    print(float(num1 / num2))


def exp(num1, num2):
    print(num1, "^", num2, "=", float(num1 ** num2))


def mod(num1):
    print(float(abs(num1)))


def rand(num1, num2):
    print(random.uniform(num1, num2))


def fact(num1):
    print(num1, "fac = ", math.factorial(num1))


def arc(num1):
    print("arc", num1, "=", math.acos(num1), "rad")


print('Возможные операторы: +, -, *, /')
print('^ - возведение в степень, m - модуль, r - рандом, fac - факториал, arc - арккосинус')
Operator = input("Введите оператор : ")
if Operator == "+":
    plus(float(input("Первое число: ")), float(input("Второе число: ")))
elif Operator == "-":
    minus(float(input("Первое число: ")), float(input("Второе число: ")))
elif Operator == "*":
    multi(float(input("Первое число: ")), float(input("Второе число: ")))
elif Operator == "/":
    div(float(input("Первое число: ")), float(input("Второе число: ")))
elif Operator == "^":
    exp(float(input("Первое число: ")), float(input("Второе число: ")))
elif Operator == "m":
    mod(float(input("Введите число: ")))
elif Operator == "r":
    rand(float(input("Введите нижнюю границу случайного числа: ")),
         float(input("Введите верхнюю границу случайного числа: ")))
elif Operator == "fac":
    fact(int(input("Введите целое неотрицательное число: ")))
elif Operator == "arc":
    arc(float(input("Введите число в диапазоне от -1 до 1: ")))