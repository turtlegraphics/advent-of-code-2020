#
# Advent of Code 2020
# Bryan Clair
#
# Day 25
#
import sys
import re
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

card_public = int(inputlines[0])
door_public = int(inputlines[1])

P = 20201227
v = 1
door_loop = 0
while v != door_public:
    v *= 7
    v = v % P
    door_loop += 1

assert(pow(7, door_loop, P) == door_public)

print 'part 1:',pow(card_public, door_loop, P)


