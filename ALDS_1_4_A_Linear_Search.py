import sys

n = int(input())
if not (0 <= n <= 10_000):
    print('Please integer n is 0 or more and 10,000 less.', sys.stderr)
    exit(1)
s = list(map(int, input().split(" ")))
for es in s:
    if not (0 <= es <= 10**9):
        print('Please element of sequence s is 0 or more and 10**9 less.', sys.stderr)
        exit(1)
if n != len(s):
    print('Please sequence s length is n value', sys.stderr)
    exit(1)

q = int(input())
if not (0 <= q <= 500):
    print('Please integer n is 0 or more and 500 less.', sys.stderr)
    exit(1)
t = list(map(int, input().split(" ")))
for et in t:
    if not (0 <= et <= 10**9):
        print('Please element of sequence t is 0 or more and 10**9 less.', sys.stderr)
        exit(1)
if q != len(t):
    print('Please sequence t length is q value', sys.stderr)
    exit(1)

count = 0
#for es in s:
#    for et in t:
#        if es == et:
#            count += 1
#            break
# 番兵法でやってみよう
for et in t:
    s.append(et)
    i = 0
    n = len(s) - 1
    while s[i] != et:
        i += 1
    count = count + 1 if i != n else count

print(count)