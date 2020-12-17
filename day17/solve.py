#
# Advent of Code 2020
# Bryan Clair
#
# Day 17
#
import sys
import re
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

state = {}
y = 0
z = 0
w = 0
for line in inputlines:
    x = 0
    for c in list(line):
        if c == '#':
            state[(x,y,z,w)] = True
        x += 1
    y += 1

deltas = []
for x in [-1,0,1]:
    for y in [-1,0,1]:
        for z in [-1,0,1]:
            for w in [-1,0,1]:
                if x or y or z or w:
                    deltas.append((x,y,z,w))

def step(state):
    newstate = {}
    for p in state:
        if not state[p]:
            continue
        (x,y,z,w) = p
        for (dx,dy,dz,dw) in deltas:
            q = (x + dx, y + dy, z + dz, w + dw)
            if q in newstate:
                newstate[q] += 1
            else:
                newstate[q] = 1
    for q in newstate:
        if q not in state:
            alive = False
        else:
            alive = state[q]
        if not alive and newstate[q] == 3:
            newstate[q] = True
        elif alive and newstate[q] in [2,3]:
            newstate[q] = True
        else:
            newstate[q] = False
    return newstate

for iter in range(6):
    state = step(state)

count = 0
for k in state:
    if state[k]:
        count += 1
print '(run solve1.py for part 1)'
print 'part 2:', count
