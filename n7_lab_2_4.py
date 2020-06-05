import argparse


def flatten_it(some_list, key='', connect='_'):
    if isinstance(some_list, dict):
        for k, v in some_list.items():
            new = key + connect + k if key else k
            if isinstance(v, dict):
                yield from flatten_it(v, new, connect=connect)
            else:
                yield tuple([new, v])
    else:
        for elem in some_list:
            if isinstance(elem, (list, dict, tuple, set)):
                yield from flatten_it(elem)
            else:
                yield elem


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-mt", "--make_tuple", help="create tuple", default=None)
    parser.add_argument("-in", "--int_in", type=int, nargs='+', help="integer in list", action='append')
    parser.add_argument("-cin", "--char_in", type=str, nargs='+', help="character in list", action='append')
    parser.add_argument("-i", "--int", type=int, nargs='+', help="integer")
    parser.add_argument("-c", "--char", type=str, nargs='+', help="character")
    parser.add_argument("-t", "--tuple", nargs='+', help="tuple", action='append')
    parser.add_argument("-s", "--set", nargs="+", help="set", action='append')
    args = parser.parse_args()
    argu = [args.char_in, args.int_in, args.int, args.char]
    list = []
    for x in argu:
        if x is not None:
            list.append(x)
    if args.set is not None:
        for x in args.set:
            x = set(x)
            list.append(x)
    if args.tuple is not None:
        for x in args.tuple:
            x = tuple(x)
            list.append(x)
    if args.make_tuple is not None:
        list = tuple(list)
    print(list)
    try:
        final = [x for x in flatten_it(list)]
        if args.make_tuple is not None:
            final = tuple(final)
        print(final)
    except RecursionError:
        print("ValueError")


if __name__ == "__main__":
    main()
