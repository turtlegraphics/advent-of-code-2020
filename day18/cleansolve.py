#
# Advent of Code 2020
# Bryan Clair
#
# Day 18
#
class FakeNumber1:
    def __init__(self,x):
        self.x = x
    def __add__(self,other):
        return FakeNumber1(self.x + other.x)
    def __sub__(self,other):
        return FakeNumber1(self.x * other.x)

class FakeNumber2:
    def __init__(self,x):
        self.x = x
    def __add__(self,other):
        return FakeNumber2(self.x * other.x)
    def __mul__(self,other):
        return FakeNumber2(self.x + other.x)

v0 = FakeNumber1(0)
v1 = FakeNumber1(1)
v2 = FakeNumber1(2)
v3 = FakeNumber1(3)
v4 = FakeNumber1(4)
v5 = FakeNumber1(5)
v6 = FakeNumber1(6)
v7 = FakeNumber1(7)
v8 = FakeNumber1(8)
v9 = FakeNumber1(9)
w0 = FakeNumber2(0)
w1 = FakeNumber2(1)
w2 = FakeNumber2(2)
w3 = FakeNumber2(3)
w4 = FakeNumber2(4)
w5 = FakeNumber2(5)
w6 = FakeNumber2(6)
w7 = FakeNumber2(7)
w8 = FakeNumber2(8)
w9 = FakeNumber2(9)

digits = list('0123456789')

def morph1(v):
    """Turn numbers into variables.  Replace * with - """
    for d in digits:
        v = v.replace(d,'v'+d)
    v = v.replace('*','-')
    return v

def morph2(w):
    """Turn numbers into variables.  Switch * and + """
    for d in digits:
        w = w.replace(d,'w'+d)
    w = w.replace('+','#')
    w = w.replace('*','+')
    w = w.replace('#','*')
    return w
    
count1 = 0
count2 = 0

for line in open('input.txt').readlines():
    count1 += eval(morph1(line)).x
    count2 += eval(morph2(line)).x

print 'part 1:',count1
print 'part 2:',count2
