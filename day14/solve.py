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

def writeall(loc,val,floats):
    if len(floats) == 0:
        if args.verbose > 1:
            print 'writing {0:b}'.format(loc),'<--',val
        mem[loc] = val
        return
    
    f = floats[0]
    loc2 = loc | f
    if loc2 == loc:
        loc2 = loc - f
    writeall(loc,val,floats[1:])
    writeall(loc2,val,floats[1:])

for line in inputlines:
    if args.verbose > 1:
        print line
    op,eq,val = line.split()
    assert(eq == '=')
    if op == 'mask':
        zero = 0
        one = 0
        floats = []
        float = 2**36

        for c in list(val):
            zero *= 2
            one *= 2
            float /= 2
            if c != '0':
                zero += 1
            if c == '1':
                one += 1
            if c == 'X':
                floats.append(float)
    else:
        m,vc = op.split('[')
        loc = (int(vc[:-1]) | one)
        writeall(loc,int(val),floats)
    
tot = 0    
for loc in mem:
    tot += mem[loc]

print 'Part 2:',tot
