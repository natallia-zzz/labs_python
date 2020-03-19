import math

f = input("input a .txt file with numbers: ")
# fil = open("7_lab_2_1.txt")
fil = open(f)
str = fil.read()
test = [int(s) for s in str.split() if s.isdigit()]
# это возврaщает все числа в файле(без пробелов и в массиве)
print(test)
print("You have a list of numbers. You will be given the sum of elements in range l to r.")
ll = int(input("Enter l: "))
while ll <= 0:
    print("Integer must be positive. reenter")
    ll = int(input("Enter l: "))
rr = int(input("Enter r: "))
while rr <= 0:
    print("Integer must be positive. reenter")
    rr = int(input("Enter r: "))
# длина массива
wh = len(test)
# количество блоков
nu = int(math.sqrt(wh - 1)) + 1
# количество чисел в блоках.
le = int((wh - 1) / nu) + 1
# считаем сумму в блоках
presum = [0] * nu
i = 0
while i < wh:
    presum[int(i / le)] += test[i]
    i += 1
# тк нумерация идет с нуля, предположим, что пользователь считает, что 0й элемент это первый
sum = 0
i = ll - 1
while i < rr:
    if i % le == 0 and i + le - 1 <= rr - 1:
        sum += presum[int(i / le)]
        i += le
    else:
        sum += test[i]
        i += 1
print(sum)
# как вариант еще можно сделать так, чтоб пользователь прямо в программе вводил числа через запятую или пробе;:
# print("enter a list of numbers: ")
# str2 = input()
# test2 = [int(s) for s in str2.split() if s.isdigit()]
# если вместо test подставить test2, порграмма также посчитает
