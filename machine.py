#
# Advent of Code 2020
# Bryan Clair
#
# Machine
#

class Machine:
    def __init__(self, program):
        self.code = self.parse(program)
        self.reset()

    def reset(self):
        self.acc = 0
        self.ip = 0
        self.run_already = [0]*len(self.code)
        
    def parse(self,program):
        """Pass program as a list of lines."""
        code = []
        for line in program:
            op,val = line.split()
            code.append((op,int(val)))
        return code

    def run(self, debug=False):
        """Run until a repeat occurs"""
        while self.run_already[self.ip] == 0:
            self.run_already[self.ip] += 1
            op,val = self.code[self.ip]
            if debug:
                sgn = '+' if val > 0 else ''
                print "[%4d]:%s %s%d (acc=%d)" %\
                    (self.ip, op, sgn, val, self.acc)
            if op == 'nop':
                self.ip += 1
                continue
            if op == 'acc':
                self.acc += val
                self.ip += 1
                continue
            if op == 'jmp':
                self.ip += val
                continue
            raise('bad op:'+str(op)+'at line'+str(self.ip))

if __name__=="__main__":
    prog =\
"""acc +13
acc -6
acc -8
jmp +3
acc +44
acc +21
nop +23
acc +5
jmp -3
acc +9
acc +19
nop +513"""
    m = Machine(prog.split('\n'))
    m.run(debug = True)
    assert(m.acc == 25)
