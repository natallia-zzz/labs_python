import argparse


def leo_num(n):
    if not isinstance(n, int):
        print("неправильно введенное число")
    elif n < 0:
        print("нет такого числа. введенный параметр отрицательный ")
    else:
        a = [1, 1]
        for i in range(2, n):
            a.append(1 + a[i - 2] + a[i - 1])
        print(a[-1])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--num", type=int, help="integer for function", nargs=1)  # только одно число
    args = parser.parse_args()
    if args.num is not None:
        leo_num(args.num)
    else:
        print("Напишите exit когда захотите завершить работу")
        n = input("введите число: ")
        while True:
            try:
                if n == 'exit':
                    break
                n = int(n)
                if n < 0:
                    n = input("Число отрицательное. Повторите ввод: ")
                else:
                    leo_num(n)
                    n = input("введите число: ")
            except ValueError:
                n = input("Это не число. Повторите ввод: ")


if __name__ == '__main__':
    main()
