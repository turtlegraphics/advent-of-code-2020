#
# Advent of Code 2020
# Bryan Clair
#
# Day 01
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

nums = {}
found = False
for line in inputlines:
    v = int(line)
    for w in nums:
        if 2020-v-w in nums:
            print 'found',v,'*',w,'*',2020-v-w,'=',v*w*(2020-v-w)
            break
    if 2020-v in nums:
        print 'found',v,'*',2020-v,'=',v*(2020-v)
    nums[v] = True

