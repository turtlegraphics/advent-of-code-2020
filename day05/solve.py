#
# Advent of Code 2020
# Bryan Clair
#
# Day 05
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

seats = []
for line in inputlines:
    rowst = line[:7]
    colst = line[7:]
    rowb = rowst.replace('F','0').replace('B','1')
    colb = colst.replace('L','0').replace('R','1')

    row = int(rowb,2)
    col = int(colb,2)

    seatid = row*8 + col
    seats.append(seatid)

seats.sort()
print 'highest ID:',seats[-1]

last = False
for i in range(len(seats)):
    if last and seats[i] != last+1:
        print 'my seat:',seats[i]-1
    last = seats[i]
