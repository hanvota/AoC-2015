# Advent of Code 2015, Day-24
# https://adventofcode.com/2015
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from itertools import combinations
import numpy


def part_1(data):
    # grp_f = []   # front compartments
    # grp_r = []   # right compartments
    # grp_l = []   # left compartments
    compartments = 3
    all_good_choices = []
    unique_front = set()

    all_weights = [int(num) for num in data]
    # print(all_weights, sum(all_weights))

    avg_weight = sum(all_weights) / compartments  # 3 compartments
    # print(avg_weight)
    for i in range(1, len(all_weights) - compartments - 1):  # front grp, from all possible weights minus 2 (for the left and right side)
        all_possible_grp_f = combinations(all_weights, i)
        for grp_f in all_possible_grp_f:
            if sum(grp_f) == avg_weight:
                qe_f = numpy.product(grp_f)
                grp_f = list(grp_f)
                remainder = [k for k in all_weights if k not in grp_f]
                for k in range(1, len(remainder) - 1):
                    all_possible_grp_r = combinations(remainder, k)
                    for grp_r in all_possible_grp_r:
                        if sum(grp_r) == avg_weight:
                            grp_r = list(grp_r)
                            grp_l = [k for k in remainder if k not in grp_r]
                            choice = [grp_f, grp_r, grp_l, qe_f]
                            if tuple(grp_f) not in unique_front:
                                unique_front.add(tuple(grp_f))
                                all_good_choices.append(choice)
                                return choice


def part_2(data):
    # grp_f = []   # front compartments
    # grp_r = []   # right compartments
    # grp_l = []   # left compartments
    # grp_t = []   # trunk compartments
    compartments = 4
    all_good_choices = []
    unique_front = set()

    all_weights = [int(num) for num in data]
    # print(all_weights, sum(all_weights))

    avg_weight = sum(all_weights) / compartments  # 4 compartments
    # print(avg_weight)
    for f_ in range(1, len(all_weights) - compartments - 1):  # front grp, from all possible weights minus 3 (for the left and right side, trunk)
        all_possible_grp_f = combinations(all_weights, f_)
        for grp_f in all_possible_grp_f:
            if sum(grp_f) == avg_weight:
                qe_f = numpy.product(grp_f)
                grp_f = list(grp_f)
                remainder = [k for k in all_weights if k not in grp_f]

                for t in range(1, len(remainder) - compartments - 1):
                    all_possible_grp_t_r_l = combinations(remainder, t)
                    for grp_t in all_possible_grp_t_r_l:
                        if sum(grp_t) == avg_weight:
                            grp_t = list(grp_t)
                            remainder = [k for k in remainder if k not in grp_t]

                            for r in range(1, len(remainder) - compartments - 1):
                                all_possible_grp_r = combinations(remainder, r)
                                for grp_r in all_possible_grp_r:
                                    if sum(grp_r) == avg_weight:
                                        grp_r = list(grp_r)
                                        grp_l = [k for k in remainder if k not in grp_r]
                                        choice = [grp_f, grp_t, grp_r, grp_l, qe_f]
                                        if tuple(grp_f) not in unique_front:
                                            unique_front.add(tuple(grp_f))
                                            all_good_choices.append(choice)
                                            return choice


if __name__ == '__main__':
    with open('Day-24-data.txt', 'r') as f:
        input_data = f.readlines()

    # all_weights = [int(num) for num in input_data]
    # print(all_weights, sum(all_weights))

    p = part_1(input_data)
    print(p)
    print(f'Day 24, Part 1--Best combination is (QE= {p[3]}) with Front= {p[0]}, Right= {p[1]}, Left= {p[2]})')
    p = part_2(input_data)
    print()
    print(p)
    print(f'Day 24, Part 2--Best combination is (QE= {p[4]}) with Front= {p[0]}, Trunk= {p[1]}, Right= {p[2]}, Left= {p[3]})')
