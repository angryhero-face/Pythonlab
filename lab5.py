vegetable1 = input("первый овощ:")
vegetable2 = input("второй овощ:")
vegetable3 = input("третий овощ:")
vegetablel1 = vegetable1.lower()
vegetablel2 = vegetable2.lower()
vegetablel3 = vegetable3.lower()
vegetableu1 = vegetable1.upper()
vegetableu2 = vegetable2.upper()
vegetableu3 = vegetable3.upper()
vegetablet1 = vegetable1.title()
vegetablet2 = vegetable2.title()
vegetablet3 = vegetable3.title()
vegetables1 = int(input("сколько" + vegetable1 + ": "))
vegetables2 = int(input("сколько" + vegetable2 + ": "))
vegetables3 = int(input("сколько" + vegetable3 + ": "))
print("{} кг {} ({}, {})".format(vegetables1, vegetablel1, vegetableu1, vegetablet1))
print("{} кг {} ({}, {})".format(vegetables2, vegetablel2, vegetableu2, vegetablet2))
print("{} кг {} ({}, {})".format(vegetables3, vegetablel3, vegetableu3, vegetablet3))