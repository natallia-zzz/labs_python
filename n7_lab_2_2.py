import random as r
import string as s
import os
import sys
import argparse


def status(sze, mb):
    print(str(sze / mb) + '%')
    # setup toolbar
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width + 1))  # return to start of line, after '['
    for i in xrange(toolbar_width):
        time.sleep(0.1)  # do real work here
        # update the bar
        sys.stdout.write("-")
        sys.stdout.flush()
    sys.stdout.write("]\n")  # this ends the progress bar


def gen_file(title, mb, k, ll):
    txtfile = title + 'txt'
    file = open(txtfile, 'a')
    f_size = 0
    while not f_size == mb:
        kk = r.randint(10, 100) if k == () else kk = r.randint(k(0), k(1))
        sentence = [0]*kk
        for i in range(kk):
            len = r.randint(3, 10) if ll == () else len = r.randint(ll(0), ll(1))
            a = [0]*len
            for j in range(len):
                a[j] = r.choice(s.ascii_letters)
            sentence[i] = ''.join(a)
        sentence = sentence + '\n'  # добавление переноса строки
        file.write(sentence)
    f_size = os.stat(txtfile).st_size  # in bytes
    f_size /= 10000
    status(f_size, mb)


def main():
    arg
