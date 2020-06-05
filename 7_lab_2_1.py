import math


def create_array(zz):
    if zz == "file":
        f = input("Подключаем файл. Наберите путь к .txt файлу: ")
        fil = open(f)
        str1 = fil.read()
        test1 = [int(s) for s in str1.split() if s.isdigit()]
        return test1
    elif zz == "input":
        print("Введите массив чисел ")
        str2 = input()
        test2 = [int(s) for s in str2.split() if s.isdigit()]
        return test2
    else:
        print("К сожалению вы не выбрали предложенные результаты. Создадим массив для примера")
        while True:
            try:
                rand = int(input("введите длину: "))
                break
            except ValueError:
                print("повторите ввод: ")
        test3 = list(range(rand))
        return test3


def sqrt_decomposition(test):
    print("Массив: " + str(test))
    print("Выберите отрезок l до r.")
    wh = len(test)  # длина массива
    while True:
        ll = input("введите l: ")
        if ll.isdigit():
            ll = int(ll)
            if ll < wh:
                break
            else:
                print("повторите ввод: ")
        else:
            print("повторите ввод: ")
    while True:
        rr = input("введите r: ")
        if rr.isdigit():
            rr = int(rr)
            if ll < rr < wh:
                break
            else:
                print("повторите ввод: ")
        else:
            print("повторите ввод: ")
    nu = int(math.sqrt(wh - 1)) + 1  # количество блоков и чисел в каждом блоке
    pre_sum = [0] * nu  # считаем сумму в блоках.
    for i in range(wh):
        pre_sum[int(i / nu)] += test[i]
    # тк нумерация идет с нуля, предположим, что пользователь считает, что 0й элемент это первый
    sum = 0
    for i in range(ll - 1, rr):
        if i % nu == 0 and i + nu - 1 <= rr - 1:
            sum += pre_sum[int(i / nu)]
            i += nu
        else:
            sum += test[i]
            i += 1
    print("Сумма: " + str(sum))


print("Эта программа найдет сумму чисел на отрезке массива от r до l")
print("Если хотите подключить файл с массивом, введите 'file'. Если сами наберете массив, введите 'input'")
z = input("вводите: ")  # пользователь выбирает как задает массив
final_test = create_array(z)
sqrt_decomposition(final_test)
