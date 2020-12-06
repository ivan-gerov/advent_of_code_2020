
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import re


DATA_FILE = 'passport_data.txt'

with open(DATA_FILE) as f:
    passports = [line for line in f.read().split('\n\n')]

passports = [passport.replace('\n', ' ') for passport in passports]

def clean_passport(raw_passport):
    passport_fields = raw_passport.split(' ')
    fields: list = [tuple(field.split(':')) for field in passport_fields]
    fields: dict = {field[0]:field[1] for field in fields}
    return fields

passports = [clean_passport(passport) for passport in passports]

def validate_passport(passport):
    necessary_fields = ['ecl', 'pid', 'eyr', 'hcl', 
                        'byr', 'iyr', 'hgt']
    CID = 'cid'

    cid_present = False
    if all(field in passport.keys() for field in necessary_fields)\
        and CID in passport.keys():
        cid_present = True
    elif all(field in passport.keys() for field in necessary_fields):
        pass
    else:
        return False

    byr = bool(re.match(r'([1][9][2-9][0-9])|([2][0][0][0-2])', passport['byr']))
    iyr = bool(re.match(r'([2][0][1][0-9])|2020', passport['iyr']))
    eyr = bool(re.match(r'([2][0][2][0-9])|2030', passport['eyr']))

    in_validation = r'(([5-6][0-9])|([7][0-6]))in'
    cm_validation = r'(([1][5-8][0-9])|([1][9][0-3]))cm'
    hgt = bool(re.match(f'({in_validation})|({cm_validation})', passport['hgt']))

    hcl = bool(re.match(r'#[a-f0-9]{6}', passport['hcl']))
    ecl = bool(re.match(r'(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)', passport['ecl']))
    
    if bool(re.match(r'\d{9}', passport['pid']))\
        and len(passport['pid']) == 9:
        pid = True
    else:
        pid = False
    return all([byr, iyr, eyr, hgt, hcl, ecl, pid])

invalid_passports = [passport for passport in passports
                    if not validate_passport(passport)]

valid_passports = len(passports) - len(invalid_passports)

print(valid_passports)

