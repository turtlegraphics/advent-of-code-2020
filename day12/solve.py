#
# Advent of Code 2020
# Bryan Clair
#
# Day 12
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

moves = []
for line in inputlines:
    op = line[0]
    amt = int(line[1:])
    moves.append((op,amt))


compass = {
    'N': (0,1),
    'S': (0,-1),
    'E': (1,0),
    'W': (-1,0)
}

headings = {
    90: (0,1),
    270: (0,-1),
    0: (1,0),
    180: (-1,0)
}


class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.wx = 10
        self.wy = 1
        self.dir = 0

    def move(self,m):
        op, amt = m

        if op == 'R':
            self.dir -= amt
            self.dir = self.dir % 360
            return

        if op == 'L':
            self.dir += amt
            self.dir = self.dir % 360
            return

        if op == 'F':
            heading = headings[self.dir]
        else:
            heading = compass[op]

        dx,dy = heading
        self.x += dx*amt
        self.y += dy*amt

    def waymove(self,m):
        op, amt = m

        if op == 'R':
            while amt > 0:
                oldy = self.wy
                self.wy = -self.wx
                self.wx = oldy
                amt -= 90
            return

        if op == 'L':
            while amt > 0:
                oldx = self.wx
                self.wx = -self.wy
                self.wy = oldx
                amt -= 90
            return

        if op == 'F':
            self.x += self.wx*amt
            self.y += self.wy*amt
            return

        heading = compass[op]
        dx,dy = heading
        self.wx += dx*amt
        self.wy += dy*amt
    
for part in [1,2]:
    s = Ship()
    for m in moves:
        if part == 1:
            s.move(m)
        else:
            s.waymove(m)
        if args.verbose > 1:
            op, amt = m
            print op,amt,(s.x,s.y),s.dir

    print 'Part %d: %d' % (part, abs(s.x) + abs(s.y))
