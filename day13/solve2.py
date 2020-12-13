#
# Advent of Code 2020
# Bryan Clair
#
# Day 13
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

mytime = int(inputlines[0])
buses = inputlines[1].split(',')

busids = []
departs = []
t = 0
for x in buses:
    if x != 'x':
        busids.append(int(x))
        departs.append(-t)
    t += 1

print mytime
print busids
print departs

for x in busids:
    print -mytime % x

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
 
    for n_i, a_i in zip(n, a):
        p = prod / n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a / b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
 
print chinese_remainder(busids, departs)
