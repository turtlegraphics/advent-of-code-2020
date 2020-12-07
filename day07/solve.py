#
# Advent of Code 2020
# Bryan Clair
#
# Day 07
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

def axe(x):
    n,d = x.split(' ',1)
    return (int(n),d)

def bagoff(x):
    x = x.strip()
    loc = x.rfind('bag')
    x = x[:loc]
    return x.strip()

rules = {}
for line in inputlines:
    outer, inner = line.split(' contain')
    outer = bagoff(outer)
    inner = inner.strip('.')
    inner = [bagoff(x) for x in inner.split(', ')]
    if inner[0] == 'no other':
        inner = []
    inner = [axe(x) for x in inner]

    rules[outer] = inner

def has_gold(bag):
    if bag == 'shiny gold':
        return True
    myrules = rules[bag]
    for r in myrules:
        n,d = r
        if has_gold(d):
            return True
    return False

def contains(bag):
    count = 1
    myrules = rules[bag]
    for r in myrules:
        n,d = r
        count += contains(d)*n
    return count

print 'part 1'
count = 0
for d in rules.keys():
    count += 1 if has_gold(d) else 0
print count-1

print 'part 2'
print contains('shiny gold')-1
