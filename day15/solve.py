#
# Advent of Code 2020
# Bryan Clair
#
# Day 15
#
import sys
import re
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

start = [int(x) for x in inputlines[0].split(',')]

when = {}
for i in range(len(start)):
    when[start[i]] = i

print when

last = start[-1]
lastage = 0
t = len(start)
maxsaid = max(start)
maxdiff = 0

def tracer(say,t):
    global maxsaid, maxdiff
    if say >= maxsaid:
        print 'new max of',say,'on turn',t
        if say - maxsaid >= maxdiff:
            print 'difference',say - maxsaid
            maxdiff = say - maxsaid
        maxsaid = say
    
while True:
    if t == 2020:
        print 'Part 1:',last
        print 'Now wait for it (count to 30):'

    if t == 30000000:
        print 'Part 2:',last
        break

    if args.verbose > 2:
        print 'last:',last,'age:',lastage

    if lastage == 0:
        # new
        say = 0
    else:
        say = lastage

    if args.verbose > 2:
        print 'turn',t+1,'saying',say

    if args.verbose > 1:
        tracer(say,t+1)

    last = say
    if say in when:
        lastage = t - when[say]
    else:
        lastage = 0
    when[say] = t
    t += 1
    if t % 1000000 == 0:
        print t/1000000

    

