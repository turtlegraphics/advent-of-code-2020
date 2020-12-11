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

dirs = [(1,0), (1,1), (1,-1), (0,1), (0,-1), (-1,0), (-1,-1), (-1,1)]

def neighbors(grid,i,j):
    ocount = 0
    for (dx,dy) in dirs:
        x = i + dx
        y = j + dy
        if x >= 0 and y >= 0 and x < xmax and y < ymax and grid[x][y] == '#':
            ocount += 1
    return ocount

def visneighbors(grid,i,j):
    ocount = 0
    for (dx,dy) in dirs:
        x = i + dx
        y = j + dy
        while x >= 0 and y >= 0 and x < xmax and y < ymax:
            if grid[x][y] == '#':
                ocount += 1
                break
            if grid[x][y] == 'L':
                break
            x += dx
            y += dy
    return ocount

def countseats(grid):
    count = 0
    for i in range(xmax):
        for j in range(ymax):
            if grid[i][j] == '#':
                count += 1
    return count

def dump(grid):
    for row in grid:
        print ''.join(row)
    print 'occupied:',countseats(grid)
    
def sim(g,part):
    grid = copy.deepcopy(g)
    newgrid = copy.deepcopy(g)

    tolerance = 3+part
    neighborcount = neighbors if part == 1 else visneighbors
    iters = 0
    changed = True
    while changed:
        changed = False
        for i in range(xmax):
            for j in range(ymax):
                ocount = neighborcount(grid,i,j)
                here = grid[i][j]
                if here == 'L' and ocount == 0:
                    newgrid[i][j] = '#'
                    changed = True
                elif here == '#' and ocount >= tolerance:
                    newgrid[i][j] = 'L'
                    changed = True
                else:
                    newgrid[i][j] = here

        temp = grid
        grid = newgrid
        newgrid = temp
        iters += 1

    return iters, countseats(grid)

g = []
for line in inputlines:
    row = list(line)
    g.append(row)
xmax = len(g)
ymax = len(g[0])

print '%d x %d grid' % (ymax, xmax)
for part in [1,2]:
    iters, count = sim(g,part)
    print 'Part %d: %d (after %d iterations)' % (part,count,iters)
