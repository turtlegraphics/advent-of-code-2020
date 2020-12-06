#
# Advent of Code 2020
# Bryan Clair
#
# Day 06
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

data = open(args.file).read()

groups = data.split('\n\n')

groups = [x.split() for x in groups]

count = 0
for g in groups:
    sets = [set(list(x)) for x in g]
    univ = set(list('abcdefghijklmnopqrstuvwxyz'))
    for s in sets:
        univ = univ.intersection(s)
    count += len(univ)
    
print count


