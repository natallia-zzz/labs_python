import argparse
import os


def merge_sort(a):  # функция сортировки
    if len(a) > 1:
        half = int((len(a) + 1) / 2)
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


def sort_line(fi):  # сортировка строк
    for line in fi:
        line = line.split()
        merge_sort(line)
        line = ' '.join(line)
        fi.write(line)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("title", type=str, help="title of file to be sorted")
    arg = parser.parse_args()
    if arg.title is not None:
        txtfile = str(arg.title) + '.txt'
    else:
        txtfile = input("введите имя файла:\n") + '.txt'
    file = open(txtfile, 'w')



if __name__ == '__main__':
    main()
