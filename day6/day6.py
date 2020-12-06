
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

DATA_FILE = 'data.txt'

with open(DATA_FILE) as f:
    groups = [group for group in f.read().split('\n\n')]

def part1(groups):
    groups = [group.replace('\n', '') for group in groups]
    no_yes_per_group = [len(set(group)) for group in groups]
    return sum(no_yes_per_group)
    
def get_matching_asnwers(group):
    people = [set(person) for person in group.split('\n')]
    matching_answers = set.intersection(*people)
    return len(matching_answers)

all_matching_answers = [get_matching_asnwers(group) for group in groups]
print(sum(all_matching_answers))