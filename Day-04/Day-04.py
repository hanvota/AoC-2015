# Advent of Code 2015, Day-04
# https://adventofcode.com/2015

# help with using hash, md5 from Reddit  https://www.reddit.com/r/adventofcode/comments/3vdn8a/day_4_solutions/

from hashlib import md5


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def Day_04_part_01(key: str, numberOfLeadingZeros: int) -> int:
    counter = 0

    while True:
        counter += 1
        hash = md5((key + str(counter)).encode()).hexdigest()
        if hash.startswith('0' * numberOfLeadingZeros):
            return counter


if __name__ == '__main__':
    dataFile = open('Day-04-data.txt', 'r')
    puzzleInput = dataFile.readlines()[0]
    dataFile.close()

    # print(f'Instruction List {instructionsList}')
    print(f'Puzzle Input is ({puzzleInput})')
    print(f'Day 04, Part 1--{Day_04_part_01(key=puzzleInput, numberOfLeadingZeros=5)}')
    print(f'Day 04, Part 2--{Day_04_part_01(key=puzzleInput, numberOfLeadingZeros=6)}')
