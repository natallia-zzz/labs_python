import random as r
import string as s
import os
import sys
import argparse


def status(sze, mb):
    print(str(sze / mb) + '%')
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
        sentence = sentence + '\n'  # добавление переноса строки
        file.write(sentence)
    f_size = os.stat(txtfile).st_size  # in bytes
    f_size /= 10000
    status(f_size, mb)



