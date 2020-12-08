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

code = []
for line in inputlines:
    op,val = line.split()
    code.append((op,int(val)))

def tryrun():
    run = [False]*len(code)
    acc = 0
    cur = 0
    while True:
        try:
            if run[cur]:
                return (acc,cur)
        except IndexError:
            return (acc,cur)
        run[cur] = True
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
        sys.exit()
    return (acc,cur)

(acc,cur) = tryrun()
print 'part 1:',acc

for line in range(len(code)):
    op,val = code[line]
    if op == 'nop':
        code[line] = ('jmp',val)
    elif op == 'jmp':
        code[line] = ('nop',val)
    (acc,cur) = tryrun()
    if cur == len(code):
        print 'part 2:',acc
    code[line] = (op,val)
