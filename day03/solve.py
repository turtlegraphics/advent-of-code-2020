#
# Advent of Code 2019
# Bryan Clair
#
# Day 03
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

prod = 1
for dx in [1,3,5,7,0.5]:
    count = 0
    x = 0
    for y in range(len(inputlines)):
        i = int(x)
        if i == x:
            if inputlines[y][i] == '#':
                count += 1
        x = (x + dx) % len(inputlines[y])
    print dx,':',count
    prod *= count
print 'product:',prod
