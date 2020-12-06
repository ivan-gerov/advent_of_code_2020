
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from collections import Counter

with open('sample_data.txt') as f:
    groups = [group for group in f.read().split('\n\n')]

def part1(groups):
    groups = [group.replace('\n', '') for group in groups]
    no_yes_per_group = [len(set(group)) for group in groups]
    return sum(no_yes_per_group)
    
def get_matching_answers_1(group):
    people = [''.join(list(set(person))) for person in group.split('\n')]
    if len(people) > 1:
        counter = Counter(''.join(people))
        dupes = [k for k, v in counter.items()
                if v > 1]
        dupes = ''.join(sorted(dupes))
        if len(dupes) < 1:
            dupes = ''
        return dupes
    else:
        answers = ''.join(sorted([ans for ans in people[0]]))
        return answers

# print(part2(groups))

# print(sum([len(set.intersection(*[set(t) for t in i.split("\n")])) for i in file.read().split("\n\n")]))

# for group in groups:
#     for p in group.split('\n'):
#         print(set.intersection(*[set(p)]))

def get_matching_answers_2(group):
    people = [set(person) for person in group.split('\n')]
    matching_answers: set = set.intersection(*people)
    matching_answers = ''.join(sorted(list(matching_answers)))
    return matching_answers

matching_1 = [get_matching_answers_1(group) for group in groups]
matching_2 = [get_matching_answers_2(group) for group in groups]

print(set.intersection(
    set(matching_1),
    set(matching_2)
))

