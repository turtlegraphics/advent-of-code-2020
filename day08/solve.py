#
# Advent of Code 2020
# Bryan Clair
#
# Day 08
# Classy version
#
import sys
sys.path.append("..")
import aocutils
from machine import Machine

args = aocutils.parse_args()

program = [x.strip() for x in open(args.file).readlines()]

m = Machine(program)
m.run()
print 'part 1:',m.acc

for line in range(len(program)):
    old = program[line]
    op = old[:3]
    if op == 'nop':
        program[line] = 'jmp' + old[3:]
    elif op == 'jmp':
        program[line] = 'nop' + old[3:]
    m = Machine(program)
    try:
        m.run()
    except IndexError:
        if m.ip == len(program):
            print 'part 2:',m.acc
    program[line] = old

