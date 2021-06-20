import math
import random


class Calc:

    def plus(self, num1, num2):
        print("Сумма = ", float(num1 + num2))

    def minus(self, num1, num2):
        print("Разность = ", float(num1 - num2))

    def multi(self, num1, num2):
        print("Произведение = ", float(num1 * num2))

    def div(self, num1, num2):
        print("Частное = ", float(num1 / num2))

    def exp(self, num1, num2):
        print(num1, "в степени", num2, "=", float(num1 ** num2))

    def mod(self, num1):
        print("Модуль числа = ", float(abs(num1)))

    def rand(self, num1, num2):
        print("Случайное число = ", random.uniform(num1, num2))

    def fact(self, num1):
        print(num1, "! = ", math.factorial(num1))

    def arc(self, num1):
        print("Арккосинус", num1, "=", math.acos(num1), "рад")


c = Calc()

print('Возможные операторы: +, -, *, /')
print('^ - возведение в степень, m - модуль, r - рандом, fac - факториал, arc - арккосинус')
print('Для выхода наберите ex')
Operator = input("Введите оператор : ")
while Operator != "ex":
    if Operator == "+":
        c.plus(float(input("Первое число: ")), float(input("Второе число: ")))
    elif Operator == "-":
        c.minus(float(input("Первое число: ")), float(input("Второе число: ")))
    elif Operator == "*":
        c.multi(float(input("Первое число: ")), float(input("Второе число: ")))
    elif Operator == "/":
        c.div(float(input("Первое число: ")), float(input("Второе число: ")))
    elif Operator == "^":
        c.exp(float(input("Первое число: ")), float(input("Второе число: ")))
    elif Operator == "m":
        c.mod(float(input("Введите число: ")))
    elif Operator == "r":
        c.rand(float(input("Введите верхнюю границу случайного числа: ")),
               float(input("Введите нижнюю границу случайного числа: ")))
    elif Operator == "fac":
        c.fact(int(input("Введите целое неотрицательное число: ")))
    elif Operator == "arc":
        c.arc(float(input("Введите число в диапазоне от -1 до 1: ")))
    Operator = input("Введите оператор : ")