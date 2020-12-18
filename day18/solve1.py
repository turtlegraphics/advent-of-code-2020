#
# Advent of Code 2020
# Bryan Clair
#
# Day 18
#
import sys
import re
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

digits = list('0123456789')

def Eval(expr):
    """Evaluate an expression. Return (value, eaten)"""
    if args.verbose > 1:
        print 'evaluating',expr
    op = None
    c = 0
    acc = None
    while True:
        # get value
        if expr[c] == '(':
            c += 1
            value,eaten = Eval(expr[c:])
            if args.verbose > 2:
                print 'got back',value,eaten
            c += eaten
            assert(expr[c] == ')')
            c += 1
        else:
            assert(expr[c] in digits)
            value = int(expr[c])
            c += 1

        # calculate
        if op == '*':
            acc *= value
        elif op == '+':
            acc += value
        else:
            acc = value

        # get op, if there is one
        if c == len(expr):
            return (acc,c)
        if expr[c] == ')':
            return (acc,c)
        assert(expr[c] == ' ')
        c += 1
        op = expr[c]
        c += 1
        assert(expr[c] == ' ')
        c += 1

count = 0        
for line in inputlines:
    if args.verbose > 1:
        print line,

    val,eaten = Eval(line)
    count += val

    if args.verbose > 1:
        print '=',Eval(line)[0]

print 'part 1:',count
