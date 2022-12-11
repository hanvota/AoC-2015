# Advent of Code 2015, Day-01
# https://adventofcode.com/2015

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


if __name__ == '__main__':
    dataFile = open('Day-01-data.txt', 'r')
    instructionsList = dataFile.readlines()[0]
    dataFile.close()

    # print(f'Instruction List {instructionsList}')
    print(f'Length of instructions is {len(instructionsList)}')

# Santa starts at Floor 0. Follow the instructions. Each "(" is go up 1 floor and ")" is go down one floor.
floor = 0
for instruction in instructionsList:
    if instruction == "(":  # go up 1 floor
        floor += 1
    else:  # otherwise go down 1 floor
        floor -= 1

print(f"Part 1--I am now on Floor {floor}")

# Santa starts at Floor 0. Follow the instructions. Each "(" is go up 1 floor and ")" is go down one floor.
# Show instruction number (starting at #1) that cause Santa to enter basement (Floor -1)
floor = 0
step = 1
for instruction in instructionsList:
    if instruction == "(":
        floor += 1
    else:
        floor -= 1

    if floor == -1:  # if Santa is at basement, stop and get out of loop
        break

    step += 1

print(f"Part 2--I am now on Floor {floor} at step {step}")
