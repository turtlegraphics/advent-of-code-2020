#
# passport class
#

import re

#
# input validators
#
# All accept a string, and return parsed validated input or None
#

def intrange_v(x, vmin, vmax):
    """Validate that x is an integer with vmin <= x <= vmax."""
    try:
        y = int(x)
    except:
        return None
    if y >= vmin and y <= vmax:
        return y
    return None

def regex_v(x, pattern):
    """Validate that x matches the regex pattern."""
    if re.match(pattern,x):
        return x
    else:
        return None

def hgt_v(x):
    """ Validate height and convert to cm."""
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

validators = {
"byr": lambda x : intrange_v(x,1920,2002),
"iyr": lambda x : intrange_v(x,2010,2020),
"eyr": lambda x : intrange_v(x,2020,2030),
"hgt": hgt_v,
"hcl": lambda x : regex_v(x, '^#[0-9a-f]{6}$'),
"ecl": lambda x : regex_v(x, '^amb|blu|brn|gry|grn|hzl|oth$'),
"pid": lambda x : regex_v(x, '^[0-9]{9}$'),
"cid": lambda x : x
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
