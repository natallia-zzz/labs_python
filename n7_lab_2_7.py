import argparse


def leo_num(n):
    if not isinstance(n,int):
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
    parser.add_argument("num", type=int, required=True, help="integer for function", nargs=1)  # только одно число
    args = parser.parse_args()
    leo_num(args.num)


if __name__ == '__main__':
    main()
