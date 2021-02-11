import sys


def show(a):
    str_a = map(str, a)
    print(' '.join(str_a))


def insertion_sort(a, n):
    for i in range(1, n):
        v = a[i]
        j = i - 1
        while j >= 0 and a[j] > v:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = v
        show(a)


n = int(input())
if not (0 <= n <= 100):
    print('Please integer n is 0 or more and 100 less.', sys.stderr)
    exit(1)

int_list = list(map(int, input().split(" ")))
for e in int_list:
    if not (0 <= e <= 1000):
        print('Please element of integer list is 0 or more and 1000 less.', sys.stderr)
        exit(1)

if n != len(int_list):
    print('Please integer list length is n value', sys.stderr)
    exit(1)

show(int_list)
insertion_sort(int_list, n)