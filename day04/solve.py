#
# Advent of Code 2020
# Bryan Clair
#
# Day 04
#
import sys
sys.path.append("..")
import aocutils
import re

from passport import Passport

args = aocutils.parse_args()

input = open(args.file).read()

# cut input into passport definitions,
# separated by blank lines
passtxt = re.split('\n\n+',input)

count = 0
for line in passtxt:
    lf = line.split()
    fields = {}
    for x in lf:
        id,val = x.split(':')
        fields[id] = val
    p = Passport(fields)
    if p.valid():
        count += 1
    if args.verbose:
        print p

print
print 'Valid passports: ', count
