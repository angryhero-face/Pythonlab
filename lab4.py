import math
import random
do = input("ввести арифметический оператор:")
if do == "+":
    num1 = float(input("ввести первое значение:"))
    num2 = float(input("ввести второе значение:"))
    print(num1 + num2)
elif do == "-":
    num1 = float(input("ввести первое значение:"))
    num2 = float(input("ввести второе значение:"))
    print(num1 - num2)
elif do == "/":
    num1 = float(input("ввести первое значение:"))
    num2 = float(input("ввести второе значение:"))
    print(num1 / num2)
elif do == "*":
    num1 = float(input("ввести первое значение:"))
    num2 = float(input("ввести второе значение:"))
    print(num1 * num2)
elif do == "pow":
    num1 = float(input("ввести первое значение:"))
    num2 = float(input("ввести второе значение:"))
    print(pow(num1, num2))
elif do == "module":
    num1 = float(input("ввести значение:"))
    print(abs(num1))
elif do == "0":
    print(random.randint(-999999, 999999))
elif do == "div":
    num1 = float(input("ввести первое значение:"))
    num2 = float(input("ввести второе значение:"))
    print(num1//num2)
elif do == "mod":
    num1 = float(input("ввести первое значение:"))
    num2 = float(input("ввести второе значение:"))
    print(num1 % num2)
elif do == "f":
    num1 = int(input("ввести  значение:"))
    print(math.factorial(num1))
elif do == "arccos":
    num1 = float(input("ввести значение:"))
    num3 = num1*math.pi/180
    print(math.acos(num3))