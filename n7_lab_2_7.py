import argparse


def leo_num(n):
    try:
        n = int(n)
        if n < 0:
            print(str(n) + " - отрицательнoe число. Нет такого числа Леонардо.")
        else:
            a = [1, 1]
            for i in range(2, n):
                a.append(1 + a[i - 2] + a[i - 1])
            print(str(n)+"-е число Леонардо: " + str(a[-1]))
    except ValueError:
        print("неправильный параметр")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--num", type=int, help="integer for function", nargs="*")
    args = parser.parse_args()
    if args.num is not None:
        for x in args.num:
            leo_num(x)
    else:
        print("Напишите exit когда захотите завершить работу")
        n = input("введите число: ")
        while True:
            if n == 'exit':
                break
            else:
                leo_num(n)
                n = input("введите другое число: ")


if __name__ == '__main__':
    main()
