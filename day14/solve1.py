#
# Advent of Code 2020
# Bryan Clair
#
# Day 14
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

mem = {}
for line in inputlines:
    if args.verbose > 1:
        print line
    op,eq,val = line.split()
    assert(eq == '=')
    if op == 'mask':
        zero = 0
        one = 0
        for c in list(val):
            zero *= 2
            one *= 2
            if c != '0':
                zero += 1
            if c == '1':
                one += 1
    else:
        m,vc = op.split('[')
        loc = int(vc[:-1])
        mem[loc] = (int(val) | one) & zero
    
tot = 0    
for loc in mem:
    tot += mem[loc]

print 'Part 1:',tot
