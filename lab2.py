name = input("введите слово:")
last_name = name[:-1]
str_name = " "
for x in range(0, len(last_name)):
    if x != 2:
        str_name = str_name + last_name[x]
print(str_name)
if name.find("с") >= 0:
    print("есть символ с")
