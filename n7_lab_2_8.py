import argparse


def div_by_two(n):
    try:
        n = int(n)
    except ValueError:
        print("неправильно введен параметр")
        return
    if n <= 0:
        print(str(n) + " отрицательное и не может быть 2^n")
        return
    if n == 1:
        print(str(n) + "2^0")
        return
    i = 0
    num = n
    while n != 1:
        if n % 2 == 1:
            print(str(n) + " не является 2^n")
            break
        else:
            n /= 2
            i += 1
            if n == 1:
                print(str(num) + " это 2^" + str(i))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--num", type=int, help="integer for function", nargs='*')
    args = parser.parse_args()
    if args.num is not None:
        for x in args.num:
            div_by_two(x)
    else:
        print("Напишите exit когда захотите завершить работу")
        n = input("введите число:\n")
        while True:
            if n == 'exit':
                break
            else:
                div_by_two(n)
                n = input("введите другое число:\n")


if __name__ == '__main__':
    main()
