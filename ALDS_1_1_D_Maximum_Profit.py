import sys

n = int(input())
if not (2 <= int(n) <= 200000):
    print('Please integer n is 2 or more and 20000 less.', sys.stderr)
    exit(1)

r_list = list()
for i in range(n):
    r = int(input())
    if not (1 <= r <= 10 ** 9):
        print('Please integer r is 1 or more and 10**9 less.', sys.stderr)
        exit(1)
    r_list.append(r)

maximumBenefit = -sys.maxsize
minimumValue = sys.maxsize
for i in range(len(r_list)):
    if minimumValue > r_list[i]:
        minimumValue = r_list[i]
    benefit = r_list[i] - minimumValue
    if maximumBenefit < benefit:
        maximumBenefit = benefit

#    for j in range(i + 1, len(integer_r)):
#        benefit = integer_r[j] - integer_r[i]
#        if maxBenefit < benefit:
#            maxBenefit = benefit

print(maximumBenefit)



