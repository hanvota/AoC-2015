# Advent of Code 2015, Day-12
# https://adventofcode.com/2015
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json
import re


def part_1(input_string):
    number_pattern = re.compile(r'(-?\d+)')  # group of optional neg sign "-?" and 1 or more digits "\d+"
    part_1_data = str(input_string).strip().lstrip()
    number_list = number_pattern.findall(part_1_data)
    total = sum(int(i) for i in number_list)

    return total


def part_2(input_json):
    if isinstance(input_json, int):
        return input_json
    elif isinstance(input_json, list):
        return sum(part_2(i) for i in input_json)
    elif isinstance(input_json, dict):
        if "red" in input_json.values():
            return 0
        else:
            return sum(part_2(i) for i in input_json.values())

    return 0


if __name__ == '__main__':
    with open('Day-12-data.txt', 'r') as f:
        input_data = f.readlines()

    total = part_1(input_data)
    print(f'Day 12, Part 1--Sum of list is {total}')

    with open("Day-12-data.txt") as f:
        input_data = json.load(f)
        total = (part_2(input_data))

    print(f'Day 12, Part 2--Sum of list is {total}')
    print(json.dumps(input_data, sort_keys=True, indent=4))
