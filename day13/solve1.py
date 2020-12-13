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
for x in buses:
    if x != 'x':
        busids.append(int(x))

print mytime
print busids
for x in busids:
    print -mytime % x
