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
    print(a)


def main():
    parser = argparse.ArgumentParser()
    # parser.add_argument("-a", "--list", type=list, nargs='*', help="array") - будет работать так себе. если мы
    # введем [1, [2, 3], 4, [5, [6, 7], 8], 9], то оно сделает массив нам желаемый массив, но там все будет типа str
    # и еще будут символы '[' ,   ',' , ']'.
    parser.add_argument("-in", "--int_in", type=int, nargs='+', help="integer in list", action='append')
    parser.add_argument("-cin", "--char_in", type=str, nargs='+', help="character in list", action='append')
    parser.add_argument("-i", "--int", type=int, nargs='+', help="integer")
    parser.add_argument("-c", "--char", type=str, nargs='+', help="character")
    args = parser.parse_args()
    argu = [args.char_in, args.int_in, args.int, args.char]
    list = []
    for x in argu:
        if x is not None:
            list += x
    print(list)
    flatten_it(list)


if __name__ == "__main__":
    main()
