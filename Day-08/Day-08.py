# Advent of Code 2015, Day-08
# https://adventofcode.com/2015
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

ESC = '\\'
QUOTE = '\"'
HEX = 'x'


def part_1(input_line):
    in_length = 0
    out_length = 0

    input_line = input_line[1:-2]  # strip off leading quote, trailing quote and newline
    out_length += len(input_line) + 2
    # print(f'{input_line}')
    # print(f'Total Raw Length = {out_length}')
    while input_line:
        one_char = input_line[0]
        # print({one_char},end='')
        if one_char == ESC:
            # print('--Handle escape char',end='')
            next_char = input_line[1]
            # print(f' ({next_char}',end='')
            if next_char == HEX:
                # print(f'{input_line[2:4]})',end='')
                input_line = input_line[4:]  # skip the next 4 char -- i.e. \x27
            elif (next_char == QUOTE) or (next_char == ESC):
                # print(')')
                input_line = input_line[2:]  # skip 2 char -- i.e \" or \\
            else:  # some unknown esc char
                print(f'Error--Unknown escape char ({next_char})')

        else:
            # print(f'--Regular char ({one_char})',end='')
            input_line = input_line[1:]

        in_length += 1
        # print(f' ({in_length}), ({out_length})')
        # print(f'Line length = {in_length}')

    return in_length, out_length


def part_2(input_line):
    in_length = 0
    out_length = 0

    input_line = input_line[:-1]  # strip newline
    in_length += len(input_line)
    # print(f'{input_line}')
    # print(f'Total Raw Length = {out_length}')
    while input_line:
        one_char = input_line[0]
        # print({one_char},end='')

        if (one_char == QUOTE) or (one_char == ESC):
            out_length += 2
        else:
            out_length += 1

        # print(f'in ({in_length}), out ({out_length})')
        input_line = input_line[1:]

    return in_length, out_length + 2  # add the enclosing quotes to the resulting string


if __name__ == '__main__':

    in_total = 0
    out_total = 0

    with open('Day-08-data.txt', 'r') as f:
        input_data = f.readlines()

    for input_line in input_data:
        in_length, out_length = part_1(input_line)
        in_total += in_length
        out_total += out_length

    print(f'Day 08, Part 1--Total Raw - Total Memory = {out_total - in_total}')

    in_total = 0
    out_total = 0

    with open('Day-08-data.txt', 'r') as f:
        input_data = f.readlines()

    for input_line in input_data:
        in_length, out_length = part_2(input_line)
        in_total += in_length
        out_total += out_length

    print(f'Day 08, Part 2--End Length - Start Length = {out_total - in_total}')
