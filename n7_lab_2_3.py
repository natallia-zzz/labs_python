import argparse
import tempfile
import sys


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
                a[k] = left_a[i]
                i += 1
            else:
                a[k] = right_a[j]
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
    whole = line_count(file)
    f = open(file)
    temp_files = []
    lines = []
    part = bytes = 0
    while True:
        line = f.readline()
        bytes += len(line)
        part += 0.5
        status(part, whole)
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
    part = whole/2
    status(part, whole)
    while len(temp_files) > 1:
        f1 = temp_files.pop(0)
        f2 = temp_files.pop(0)
        f3 = merge_files(f1, f2)
        temp_files.append(f3)
    f = open(file, 'w+b')
    tmp = temp_files.pop()
    tmp.seek(0)
    while True:
        line = tmp.readline()
        part += 0.5
        status(part, whole)
        if line == b'':
            break
        f.write(line)
    print('100%')


def write_temp_file(lines):  # создаем временные файлы
    tmp = tempfile.TemporaryFile()
    for line in lines:
        tmp.write(line.encode('utf-8'))
    return tmp


def merge_files(file1, file2):  # чтоб собрать временные файлы в один отсортированный документ
    file1.seek(0)
    file2.seek(0)
    tmp = tempfile.TemporaryFile()
    line1 = file1.readline()
    line2 = file2.readline()
    while line1 != b'' and line2 != b'':  # аналогично алгоритму mergesort
        if line1 < line2:
            tmp.write(line1)
            line1 = file1.readline()
        else:
            tmp.write(line2)
            line2 = file2.readline()
    while line1 != b'':
        tmp.write(line1)
        line1 = file1.readline()
    while line2 != b'':
        tmp.write(line2)
        line2 = file2.readline()
    return tmp


def line_count(file):
    f = open(file)
    n = 0
    line = f.readline()
    print("preparing")
    while line != '':
        n += 1
        line = f.readline()
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')
    f.close()
    return n


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("title", type=str, help="title of file to be sorted")
    arg = parser.parse_args()
    if arg.title is not None:
        txtfile = arg.title + '.txt'
    else:
        txtfile = input("введите имя файла:\n") + '.txt'
    merge_sort_file(txtfile)


def status(part, whole):
    part *= 100
    print(str(int(part / whole)) + '%')
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')


if __name__ == '__main__':
    main()
