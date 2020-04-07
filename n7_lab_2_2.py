import random as r
import string as s
import os
import sys
import argparse


def status(sze, mb):
    sze *= 100
    print(str(int(sze / mb)) + '%')
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')


def gen_file(title, mb, k, ll):
    mb = int(mb)
    if k is not None:
        k = tuple(k)
    else:
        k = ()
    if ll is not None:
        ll = tuple(ll)
    else:
        ll = ()
    txtfile = str(title) + '.txt'
    file = open(txtfile, 'a')
    f_size = 0
    while f_size < mb:
        if k == ():
            kk = r.randint(10, 100)
        else:
            kk = r.randint(k[0], k[1])
        sentence = [0] * kk
        for i in range(kk):
            if ll == ():
                len = r.randint(3, 10)
            else:
                len = r.randint(ll[0], ll[1])
            a = [0] * len
            for j in range(len):
                a[j] = r.choice(s.ascii_letters)
            sentence[i] = ''.join(a)
        sent = ' '.join(sentence)
        sent += '\n'  # добавление переноса строки
        file.write(sent)
        f_size = os.stat(txtfile).st_size  # in bytes
        f_size /= 1000000
        status(f_size, mb)
    print('100%')


def main():
    parser = argparse.ArgumentParser(description="creates file")
    parser.add_argument("-t", "--title", type=str, help="Название файла", default="text")
    parser.add_argument("-mb", "--size", type=int, help="размер файла", default=10)
    parser.add_argument("-k", "--sent", type=int, nargs=2, help="tuple для размера строк")
    parser.add_argument("-l", "--word", type=int, nargs=2, help="tuple для размера слов")
    args = parser.parse_args()
    gen_file(args.title, args.size, args.sent, args.word)


if __name__ == "__main__":
    main()
