#
# Advent of Code 2020
# Bryan Clair
#
# Day 11
#
import sys
sys.path.append("..")
import aocutils
import copy

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

grid = []


def countseats(g):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if g[i][j] == '#':
                count += 1
    return count

for line in inputlines:
    row = list(line)
    grid.append(row)

iters = 0

newgrid = copy.deepcopy(grid)
count = copy.deepcopy(grid)

while True:
    dirs = [(1,0), (1,1), (1,-1), (0,1), (0,-1), (-1,0), (-1,-1), (-1,1)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            ocount = 0
            for (dx,dy) in dirs:
                x = i + dx
                y = j + dy
                if x >= 0 and y >= 0:
                    try:
                        if grid[x][y] == '#':
                            ocount += 1
                    except IndexError:
                        pass
            count[i][j] = str(ocount)
            here = grid[i][j]
            if here == 'L' and ocount == 0:
                newgrid[i][j] = '#'
            elif here == '#' and ocount >= 4:
                newgrid[i][j] = 'L'
            else:
                newgrid[i][j] = here

    temp = grid
    grid = newgrid
    newgrid = temp
    iters += 1
    if iters % 100 == 0:
        print
        print 'iteration', iters, 'occupied:',countseats(grid)
        for row in grid:
            print ''.join(row)
        print
        print
