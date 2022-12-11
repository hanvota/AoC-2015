# Advent of Code 2015, Day-16
# https://adventofcode.com/2015
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import re


def part_2(in_line):
    match_count = 0
    # children: 3
    m = re.findall(r'children: ([\d*])', in_line)
    if m and int(m[0]) == 3:
        match_count += 1

    # cats: > 7
    m = re.findall(r'cats: ([\d*])', in_line)
    # if m:
    #     print(int(m[0]),in_line)
    if m and int(m[0]) > 7:
        match_count += 1

    # samoyeds: 2
    m = re.findall(r'samoyeds: ([\d*])', in_line)
    if m and int(m[0]) == 2:
        match_count += 1

    # pomeranians:  < 3
    m = re.findall(r'pomeranians: ([\d*])', in_line)
    # if m:
    #     print(int(m[0]),in_line)
    if m and int(m[0]) < 3:
        match_count += 1

    # akitas: 0
    m = re.findall(r'akitas: ([\d*])', in_line)
    if m and int(m[0]) == 0:
        match_count += 1

    # vizslas: 0
    m = re.findall(r'vizslas: ([\d*])', in_line)
    if m and int(m[0]) == 0:
        match_count += 1

    # goldfish: < 5
    m = re.findall(r'goldfish: ([\d*])', in_line)
    # if m:
    #     print(int(m[0]),in_line)
    if m and int(m[0]) < 5:
        match_count += 1

    # trees: > 3
    m = re.findall(r'trees: ([\d*])', in_line)
    # if m:
    #     print(int(m[0]),in_line)
    if m and int(m[0]) > 3:
        match_count += 1

    # cars: 2
    m = re.findall(r'cars: ([\d*])', in_line)
    if m and int(m[0]) == 2:
        match_count += 1

    # perfumes: 1
    m = re.findall(r'perfumes: ([\d*])', in_line)
    if m and int(m[0]) == 1:
        match_count += 1

    return match_count


if __name__ == '__main__':

    s1 = r'children: [^3]|cats: [^7]|samyoeds: [^2]|pomeranians: [^3]|akitas: [^0]|vizslas: [^0]|goldfish: [^5]|trees: [^3]|cars: [^2]|perfumes: [^1]'
    p1 = re.compile(s1)
    with open('Day-16-data.txt', 'r') as f:
        input_data = f.readlines()

    for input_line in input_data:
        input_line = input_line.strip().lstrip()
        match = p1.search(input_line)
        if not match:
            print(f'Day 16, Part 1--{input_line}')

    for input_line in input_data:
        input_line = input_line.strip().lstrip()
        match = part_2(input_line)
        if match == 3:
            print(f'Day 16, Part 2--{input_line}')
