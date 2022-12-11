# Advent of Code 2015, Day-13
# https://adventofcode.com/2015
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import itertools
import sys


def build_data_structures(in_line):
    people_set = set()
    happy_list = []
    for line in in_line:
        i = (line.strip().lstrip())[:-1].split()
        person_1 = i[0]
        person_2 = i[-1]
        happiness = int(i[3])
        if i[2] == 'lose':
            happiness = -1 * happiness

        people_set.add(person_1)
        people_set.add(person_2)
        happy_list.append([person_1, person_2, happiness])

    return people_set, happy_list


def happiness_score_per_couple(person_1, person_2, happiness_score):
    # For part 2, if either person is 'Me', score = 0
    if person_1 == 'Me' or person_2 == 'Me':
        return 0
    for happy_ in happiness_score:
        if happy_[0] == person_1 and happy_[1] == person_2:
            return happy_[2]


def part_1(people_set, happy_list):
    best_score = -1 * sys.maxsize
    # for i in happy_list:
    #     print(i)
    people_permutation = itertools.permutations(people_set, len(people_set))
    # print('People permutation')
    for i in people_permutation:
        i = list(i)
        happy_score = 0
        for j in range(len(i) - 1):
            # for each pair of people (A and B), calculate the happiness of A -> B and also B -> A
            happy_ = happiness_score_per_couple(i[j], i[j + 1], happy_list)
            happy_score += happy_
            happy_ = happiness_score_per_couple(i[j + 1], i[j], happy_list)
            happy_score += happy_

        # Happiness score of the last person to the 1st person (circular table)
        happy_ = happiness_score_per_couple(i[-1], i[0], happy_list)
        happy_score += happy_
        happy_ = happiness_score_per_couple(i[0], i[-1], happy_list)
        happy_score += happy_

        if happy_score > best_score:
            best_score = happy_score

    return best_score


if __name__ == '__main__':
    with open('Day-13-data.txt', 'r') as f:
        input_data = f.readlines()

    people, happy = build_data_structures(input_data)

    best_happiness = part_1(people, happy)
    print(f'Day 13, Part 1--Total change in happiness is {best_happiness}')

    # For part 2, add "Me" to the people set and re run
    people.add('Me')
    best_happiness = part_1(people, happy)
    print(f'Day 13, Part 2--Total change in happiness is {best_happiness}')
    # print(f'Day 13, Part 2--')
