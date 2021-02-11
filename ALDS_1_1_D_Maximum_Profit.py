import sys

integer_n = int(input())
if not (2 <= int(integer_n) <= 200000):
    print('Please integer n is 2 or more and y 20000 less.', sys.stderr)
    exit(1)

integer_r = list()
for i in range(integer_n):
    r = int(input())
    if not (1 <= r <= 10 ** 9):
        print('Please integer r is 1 or more and y 10**9 less.', sys.stderr)
        exit(1)
    integer_r.append(r)

maximumBenefit = -sys.maxsize
minimumValue = sys.maxsize
for i in range(len(integer_r)):
    if minimumValue > integer_r[i]:
        minimumValue = integer_r[i]
    benefit = integer_r[i] - minimumValue
    if maximumBenefit < benefit:
        maximumBenefit = benefit

#    for j in range(i + 1, len(integer_r)):
#        benefit = integer_r[j] - integer_r[i]
#        if maxBenefit < benefit:
#            maxBenefit = benefit

print(maximumBenefit)



