#
# Advent of Code 2020
# Bryan Clair
#
# Day 08
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

acc = 0
cur = 0

code = []
runsofar = []
for line in inputlines:
    op,val = line.split()
    code.append((op,int(val)))
    runsofar.append(False)

print code

while not runsofar[cur]:
    runsofar[cur] = True
    op,val = code[cur]
    if op == 'nop':
        cur += 1
        continue
    if op == 'acc':
        acc += val
        cur += 1
        continue
    if op == 'jmp':
        cur += val
        continue
    print 'bad op:',op,'at line',cur

print acc
