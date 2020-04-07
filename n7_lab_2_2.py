import random as r
import string as s
import os
import sys


def status(sze, mb):
    sze *= 100
    sys.stdout.write(str(sze / mb) + '%')
    sys.stdout.flush()


def gen_file(title, mb, k, ll):
    txtfile = title + '.txt'
    file = open(txtfile, 'a')
    f_size = 0
    while f_size < mb:
        if k == ():
            kk = r.randint(10, 100)
        else:
            kk = r.randint(k(0), k(1))
        sentence = [0]*kk
        for i in range(kk):
            if ll == ():
                len = r.randint(3, 10)
            else:
                len = r.randint(ll(0), ll(1))
            a = [0]*len
            for j in range(len):
                a[j] = r.choice(s.ascii_letters)
            sentence[i] = ''.join(a)
        ' '.join(sentence)
        sentence = sentence + '\n'  # добавление переноса строки
        file.write(sentence)
        f_size = os.stat(txtfile).st_size  # in bytes
        # f_size /= 1000000
        status(f_size, mb)


def main():
    title = sys.argv[1]
    while True:
        try:
            mb = int(sys.argv[2])
            if mb < 0:
                mb = 0 - mb
            break
        except ValueError:
            mb = r.randint(1, 1000)
            break
    if isintance(sys.argv[3], tuple):
        k = sys.argv[3]
    else:
        k = ()
    if isintance(sys.argv[4], tuple):
        ll = sys.argv[4]
    else:
        ll = ()
    gen_file(title, mb, k, ll)

if __name__ == "__main__":
    main()