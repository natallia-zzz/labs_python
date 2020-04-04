import sys


def leo_num(n):
    while True:
        try:
            n = int(n)
            if n > -1:
                break
            else:
                print("повторите ввод")
        except ValueError:
            print("повторите ввод")
    a = [1, 1]
    for i in range(2, n):
        a.append(1 + a[i - 2] + a[i - 1])
    print(a[-1])


def main():
    n = sys.argv[1]
    leo_num(n)


if __name__ == '__main__':
    main()
