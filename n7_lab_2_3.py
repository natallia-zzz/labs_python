import argparse
import os
import tempfile
import math


def merge_sort(a):  # функция сортировки
    if len(a) > 1:
        half = int((len(a)+1) / 2)
        left_a = a[:half]
        right_a = a[half:]
        merge_sort(left_a)
        merge_sort(right_a)
        i = j = k = 0
        while i < len(left_a) and j < len(right_a):
            if left_a[i] < right_a[j]:
                a[k]= left_a[i]
                i += 1
            else:
                a[k]= right_a[j]
                j += 1
            k += 1
        while i < len(left_a):
            a[k] = left_a[i]
            i += 1
            k += 1
        while j < len(right_a):
            a[k] = right_a[j]
            j += 1
            k += 1

MEM_LIMIT = 400000000  # ограничение в памяти


def merge_sort_file(file):
    f = open(file)
    temp_files = []
    lines = []
    bytes = 0
    while True:
        line = f.readline()
        bytes += len(line)
        if line == '':
            break
        line = line.split()
        merge_sort(line)
        lines.append(' '.join(line) + '\n')
        if bytes > MEM_LIMIT:
            merge_sort(lines)
            temp_files.append(write_temp_file(lines))
            lines = []
            bytes = 0
    merge_sort(lines)
    temp_files.append(write_temp_file(lines))


def write_temp_file(lines):  # создаем временные файлы 
    tmp = tempfile.TemporaryFile()
    for line in lines:
        tmp.append(line.encode('utf-8'))
    return tmp


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("title", type=str, help="title of file to be sorted")
    arg = parser.parse_args()
    if arg.title is not None:
        txtfile = str(arg.title) + '.txt'
    else:
        txtfile = input("введите имя файла:\n") + '.txt'
    merge_sort_file(txtfile)




if __name__ == '__main__':
    main()
