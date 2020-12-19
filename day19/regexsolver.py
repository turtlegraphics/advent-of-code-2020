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

class Rule:
    def __init__(self, rule=None):
        self._regex = None

    @classmethod
    def create(cls, rule):
        """Rule factory method."""
        if '"' in rule:
            return Literal(rule)
        elif '|' in rule:
            return Alternation(rule)
        else:
            return RuleList(rule)

class Literal(Rule):
    def __init__(self,rule):
        self.val = rule.strip('" ')
        Rule.__init__(self)
    def __str__(self):
        return '"%s"' % self.val
    def regex(self):
        return self.val

class Alternation(Rule):
    def __init__(self,rule):
        self.subrules = [Rule.create(r) for r in rule.split('|')]
        Rule.__init__(self)
    def __str__(self):
        return ' | '.join([str(r) for r in self.subrules])
    def regex(self):
        if not self._regex:
            self._regex = '|'.join([r.regex() for r in self.subrules])
            self._regex = '(?:' + self._regex + ')'
        return self._regex

class RuleList(Rule):
    def __init__(self,rule):
        self.subrules = [int(n) for n in rule.split()]
        Rule.__init__(self)
    def __str__(self):
        return ' '.join([str(n) for n in self.subrules])
    def regex(self):
        if not self._regex:
            self._regex = ''.join([rules[n].regex() for n in self.subrules])
        return self._regex

class Rule8(Rule):
    def __str__(self):
        return 'SPECIAL 42 | 42 8'
    def regex(self):
        if self._regex:
            return self._regex
        self._regex = '(?:' + rules[42].regex() + ')+'
        return self._regex

class Rule11(Rule):
    def __str__(self):
        return 'SPECIAL 42 31 | 42 11 31'
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

# Handle input
args = aocutils.parse_args()
inputfile = open(args.file).read()
ruleslist, messageslist = inputfile.split('\n\n')

# Build a dictionary of rules
rules = {}
for line in ruleslist.split('\n'):
    num, rule = line.split(':')
    num = int(num)
    if num == 8 and args.part == 2:
        rules[num] = Rule8()
    elif num == 11 and args.part == 2:
        rules[num] = Rule11()
    else:
        rules[num] = Rule.create(rule)

if args.verbose > 1:
    # print rules, in order
    rnums = rules.keys()
    rnums.sort()
    for i in rnums:
        print i,':',rules[i]

# get the regular expression for rule 0
# (which kicks of a cascade of regex calculuation in all the rules)
zeroregex = '^' + rules[0].regex() + '$'

print 'rule 0 regular expression has',len(zeroregex),'characters:'
print zeroregex if len(zeroregex) < 70 else zeroregex[:70]+'...'

zeroregex = re.compile(zeroregex)

# validate the messages
messages = messageslist.strip().split('\n')
count = 0
for message in messages:
    valid = zeroregex.match(message)
    if valid:
        count += 1
        
    if args.verbose > 1:
        print message,'valid' if valid else 'invalid'

# report solution
print 'Part ' + str(args.part) + ':',count
