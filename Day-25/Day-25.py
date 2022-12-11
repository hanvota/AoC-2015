# Advent of Code 2015, Day-25
# https://adventofcode.com/2015
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def num_of_code(row_, column_):
    return sum(range(row_ + column_ - 1)) + column_


def next_code(cur_code):
    return (cur_code * 252533) % 33554393


if __name__ == '__main__':

    with open('Day-25-data.txt', 'r') as f:
        input_data = f.readlines()

    for input_line in input_data:
        print(f'{input_line}')

    # noinspection PyUnboundLocalVariable
    _, row_frag = input_line.split('row')
    row, col_frag = row_frag.split(',')
    _, col = col_frag.split('column')
    current_code = 20151125

    count = num_of_code(int(row), int(col[:-2]))

    for i in range(count - 1):
        current_code = next_code(current_code)

    print(f'Day 25, Part 1--Code is {current_code}')
    print(f'Day 25, Part 2--No Part 2')
