# Advent of Code 2015, Day-19
# https://adventofcode.com/2015
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import re
from itertools import combinations

p = r'(\w*) => (\w*)'
atom_pattern = r'([A-Z0-9][a-z]?)'


def build_data_structure(in_line):
    molec = in_line[-1].strip()
    subs = {}
    for i in in_line:
        i.strip().lstrip()
        m = re.search(p, i)
        if m:
            key = m[1]
            value = m[2]
            if key not in subs:  # make new entry if not existed
                subs[key] = []
            subs[key].append(value)

    return subs, molec


def unbuild_molecule(molec, subs_dict, keys):
    count = 0
    old_molec = ''

    while old_molec != molec:
        old_molec = molec
        for key in keys:
            while key in molec:
                count += molec.count(key)
                molec = molec.replace(key, subs_dict[key])
    return int(molec == 'e') * count  # number of steps if we down to 1 'e' left, otherwise 0 for unsuccessful run


def part_1(subs, molec):
    new_molec = set()  # number of new molecules formed

    for key in subs.keys():  # each substitutable atom
        replacements = subs[key]
        i = molec.find(key, 0)  # find the next substitution candidate, starting at beginning
        while i != -1:  # until not found
            for replace_with in replacements:  # replace with these
                new_one = molec[0:i] + replace_with + molec[i + len(key):]
                new_molec.add(new_one)
            i = molec.find(key, i + 1)  # find the next candidate for substitution

    return len(new_molec)


def part_2(subs, molec):
    reverse_sub = {}  # build  reverse look up dictionary for reverse substitution
    for key in subs:
        for val in subs[key]:
            reverse_sub[val] = key
    un_build = reverse_sub.keys()
    for i in range(len(un_build), 1, -1):
        perm = combinations(un_build, i)
        for keys in list(perm):
            step_counts = unbuild_molecule(molec, reverse_sub, list(keys))
            if step_counts != 0:
                return step_counts


if __name__ == '__main__':
    with open('Day-19-data.txt', 'r') as f:
        input_data = f.readlines()
    # substitution_dictionary format:
    # {'from' : ['to', 'to', etc...]}
    # molecule is a str
    substitution_dictionary, molecule = build_data_structure(input_data)

    new_molecule = part_1(substitution_dictionary, molecule)
    print(f'Day 19, Part 1--{new_molecule} distinct molecules created.')

    steps = part_2(substitution_dictionary, molecule)
    print(f'Day 19, Part 2--{steps} to build the molecule requested.')
