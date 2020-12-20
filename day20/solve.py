#
# Advent of Code 2020
# Bryan Clair
#
# Day 20
#
import sys
import re
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

def flip(s):
    return s[::-1]

class Tile:
    def __init__(self,pic):
        self.rows = pic.strip().split('\n')
        self._edges = None
        assert(len(self.rows) == len(self.rows[0])) # square

    def __str__(self):
        return '\n'.join(self.rows)

    def striprow(self,x):
        """Return xth row of tile without 1 character frame"""
        return self.rows[x+1][1:-1]

    def edges(self):
        """Return list of edges"""
        if not self._edges:
            top = self.rows[0]
            bottom = self.rows[-1]
            left = ''.join([r[0] for r in self.rows])
            right = ''.join([r[-1] for r in self.rows])
            self._edges = [top,bottom,left,right,
                    flip(top),flip(bottom),flip(left),flip(right)]
        return self._edges

    def rightedge(self):
        self._edges = None
        return self.edges()[3]

    def flip(self):
        self.rows = flip(self.rows)

    def rotate(self):
        newrows = []
        for i in range(len(self.rows)):
            newrows.append(''.join([r[i] for r in self.rows]))
        self.rows = flip(newrows)

    def turnup(self,edge):
        """Rotate and flip tile so edge is the top row, left to right."""
        assert(edge in self.edges())
        #print 'turnup!'
        #print self
        step = 0
        while edge != self.rows[0]:
            self.rotate()
            step += 1
            if step == 4:
                self.flip()
            #print
            #print self
            assert(step < 8)

class Ocean(Tile):
    pass

tilestr = open(args.file).read().split('\n\n')
tiles = {}
for t in tilestr:
    id,tiletxt = t.split(':')
    id = int(id.split()[1])
    tiles[id] = Tile(tiletxt)
    
if args.verbose > 2:
    for t in tiles:
        print t
        print tiles[t]

edges = {}
for t in tiles:
    for e in tiles[t].edges():
        if e in edges:
            edges[e].append(t)
        else:
            edges[e] = [t]

#lens = [0,0,0]
#for e in edges:
#    lens[len(edges[e])] += 1
#print 'edge counts',lens

corners = []
for t in tiles:
    badct = 0
    for e in tiles[t].edges():
        if len(edges[e]) == 1:
            badct += 1
    if badct == 4:
        corners.append(t)

if args.verbose > 1:
    print 'corners:',corners
# corners found, compute part 1 answer here
part1 = 1
for x in corners:
    part1 *= x

# orient start corner correctly
start_tile_id = corners[3] # arbirary choice but matches the test data
start_tile = tiles[start_tile_id]

for e in start_tile.edges():
    if len(edges[e]) == 1:
        start_tile.turnup(e)
rte = start_tile.rightedge()
if len(edges[rte]) == 1:
    start_tile.flip()
    start_tile.turnup(rte)

def follow(id):
    """Return list of tiles below the start tile, orient them all vertically"""
    column = [id]
    while True:
        the_tile = column[-1]
        the_edge = tiles[the_tile].rows[-1]
        connection = edges[the_edge]
        if len(connection) == 1:
            break
        next_tile = connection[0]
        if next_tile == the_tile:
            next_tile = connection[1]

        tiles[next_tile].turnup(the_edge)

        column.append(next_tile)
        the_tile = next_tile
    return column

toprow = follow(start_tile_id)

tiling = []
for t in toprow:
    tiles[t].rotate()
    tiles[t].rotate()
    tiles[t].rotate()
    tiling.append(follow(t))
# fight it into the right place
tiling = [list(x) for x in zip(*tiling)] # transpose
for row in tiling:
    row.reverse()

# IT'S MADE!

# print tile ids in the correct grid
if args.verbose > 1:
    print '\n'.join([' '.join([str(id) for id in row]) for row in tiling])

# build the image by pasting borderless tiles together
fullimage = ''
for row in tiling:
    for x in range(8):
        for id in row:
            fullimage += tiles[id].striprow(x)
        fullimage += '\n'

ocean = Ocean(fullimage)
ocean.rotate() # to match test image

monsterstr ="""
..................#.
#....##....##....###
.#..#..#..#..#..#...
"""

monster = monsterstr.strip('\n').split('\n')
monster = [re.compile(s) for s in monster]


def hunt(ocean,monster,mark=False):
    found = []
    for r in range(len(ocean.rows)-2):
        row = ocean.rows[r]
        m0 = monster[0].search(row)
        while m0:
            # matched row 1 of the monster
            #print r,m0.start()
            m1 = monster[1].search(ocean.rows[r+1], pos = m0.start())
            m2 = monster[2].search(ocean.rows[r+2], pos = m0.start())
            #try:
            #    print ':',r,m0.start(),m1.start(),m2.start()
            #except:
            #    pass
            if m1 and m2:
                if m1.start() == m0.start() and m2.start() == m0.start():
                    found.append((r,m0.start()))
            m0 = monster[0].search(row, pos = m0.start() + 1)
    return found

found = hunt(ocean,monster)
while not found:
    ocean.rotate()
    found = hunt(ocean,monster)

# print found

monster = monsterstr.strip('\n').split('\n')

def mark(ocean,x,y):
    for dy in range(3):
        r = list(ocean.rows[y+dy])
        for dx in range(len(monster[0])):
            if monster[dy][dx] == '#':
                r[x+dx] = 'O'
        ocean.rows[y+dy] = ''.join(r)

for (y,x) in found:
    mark(ocean,x,y)

count = 0
for c in str(ocean):
    if c == '#':
        count +=1

if args.verbose > 1:
    print re.sub('O','\033[42mO\033[0m',str(ocean))

print 'Part 1:', part1
print 'Part 2:', count

