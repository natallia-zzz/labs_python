import sys


def div_by_two(n):
    while True:
        if n.isdigit():
            n = int(n)
            break
        else:
            print("повторите ввод")
    i = 0
    if n <= 0:
        print("Число отрицательное и не может быть 2^n")
        exit()
    while True:
        if n == 1:
            print("2^0")
            break
        elif n % 2 == 1:
            print("число не является 2^n")
            break
        else:
            n /= 2
            i += 1
            if n == 1:
                print(str(num) + " это 2^" + str(i))
                break


def main():
    n = sys.argv[1]
    div_by_two(n)


if __name__ == '__main__':
    main()
