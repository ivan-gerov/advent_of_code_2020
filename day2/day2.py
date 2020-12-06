
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from collections import namedtuple
import re

if 'day2' not in os.getcwd():
    os.chdir('./day2')


class Password:
    
    def __init__(self, char, range_, pass_string):
        self.char = char
        self.range_ = range_
        self.pass_string = pass_string

    @classmethod
    def clean_raw_pass(cls, raw_pass):
        raw_pass: list = raw_pass.replace(':', '').strip('\n').split(' ')
        raw_pass[0] = [int(i) for i in raw_pass[0].split('-')]
        cleaned_pass = Password(char=raw_pass[1], 
                                range_=raw_pass[0], 
                                pass_string=raw_pass[2])
        return cleaned_pass

    def is_valid(self, validation_policy):
        policies = {
            1: Password.validation_policy1,
            2: Password.validation_policy2
        }
        return policies[validation_policy](self)

    @staticmethod
    def validation_policy1(pass_object):
        return True

    @staticmethod
    def validation_policy2(pass_obj):
        if pass_obj.pass_string.count(pass_obj.char) < 1:
            return False

        all_positions = [m.start()+1 
                    for m in re.finditer(pass_obj.char, pass_obj.pass_string)]
        
        if any(elem in all_positions for elem in pass_obj.range_)\
            and not(all(elem in all_positions for elem in pass_obj.range_)):
            return True
        else:
            return False

    def __repr__(self):
        return f'{self.char} : {self.range_} : {self.pass_string}'


all_passwords = []

with open('data.txt') as f:
    all_passwords.extend([line for line in f])

all_passwords = [Password.clean_raw_pass(raw_pass)
                 for raw_pass in all_passwords]

result = 0
for p in all_passwords:
    if p.is_valid(validation_policy=2):
        result += 1

print(result)


