def nameLow(name):
    print(name.lower())


def nameUp(name):
    print(name.upper())


def nameTit(name):
    print(name.title())


def outSum(name, count):
    print('{} - {} кг.'.format(name.title(), count))


vegetable1 = input("первый овощ: ")
vegetable2 = input("второй овощ: ")
vegetable3 = input("третий овощ: ")

nameLow(vegetable1)
nameUp(vegetable1)
nameTit(vegetable1)

nameLow(vegetable2)
nameUp(vegetable2)
nameTit(vegetable2)

nameLow(vegetable3)
nameUp(vegetable3)
nameTit(vegetable3)

countVegetable1 = input("сколько первого овоща: ")
countVegetable2 = input("сколько второго овоща: ")
countVegetable3 = input("сколько третьего овоща: ")

outSum(vegetable1, countVegetable1)
outSum(vegetable2, countVegetable2)
outSum(vegetable3, countVegetable3)