#
# Advent of Code 2020
# Bryan Clair
#
# Day 24
#
import sys
import re
sys.path.append("..")
import aocutils as aoc

args = aoc.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

floor = aoc.HexGrid()
origin = aoc.HexPoint()
floor[origin] = 'w'

row = 0
for line in inputlines:
    line = re.sub('e','e ',line)
    line = re.sub('w','w ',line)
    dirs = line.split()
    row += 1

    p = aoc.HexPoint(origin)

    for d in dirs:
        try:
            cur = floor[p]
        except KeyError:
            cur = 'w'
        floor[p] = cur
        p.move(d)

    try:
        cur = floor[p]
    except KeyError:
        cur = 'w'
    floor[p] = cur

    if floor[p] == 'w':
        floor[p] = 'b'
    else:
        floor[p] = 'w'

def count_black():
    black = 0
    for k in floor.raster:
        if floor.raster[k] == 'b':
            black += 1
    return black

def art_move():
    blacks = {}
    for p in floor:
        if floor[p] == 'b':
            for n in floor.neighbors(aoc.HexPoint(p),validate=False):
                n = (n.x,n.y)
                if n not in blacks:
                    blacks[n] = 1
                else:
                    blacks[n] += 1

    for p in floor:
        cur = floor[p]
        if p in blacks:
            nbs = blacks[p]
        else:
            nbs = 0
        if cur == 'w' and nbs == 2:
            floor[p] = 'b'
        if cur == 'b' and (nbs == 0 or nbs > 2):
            floor[p] = 'w'

    for n in blacks:
        if blacks[n] == 2:
            floor[aoc.HexPoint(n)] = 'b'

print 'part 1:',count_black()

for i in range(100):
    art_move()

print 'part 2:',count_black()
