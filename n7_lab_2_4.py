import argparse


def flatten_it(some_list):
    b = some_list
    a = []
    while True:
        for elem in b:
            if isinstance(elem, list):
                for x in elem:
                    a.append(x)
            else:
                a.append(elem)
        count = 0
        for el in a:
            if not isinstance(el, list):
                count += 1
        if count == len(a):
            break
        else:
            b = a
            a = []
    convert_to_int(a)  # в argparse элементы сохраняются как string. переводим в int


def convert_to_int(some_list):
    a = []
    for i in some_list:
        try:
            i = int(i)
            a.append(i)
        except ValueError:
            pass
    print(a)


def main():
    a_list = [1, [2, 3], 4, [5, [6, 7], 8], 9]
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--list", type=list, nargs='*', help="array", default=a_list)
    args = parser.parse_args()
    flatten_it(args.list)


if __name__ == "__main__":
    main()
