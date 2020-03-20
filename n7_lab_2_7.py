def leo_num(n):
    a = [1, 1]
    if n < 0:
        print('Error. Number is less than 0')
    elif n == 1 or n == 0:
        print(1)
    else:
        b = range(n)
        for i in b[2:n]:
            a.append(1 + a[i - 2] + a[i - 1])
        print(a[-1])


# m = int(input())
# leo_num(m)
