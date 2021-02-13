# import sys
#
# count = 0
#
# def show(a):
#     str_a = map(str, a)
#     print(' '.join(str_a))
#
#
# def insertion_sort(a, n, g):
#     global count
#     for i in range(g, n):
#         v = a[i]
#         j = i - g
#         while j >= 0 and a[j] > v:
#             a[j + g] = a[j]
#             j = j - g
#             count += 1
#         a[j + g] = v
#
# def shell_sort(a, n):
#     global count
#     count = 0
#     m = ?
#     g = [?, ?, ?]
#     for i in range(m - 1?):
#         insertion_sort(a, n, g)
#
