#
# Advent of Code 2020
# Bryan Clair
#
# Day --
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

nums = [int(line) for line in inputlines]

def test(i):
    for x in range(i-25,i):
        for y in range(x,i):
            if nums[x]+nums[y] == nums[i]:
                return True
    return False


cur = 25
while cur < len(nums):
    if not test(cur):
        invalid = nums[cur]
        break
    cur += 1

print 'part 1:',invalid

for x in range(len(nums)):
    count = 0
    y = x
    while count < invalid:
        count += nums[y]
        y += 1
    if count == invalid:
        contig = nums[x:y]
        print 'part 2:', max(contig)+min(contig)
        sys.exit()
        
