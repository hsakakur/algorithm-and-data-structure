import sys
import math


def binary_search(target, array):
    if len(array) == 1 and array[0] != target:
        print(str(target) + " : " + str(array))
        return False

    key = math.floor((len(array) / 2))
    if array[key] < target:
        return binary_search(target, array[key + 1: len(array)])
    elif array[key] > target:
        return binary_search(target, array[0: key])
    else:
        return True


n = int(input())
if not (0 <= n <= 100_000):
    print('Please integer n is 0 or more and 100,000 less.', sys.stderr)
    exit(1)
s = list(map(int, input().split(" ")))
for i in range(len(s)):
    if not (0 <= s[i] <= 10 ** 9):
        print('Please element of sequence s is 0 or more and 10**9 less.', sys.stderr)
        exit(1)
for i in range(len(s) - 1):
    if s[i] > s[i + 1]:
        print('Please sequence s is not ascending order', sys.stderr)
        exit(1)
if n != len(s):
    print('Please sequence s length is n value', sys.stderr)
    exit(1)

q = int(input())
if not (0 <= q <= 50_000):
    print('Please integer n is 0 or more and 500,00, less.', sys.stderr)
    exit(1)
t = list(map(int, input().split(" ")))
for et in t:
    if not (0 <= et <= 10 ** 9):
        print('Please element of sequence t is 0 or more and 10**9 less.', sys.stderr)
        exit(1)
if q != len(t):
    print('Please sequence t length is q value', sys.stderr)
    exit(1)

count = 0
for et in t:
    if binary_search(et, s):
        count += 1
print(count)
