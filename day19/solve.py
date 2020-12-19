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
            assert(len(self.subrules) <= 2)

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

    def match(self, message):
        if self.type == LIT:
            return(message == self.val)

        if self.type == ALT:
            for r in self.subrules:
                if r.match(message):
                    return True
            return False

        assert(self.type == LST)
        if len(self.subrules) == 1:
            return rules[self.subrules[0]].match(message)

        assert(len(self.subrules) == 2)
        r1,r2 = self.subrules
        for cut in range(1,len(message)):
            m1 = message[:cut]
            m2 = message[cut:]
            try:
                found = (r1 in matches[m1]) and (r2 in matches[m2])
            except IndexError:
                found = False
            if found:
                return True
        return False

class Rule8(Rule):
    def __init__(self):
        self.name = 'SPECIAL 42 | 42 8'
    def __str__(self):
        return self.name
    def match(self,message):
        if message in matches and 8 in matches[message]:
            return True
        if rules[42].match(message):
            return True
        for cut in range(1,len(message)):
            m1 = message[:cut]
            m2 = message[cut:]
            if rules[42].match(m1) and self.match(m2):
                return True
        return False

class Rule11(Rule):
    def __init__(self):
        self.name = 'SPECIAL 42 31 | 42 11 31'
    def __str__(self):
        return self.name
    def match(self,message):
        if message in matches and 11 in matches[message]:
            return True
        for cut1 in range(1,len(message)):
            # find prefix
            m1 = message[:cut1]
            m2 = message[cut1:]
            if rules[42].match(m1):
                # prefix found
                if rules[31].match(m2):
                    return True
                for cut2 in range(1,len(m2)):
                    # find suffix
                    n1 = m2[:cut2]
                    n2 = m2[cut2:]
                    if rules[31].match(n2):
                        # found suffix
                        if self.match(n1):
                            return True
        return False

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

rnums = rules.keys()
rnums.sort()
for i in rnums:
    print i,':',rules[i]

matches = {}
valid = 0

messages = messageslist.strip().split('\n')
print 'validating',len(messages),'messages'
n = 0
for message in messages:
    n += 1
    print n,message,
    for sublen in range(1,len(message)+1):
        for start in range(len(message) + 1 - sublen):
            submsg = message[start:start+sublen]
            # print '  ',submsg,
            if submsg not in matches:
                matches[submsg] = []
                for i in rules:
                    if rules[i].match(submsg):
                        matches[submsg].append(i)
            # print matches[submsg]
    if 0 in matches[message]:
        print 'matches rule 0'
        valid += 1
    else:
        print 'no match.'

#for k in sorted(matches.keys(),key=len):
#    print k,matches[k]
print valid
