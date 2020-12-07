#
# Advent of Code 2020
# Bryan Clair
#
# Utilities
#
from argparse import ArgumentParser
from math import sqrt

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-v", "--verbose",
                        action = "count",
                        dest = "verbose",
                        default = 1,
                        help = "Set verbosity level (-v, -vv, -vvv,...)")
    parser.add_argument("-q", "--quiet",
                        action = "store_const",
                        const = 0,
                        dest = "verbose",
                        help = "Suppress output.")
    
    parser.add_argument("-p", "--part",
                        action="store",
                        dest = "part",
                        default = 1,
                        type = int,
                        help = "Which part of the problem to solve (1 or 2)")
    
    parser.add_argument("file",
                        nargs = "?",
                        default = "input.txt",
                        help = "Problem input file (optional).")
    args = parser.parse_args()
    if args.verbose > 2:
        print(args)

    return args

class Point:
    """
    A 2d point class
    """
    def __init__(self, x=0, y=0):
        self.x, self.y = x,y

    def __iter__(self):
        yield self.x
        yield self.y

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def dist(self, other):
        """Euclidean distance."""
        return abs(self - other)

    def __add__(self,other):
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self,other):
        self.x += other.x
        self.y += other.y

    def __sub__(self,other):
        return Point(self.x - other.x, self.y - other.y)

    def __isub__(self,other):
        self.x -= other.x
        self.y -= other.y

    def __str__(self):
        return '(%s,%s)' % (str(self.x),str(self.y))

class Grid:
    """
    A 2d grid of tile objects (probably characters) that can be any size.
    Coordinates are tuples (x,y) or Points.
    Keeps track of its own dimensions and displays the smallest rectangle that
    contains all data.
    """
    def __init__(self):
        self.raster = {}

    def __setitem__(self,p,tile):
        x,y = p

        if self.raster:
            self.xmin = min(self.xmin,x)
            self.xmax = max(self.xmax,x)
            self.ymin = min(self.ymin,y)
            self.ymax = max(self.ymax,y)
        else:
            self.xmin = x
            self.xmax = x
            self.ymin = y
            self.ymax = y

        self.raster[(x,y)] = tile

    def __getitem__(self,p):
        (x,y) = p
        return self.raster[(x,y)]

    def display(self):
        for y in range(self.ymax,self.ymin-1,-1):
            out = ''
            for x in range(self.xmin,self.xmax + 1):
                if (x,y) in self.raster:
                    out += str(self.raster[(x,y)])
                else:
                    out += ' '
            print(out)

class HexGrid(Grid):
    """
    Class representing a hexagonal grid.
    See HexPoint class for details of coordinates
    """
    def display(self):
        for y in range(self.ymax,self.ymin-1,-1):
            out = ' '*(y-self.ymin)
            for x in range(self.xmin,self.xmax + 1):
                if (x,y) in self.raster:
                    out += str(self.raster[(x,y)])
                else:
                    out += ' '
                out += ' '
            print(out)

class HexPoint(Point):
    """
    Class for working with coordinates on a hexagonal grid.
    Coordinates are mappped to (x,y) with connections made in this way:
      NW  NE
     W  *   E
      SW  SE
    """
    DIRECTIONS = {
        'ne' : (0,1),
        'sw' : (0,-1),
        'nw' : (-1,1),
        'se' : (1,-1),
        'w' : (-1,0),
        'e' : (1,0)
        }
        
    def __abs__(self):
        """Returns distance to the origin on the hex grid"""
        x,y = self.x,self.y
        diag = 0
        if (x > 0 and y < 0):
            diag = -min(abs(x),abs(y))
        if (x < 0 and y > 0):
            diag = min(abs(x),abs(y))
        return abs(diag) + abs(x + diag) + abs(y - diag)

    def move(self,dir):
        dx,dy = self.DIRECTIONS[dir.lower()]
        self.x += dx
        self.y += dy

    def __str__(self):
        return '(%d,%d)' % (self.x,self.y)

if __name__ == '__main__':
    print(parse_args())

    # Point
    print '-'*20
    print "Point class"
    print '-'*20
    p = Point(1,2)
    q = Point(3,3)
    print 'p=%s,q=%s' % (str(p),str(q))
    print p.dist(q),'apart'
    print 'p + q = ',p+q
    print

    # Grid
    print '-'*20
    print "Grid class"
    print '-'*20
    g = Grid()
    g[Point(0,-1)] = 'U'
    g[Point(-1,0)] = 'o'
    g[Point(1,0)] = 'o'
    for p in [(-1,2),(0,2),(1,2),(-2,1),(-2,0),(-2,-1),
              (2,1),(2,0),(2,-1),(-1,-2),(0,-2),(1,-2)]:
        g[p] = '.'
    assert(g[(0,-1)] == 'U')
    g.display()
    print

    # HexGrid, HexPoint
    print '-'*20
    print "HexGrid, HexPoint"
    print '-'*20
    print 'Distances from origin:'
    h = HexGrid()
    for x in range(-3,4):
        for y in range(-3,4):
            p = HexPoint(x,y)
            h[p] = str(abs(p))

    h.display()

    h = HexGrid()
    for x in range(-5,4):
        for y in range(-2,6):
            h[(x,y)] = '.'

    print
    print 'Take a stroll'
    p = HexPoint()
    i = 0
    h[p] = '0'
    for d in ['e','ne','ne','nw','w','w','w','sw','se']:
        print '%s --%s-->' % (str(p),d),
        p.move(d)
        i += 1
        h[p] = str(i)
    print p

    h.display()

    print 'Ended',abs(p),'from start'
