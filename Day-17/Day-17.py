# Advent of Code 2015, Day-17
# https://adventofcode.com/2015
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from itertools import combinations

VOLUME = 150


def part_1_2(containers_, volume):
    # cycle thru B bottles of containers ( 2 or more bottles )
    # take combinations of containers, taken B bottles at a time
    # if sum the volume that each combination can hold is the goal, make a note.

    total_combo = 0
    minimum_combo = 0

    b = len(containers_)
    for i in range(b - 1):
        c = combinations(containers_, i)  # total number of bottles, taken i at a time.
        for combo in c:
            if sum(combo) == volume:
                total_combo += 1
        # since we start with the combination with the fewest bottles and proceed up,
        # the 1st number of matched combination will be the minimum
        if total_combo > 0 and minimum_combo == 0:
            minimum_combo = total_combo

    return total_combo, minimum_combo


if __name__ == '__main__':
    with open('Day-17-data.txt', 'r') as f:
        input_data = f.read().split()
    containers = list(map(int, input_data))  # convert to a list of int

    total, minimum = part_1_2(containers, VOLUME)
    print(f'Day 17, Part 1--Total combinations of containers to hold {VOLUME} liters is {total}')
    print(f'Day 17, Part 2--Minimum combinations of containers to hold {VOLUME} liters is {minimum}')
