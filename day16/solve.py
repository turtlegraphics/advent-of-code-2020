#
# Advent of Code 2020
# Bryan Clair
#
# Day 16
#
import sys
import re
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

specre = re.compile(r"([ \w]+): (\d+)-(\d+) or (\d+)-(\d+)")

def islegal(val,f):
    return (val >= f[0] and val <= f[1]) or (val >= f[2] and val <= f[3])

myticket = None
nearby = []
fields = {}

for line in inputlines:
    field_desc = specre.match(line)
    if field_desc:
        field = field_desc.groups()[0]
        ranges = [int(r) for r in field_desc.groups()[1:]]
        fields[field] = ranges
    elif line[0:4] == 'your':
        myticketq = True
    elif line[0:6] == 'nearby':
        myticketq = False
    elif line:
        if myticketq:
            myticket = [int(v) for v in line.split(',')]
        else:
            nearby.append([int(v) for v in line.split(',')])

tickets = []
error_rate = 0
for ticket in nearby:
    valid_t = True
    for v in ticket:
        valid_v = False
        for f in fields:
            if islegal(v,fields[f]):
                valid_v = True
        if not valid_v:
            error_rate += v
            valid_t = False
    if valid_t:
        tickets.append(ticket)

print 'Part 1:',error_rate

N = len(myticket)
assert(N == len(fields))

possible = {}
for f in fields:
    possible[f] = []
    for col in range(N):
        ok = True
        for t in tickets:
            if not islegal(t[col],fields[f]):
                ok = False
        if ok:
            possible[f].append(col)

actual = {}

while len(possible) > 0:
    for f in possible:
        if len(possible[f]) == 1:
            a = possible[f][0]
            actual[f] = a
            break
    del possible[f]

    for f in possible:
        possible[f].remove(a)

if args.verbose > 2:
    print actual

check = 1
for f in actual:
    if f[0:9] == 'departure':
        check *= myticket[actual[f]]
print 'Part 2:',check

if args.verbose > 1:
    print 'My Ticket'
    for f in actual:
        print ' '+f+':',myticket[actual[f]]
