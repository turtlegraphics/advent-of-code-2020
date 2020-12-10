#
# Advent of Code 2020
# Bryan Clair
#
# Day 10
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

adapters = []
for line in inputlines:
    adapters.append(int(line))

adapters.append(0)
adapters.sort()
device = max(adapters)+3
adapters.append(device)

diffs = {0:0,1:0,2:0,3:0}
for i in range(len(adapters)-1):
    diffs[adapters[i+1] - adapters[i]] += 1

print 'part 1:',diffs[1]*diffs[3]

paths = {device:1}
for i in range(len(adapters)-2,-1,-1):
    paths[adapters[i]]=0
    try:
        for x in range(1,4):
            diff = adapters[i+x] - adapters[i]
            if diff <= 3:
                paths[adapters[i]] += paths[adapters[i+x]]
    except IndexError:
        pass

print 'part 2:',paths[0]
