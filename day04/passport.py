#
# passport class
#

#
# input validators
#
# All accept a string, and return parsed validated input or None
#
def byr_v(x):
    try:
        y = int(x)
    except:
        return None
    if y >= 1920 and y <= 2002:
        return y
    return None

def iyr_v(x):
    try:
        y = int(x)
    except:
        return None
    if y >= 2010 and y <= 2020:
        return y
    return None

def eyr_v(x):
    try:
        y = int(x)
    except:
        return None
    if y >= 2020 and y <= 2030:
        return y
    return None

def hgt_v(x):
    """ Validate height and return height in cm"""
    try:
        unit = x[-2:]
        val = int(x[:-2])
    except:
        return None
    if unit == 'cm' and val >= 150 and val <= 193:
        return val
    if unit == 'in' and val >= 59 and val <= 76:
        return val*2.54
    return None

hexdigits = list('01234567890abcdef')
def hcl_v(x):
    try:
        if x[0] != '#':
            return None
        for i in [1,2,3,4,5,6]:
            if x[i] not in hexdigits:
                return None
    except:
        return None
    return x

eyecolors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
def ecl_v(x):
    if (x in eyecolors):
        return x
    return None

digits = list('01234567890')
def pid_v(x):
    if len(x) != 9:
        return None
    try:
        for i in range(9):
            if x[i] not in digits:
                return None
    except:
        return None
    return x

def cid_v(x):
    return x

validators = {
"byr": byr_v,
"iyr": iyr_v,
"eyr": eyr_v,
"hgt": hgt_v,
"hcl": hcl_v,
"ecl": ecl_v,
"pid": pid_v,
"cid": cid_v
}

class Passport:
    def __init__(self, fields):
        """
        Create a passport from a dictionary of fields.
        In the fields dictionary, all fields are strings, may not be valid.
        """
        for f,v in fields.items():
            try:
                setattr(self, f, validators[f](v))
            except KeyError:
                raise KeyError('Bad passport field: '+ f)
        if 'cid' not in fields:
            self.cid = 'NORTH POLE'

    def valid(self):
        for f in validators:
            try:
                v = getattr(self, f)
            except AttributeError:
                # missing field
                return False
            if v == None:
                # invalid field
                return False
        return True

    def __str__(self):
        out = '--------\nPassport\n--------\n'
        for k,v in vars(self).items():
            out += k + ':' + str(v)+ '\n'
        out += '---------\n'
        out += 'VALID' if self.valid() else 'INVALID'
        out += '\n---------'
        return out

if __name__ == '__main__':

    p_test_data = [
        [{'cid': '147', 'byr': '1937', 'hgt': '183cm',
         'ecl': 'gry', 'pid': '860033327', 'eyr': '2020',
         'iyr': '2017', 'hcl': '#fffffd'},True],
        [{'cid': '350', 'byr': '1929', 'ecl': 'amb',
         'pid': '028048884', 'eyr': '2023', 'iyr': '2013',
         'hcl': '#cfa07d'},False],
        [{'pid': '760753108', 'hgt': '179cm', 'ecl': 'brn',
         'byr': '1931', 'eyr': '2024', 'iyr': '2013', 'hcl': '#ae17e1'},True],
        [{'pid': '76753108', 'hgt': '100cm', 'ecl': 'bds',
         'byr': '1931', 'eyr': '2024', 'iyr': '2013', 'hcl': '#ae17e1'},False]
        ]

    for data,valid in p_test_data:
        p = Passport(data)
        print p
        print '(country',p.cid,')'
        print

        assert(p.valid() == valid)
