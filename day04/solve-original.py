#
# Advent of Code 2020
# Bryan Clair
#
# Day 04
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

def byr_v(x):
    try:
        y = int(x)
    except:
        return False
    return y >= 1920 and y <= 2002

def iyr_v(x):
    try:
        y = int(x)
    except:
        return False
    return y >= 2010 and y <= 2020

def eyr_v(x):
    try:
        y = int(x)
    except:
        return False
    return y >= 2020 and y <= 2030

def hgt_v(x):
    try:
        unit = x[-2:]
        val = int(x[:-2])
    except:
        return False
    if unit == 'cm' and val >= 150 and val <= 193:
        return True
    if unit == 'in' and val >= 59 and val <= 76:
        return True
    return False

hexdigits = list('01234567890abcdef')
def hcl_v(x):
    try:
        if x[0] != '#':
            return False
        for i in [1,2,3,4,5,6]:
            if x[i] not in hexdigits:
                return False
    except:
        return False
    return True

eyecolors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
def ecl_v(x):
    return (x in eyecolors)

digits = list('01234567890')
def pid_v(x):
    if len(x) != 9:
        return False
    try:
        for i in range(9):
            if x[i] not in digits:
                return False
    except:
        return False
    return True

def cid_v(x):
    return True

validators = {
"byr": byr_v,
"iyr": iyr_v,
"eyr": eyr_v,
"hgt": hgt_v,
"hcl": hcl_v,
"ecl": ecl_v,
"pid": pid_v
}

def validate(p):
    for field in validators:
        if field not in p:
            return False
        if not validators[field](p[field]):
            return False
    return True

allports = []
passport = {}
count = 0
for line in inputlines:
    if line:
        lf = line.split()
        for x in lf:
            id,val = x.split(':')
            passport[id] = val
    else:
        print validate(passport)
        if validate(passport):
            count += 1
        passport = {}

print count
