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

# sooo overcomplicated.
# just use an array next[1],....,next[100]
# then given n, it's easy to find n-1.

# too bad I didn't come up with that during the show

class Cup:
    def __init__(self,n):
        self.n = n
        self.next = None
        self.oneless = None
        self.removed = False

    def __str__(self):
        return str(self.n)

def state_str(start,fmt='%3d '):
    out = ''
    cur = start
    while True:
        assert((cur.n == 1) or (cur.oneless.n == cur.n - 1))
        out += fmt % cur.n
        cur = cur.next
        if cur == start:
            break
    return out

def dump(start):
    print state_str(start)

def build(tot_cups, start):
    first_cup = Cup(start[0])
    start_cups = {}

    max_cup = first_cup
    first_cup = None

    for c in start:
        cur = Cup(c)
        if cur.n > max_cup.n:
            max_cup = cur

        start_cups[c] = cur
        if first_cup == None:
            first_cup = cur
        else:
            old.next = cur
        old = cur

    for c in start_cups:
        if c != 1:
            start_cups[c].oneless = start_cups[c-1]

    first = True
    for i in range(len(start)+1,tot_cups+1):
        cur = Cup(i)
        if cur.n > max_cup.n:
            max_cup = cur

        old.next = cur
        if first:
            cur.oneless = start_cups[len(start)]
            first = False
        else:
            cur.oneless = old
        old = cur

    cur.next = first_cup

    start_cups[1].oneless = max_cup

    return first_cup, start_cups[1]

def move(cur):
    lift = cur.next
    lift.removed = True
    lift.next.removed = True
    lift.next.next.removed = True

    cur.next = cur.next.next.next.next

    dest = cur.oneless

    while dest.removed:
        dest = dest.oneless

    lift.next.next.next = dest.next
    dest.next = lift

    lift.removed = False
    lift.next.removed = False
    lift.next.next.removed = False

    return cur.next

def solve(cups,steps):
    for i in range(steps):
        if args.verbose > 0 and i > 0 and i % 100000 == 0:
            print '%d%%' % int(100*i/float(steps))
        if args.verbose > 1:
            print '-- move %d --' % (i+1)
            dump(cups)
        cups = move(cups)
    if args.verbose > 1:
        print '--final--'
        dump(cups)

# read input
inputstr = open(args.file).read().strip()
start = [int(x) for x in list(inputstr)]

# part 1
(cups,cup1) = build(len(start),start)
solve(cups,100)
s = state_str(cup1,fmt='%d')
print 'part 1:',s[1:]

# part 2
if args.verbose > 0:
    print 'building cups...'

(cups,cup1) = build(1000000,start)
solve(cups,10000000)
print 'part 2:', cup1.next.n * cup1.next.next.n

