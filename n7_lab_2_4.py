

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
            if isinstance(el, int):
                count += 1
        if count == len(a):
            break
        else:
            b = a
            a = []
    print(a)


a_list = [1, [2, 3], 4, [5, [6, 7], 8], 9]
flatten_it(a_list)
