import sys


def show(a):
    str_a = map(str, a)
    print(' '.join(str_a))


def selection_sort(a, n):
    swap_count = 0
    for i in range(0, n - 1):
        min_j = i
        flag = False
        for j in range(i + 1, n):
            if a[j] < a[min_j]:
                min_j = j
                flag = True
        a[i], a[min_j] = a[min_j], a[i]
        swap_count = swap_count + 1 if flag else swap_count

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

swap_count = selection_sort(int_list, n)
show(int_list)
print(swap_count)