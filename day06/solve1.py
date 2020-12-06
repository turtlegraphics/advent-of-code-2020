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

combined = [''.join(x.split()) for x in groups]

sets = [set(list(x)) for x in combined]

counts = [len(x) for x in sets]

print sum(counts)


