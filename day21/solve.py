#
# Advent of Code 2020
# Bryan Clair
#
# Day 21
#
import sys
import re
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

parser = re.compile(r"([ \w]+) \(contains ([ ,\w]+)\)") # or whatever

badfood = {}
allfood = set()

for line in inputlines:
    food_str,allergy_str = parser.match(line).groups()
    foods = set(food_str.split())
    allfood = allfood.union(foods)
    allergies = [x.strip() for x in allergy_str.split(',')]
    for a in allergies:
        if a not in badfood:
            badfood[a] = foods
        else:
            badfood[a] = badfood[a].intersection(foods)

safefood = set()
for f in allfood:
    good = True
    for a in badfood:
        if f in badfood[a]:
            good = False
            break
    if good:
        safefood.add(f)


count = 0
for line in inputlines:
    food_str,allergy_str = parser.match(line).groups()
    foods = set(food_str.split())
    for f in foods:
        if f in safefood:
            count += 1

print 'part 1:',count

for a in badfood:
    badfood[a] = badfood[a].difference(safefood)
    # print then solve this crap by hand.  Done!
    if args.verbose > 2:
        print a,badfood[a]

# ok ok here's code to do it, written post-competition:

found = {}
while len(found) < len(badfood):
    for a in badfood:
        badfood[a] = badfood[a].difference(found.values())
        if len(badfood[a]) == 1:
            found[a] = list(badfood[a])[0]

if args.verbose > 1:
    for a in found:
        print found[a],'contains',a

print 'part 2:',
print ','.join([found[a] for a in sorted(found.keys())])
