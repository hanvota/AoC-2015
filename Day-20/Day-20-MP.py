# Advent of Code 2015, Day-20 Using Multiprocessing
# https://adventofcode.com/2015
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Problem with running the part_2_MP.
# for some reasons, the dictionary house_visited if not being updated correctly by the process_house_part_2.
# The results AFTER house 50 (51 and on) we SHOULD NOT get presents from elf #1 anymore since he already
# gave in the first 50 houses. This problem occurs when even house_visited is defined as a global.

import time
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed

# import concurrent.futures

# from __future__ import annotations
# from multiprocessing import Pool

# INPUT = 33100000
INPUT = 500000
BATCH = 250

PRESENTS_PER_ELF_PART_1 = 10
PRESENTS_PER_ELF_PART_2 = 11
MAX_HOUSE_PER_ELF = 50

house_visited = {}  # {int(str): int(house visited so far)} dict for the number of houses that each elf has visited


def process_house_part_1(house_number):  # function for multiprocessing

    number_presents = 0
    # print(f'House {house_number:4,d} -', end='')
    for elf_ in range(1, house_number + 1):
        if (house_number % elf_) == 0:
            j = elf_ * PRESENTS_PER_ELF_PART_1
            number_presents += j

        # print(f'{int(j):5d}',end='')
    # print(f'->{number_presents:12,d} presents')

    return house_number, number_presents


def process_house_part_2(house_number):  # function for multiprocessing
    number_presents = 0
    global house_visited
    # print(f'House {house_number:4,d} -', end='')
    for elf_ in range(1, house_number + 1):
        if elf_ not in house_visited.keys():  # start an entry for this elf if not here before
            house_visited[elf_] = 0
        if house_visited[elf_] < MAX_HOUSE_PER_ELF:
            if (house_number % elf_) == 0:
                # print(f'----Elf {elf_} visiting ({house_visited[elf_]+1}/{MAX_HOUSE_PER_ELF})')
                number_presents += elf_ * PRESENTS_PER_ELF_PART_2
                house_visited[elf_] += 1  # 1 more house visited

    print(f'->House {house_number} got {number_presents:12,d} presents')

    return house_number, number_presents


def part_1_MP(minimum):
    presents_ = 0
    inc = 0
    # create a process pool
    with ProcessPoolExecutor() as executor:
        # submit tasks and get results
        while True:
            # submit tasks and collect futures
            futures = [executor.submit(process_house_part_1, i) for i in range(inc, inc + BATCH)]
            # future = executor.submit(process_house, h)
            # futures.append(future)
            # process task results as they are available
            for future in as_completed(futures):
                # retrieve the result
                (house_, presents_) = future.result()
                if presents_ >= minimum:
                    return house_, presents_

            inc += BATCH
            print(f'House {house_:,d} -->{presents_:12,d} presents')

    # return house_, presents_


def part_2(minimum):
    house_ = 0
    presents_ = 0
    global house_visited
    while presents_ < minimum:
        house_ += 1
        presents_ = 0
        for elf_ in range(1, house_ + 1):
            if elf_ not in house_visited.keys():  # start an entry for this elf if not here before
                house_visited[elf_] = 0
            if (house_visited[elf_] < MAX_HOUSE_PER_ELF) and (house_ % elf_) == 0:
                # print(f'----Elf {elf_} visiting ({house_visited[elf_]+1}/{MAX_HOUSE_PER_ELF})')
                j = elf_ * PRESENTS_PER_ELF_PART_2
                presents_ += j
                house_visited[elf_] += 1  # 1 more house visited
                if house_ == 51:
                    print(f'House {house_}.Elf {elf_} gave {j} presents')

            # print(f'{int(j):5d}',end='')
        print(f'House {house_:,d} -->{presents_:12,d} presents')

    return house_, presents_


def part_2_MP(minimum):
    presents_ = 0
    inc = 1
    # house_visited = {}  # {int(elf_number): int(house visited so far)} dict for the number of houses that each elf has visited
    # create a process pool
    with ProcessPoolExecutor() as executor:
        # submit tasks and get results
        while presents_ < minimum:
            # submit tasks and collect futures
            futures = [executor.submit(process_house_part_2, i) for i in range(inc, inc + BATCH)]
            # process task results as they are available
            for future in as_completed(futures):  # collect results as they come in, no order.
                # for future in futures:  # collect results in order
                # retrieve the result
                (house_, presents_) = future.result()
                if presents_ >= minimum:
                    return house_, presents_

            inc += BATCH


if __name__ == '__main__':
    start = time.perf_counter()
    # house, presents = part_1_MP(INPUT)
    # print(f'Day 20, Part 1 MP--House {house:,} received {presents:,} presents.')

    # house, presents = part_2_MP(INPUT)
    house, presents = part_2(INPUT)
    print(f'Day 20, Part 2--House {house:,} received {presents:,} presents.')

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 4)} second(s)')
