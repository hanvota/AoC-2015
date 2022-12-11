# Advent of Code 2015, Day-20
# https://adventofcode.com/2015
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import time

# INPUT = 33100000
INPUT = 500000

MAX_HOUSE_PER_ELF = 50
PRESENTS_PER_ELF_PART_1 = 10
PRESENTS_PER_ELF_PART_2 = 11


def part_1(minimum):
    house_ = 0
    presents_ = 0

    while presents_ < minimum:
        house_ += 1
        presents_ = 0
        # print(f'House {house_:4,d} -', end='')
        for elf_ in range(1, house_ + 1):
            if (house_ % elf_) == 0:
                j = elf_ * PRESENTS_PER_ELF_PART_1
                presents_ += j
            # print(f'{int(j):5d}',end='')
        # print(f'->{presents_:12,d} presents')
        # if house >9:
        #     print()
        #     break
    return house_, presents_


def part_2(minimum):
    house_ = 0
    presents_ = 0
    house_visited = {}  # {int(elf_number): int(house visited so far)} dict for the number of houses that each elf has visited
    while presents_ < minimum:
        house_ += 1
        presents_ = 0
        # print(f'House {house_:4,d} -', end='')
        for elf_ in range(1, house_ + 1):
            if elf_ not in house_visited.keys():  # start an entry for this elf if not here before
                house_visited[elf_] = 0
            if (house_visited[elf_] < MAX_HOUSE_PER_ELF) and ((house_ % elf_) == 0):
                # print(f'----Elf {elf_} visiting ({house_visited[elf_]+1}/{MAX_HOUSE_PER_ELF})')
                j = elf_ * PRESENTS_PER_ELF_PART_2
                presents_ += j

                house_visited[elf_] += 1  # 1 more house visited
            # print(f'{int(j):5d}',end='')
        # print(f'->{presents_:12,d} presents')
        # if house >9:
        #     print()
        #     break

    return house_, presents_


if __name__ == '__main__':
    start = time.perf_counter()
    house, presents = part_1(INPUT)
    print(f'Day 20, Part 1--House {house:,} received {presents:,} presents.')

    house, presents = part_2(INPUT)
    print(f'Day 20, Part 2--House {house:,} received {presents:,} presents.')
    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 4)} second(s)')
