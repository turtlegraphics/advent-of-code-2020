#
# Advent of Code 2019
# Bryan Clair
#
# Day 02
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

p1count = 0
p2count = 0

for line in inputlines:
    srange,sletter,word = line.split()
    letter = sletter[0]
    low,high = [int(x) for x in srange.split('-')]
    num = word.count(letter)
    if num >= low and num <= high:
        p1count += 1
    if (word[low-1]+word[high-1]).count(letter) == 1:
        p2count += 1

print 'part 1:',p1count
print 'part 2:',p2count



    
