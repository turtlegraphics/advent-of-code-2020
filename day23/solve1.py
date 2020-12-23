#
# Advent of Code 2020
# Bryan Clair
#
# Day 23
#
import sys
import re
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputstr = open(args.file).read().strip()

cups = [int(x)-1 for x in list(inputstr)]
N = len(cups)

def move(cup):
    cur = cup[0]
    pickup = cup[1:4]
    cup = cup[4:]
    cup.append(cur)
    dest = (cur - 1) % N
    while dest not in cup:
        dest = (dest - 1) % N
    #print 'dest =',dest+1
    loc = cup.index(dest)+1
    cup = cup[:loc] + pickup + cup[loc:] 
    return cup

def dump(cups):
    print ''.join([str(n + 1) for n in cups])

def state(cups):
    z = cups.index(0)
    rc = cups[z+1:] + cups[:z]
    dump(rc)

dump(cups)
for i in range(100):
    cups = move(cups)

state(cups)

