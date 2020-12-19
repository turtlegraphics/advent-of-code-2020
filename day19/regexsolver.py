#
# Advent of Code 2020
# Bryan Clair
#
# Day 19
#
import sys
import re
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputfile = open(args.file).read()

ruleslist, messageslist = inputfile.split('\n\n')

LIT = 0
LST = 1
ALT = 2

class Rule:
    def __init__(self, rule):
        self._regex = None
        if '"' in rule:
            self.type = LIT
            self.val = rule.strip('" ')
        elif '|' in rule:
            self.type = ALT
            one,two = rule.split('|')
            self.subrules = [Rule(one),Rule(two)]
        else:
            self.type = LST
            self.subrules = [int(n) for n in rule.split()]

    def __str__(self):
        out = ''
        if self.type == LIT:
            out += '"%s"' % self.val
        elif self.type == ALT:
            for r in self.subrules:
                out += str(r) + ' | '
            out = out[:-3]
        else:
            for n in self.subrules:
                out += str(n) + ' '
            out = out[:-1]
        return out

    def regex(self):
        """Return a regex for this rule to match"""
        if self._regex:
            return self._regex

        if self.type == LIT:
            self._regex = self.val
        elif self.type == LST:
            self._regex = ''.join([rules[n].regex() for n in self.subrules])
        else:
            assert(self.type == ALT)
            self._regex = '|'.join([r.regex() for r in self.subrules])
            self._regex = '(?:' + self._regex + ')'
        return self._regex

class Rule8(Rule):
    def __init__(self):
        self.name = 'SPECIAL 42 | 42 8'
        self._regex = None
    def __str__(self):
        return self.name
    def regex(self):
        if self._regex:
            return self._regex
        self._regex = '(?:' + rules[42].regex() + ')+'
        return self._regex

class Rule11(Rule):
    def __init__(self):
        self.name = 'SPECIAL 42 31 | 42 11 31'
        self._regex = None
    def __str__(self):
        return self.name
    def regex(self):
        if self._regex:
            return self._regex
        rule42 = rules[42].regex()
        rule31 = rules[31].regex()
        myrules = []
        depth = 4  # how deep does the recursion need to go?
        while depth > 0:
            myrules.append(rule42*depth + rule31*depth)
            depth -= 1
        self._regex = '(?:' + '|'.join(myrules) + ')'
        return self._regex

rules = {}

for line in ruleslist.split('\n'):
    num, rule = line.split(':')
    num = int(num)
    if num == 8 and args.part == 2:
        rules[num] = Rule8()
    elif num == 11 and args.part == 2:
        rules[num] = Rule11()
    else:
        rules[num] = Rule(rule.strip())

if args.verbose > 1:
    # print rules, in order
    rnums = rules.keys()
    rnums.sort()
    for i in rnums:
        print i,':',rules[i]

matches = {}
valid = 0

zeroregex = '^' + rules[0].regex() + '$'
print 'rule 0 regular expression has',len(zeroregex),'characters:'
if len(zeroregex) < 70:
    print zeroregex
else:
    print zeroregex[:70]+'...'

messages = messageslist.strip().split('\n')
print 'validating',len(messages),'messages'
n = 0
for message in messages:
    n += 1
    if args.verbose > 1:
        print n,message,
    zr = re.compile(zeroregex)
    if zr.match(message):
        if args.verbose > 1:
            print 'matches rule 0'
        valid += 1
    else:
        if args.verbose > 1:
            print 'no match.'

#for k in sorted(matches.keys(),key=len):
#    print k,matches[k]
print 'Part ' + str(args.part) + ':',valid
