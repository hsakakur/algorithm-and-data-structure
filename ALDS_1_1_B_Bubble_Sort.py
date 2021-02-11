import sys


def show(a):
    str_a = map(str, a)
    print(' '.join(str_a))


def bubble_sort(a, n):
    swap_count = 0
    flag = True
    while flag:
        flag = False
        for i in reversed(range(1, n)):
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]
                flag = True
                swap_count += 1
    return swap_count

n = int(input())
if not (0 <= n <= 100):
    print('Please integer n is 0 or more and 100 less.', sys.stderr)
    exit(1)

int_list = list(map(int, input().split(" ")))
for ne in int_list:
    if not (0 <= ne <= 100):
        print('Please element of integer list is 0 or more and 1000 less.', sys.stderr)
        exit(1)

if n != len(int_list):
    print('Please integer list length is n value', sys.stderr)
    exit(1)

swap_count = bubble_sort(int_list, n)
show(int_list)
print(swap_count)