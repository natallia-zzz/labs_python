import math

# n = int(input("input a number greater than 0: "))
test = list(range(17))
wh = len(test)
# количество блоков
nu = int(math.sqrt(wh - 1)) + 1
# количество чисел в блоках.
le = int((wh - 1) / nu) + 1
# считаем сумму в блоках
presum = [0] * nu
for i in test:
    presum[int(i / le)] += test[i]
ll = 2
rr = 8
sum = 0
# тк нумерация идет с нуля, предположим, что пользователь считает, что 0й элемент это первый
i = ll-1
while i < rr:
    if i % le == 0 and i + le - 1 <= rr-1:
        sum += presum[int(i / le)]
        i += le
    else:
        sum += test[i]
        i += 1
print(sum)
