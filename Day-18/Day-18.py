# Advent of Code 2015, Day-18
# https://adventofcode.com/2015
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# NOT very 'pythonic'

BOARD_SIZE = 100
NUMBER_STEPS = 100


def show_board(in_board):
    for i in in_board:
        print(i)
    print()


def build_board(dimension):
    # Build a new board with a surrounding border of '.'
    new_board = []

    with open('Day-18-data.txt', 'r') as f:
        input_data = f.readlines()

    new_board.append(list('.' * (dimension + 2)))

    for input_line in input_data:
        input_line = input_line.strip().lstrip()
        new_board.append(list('.' + input_line + '.'))

    new_board.append(list('.' * (dimension + 2)))

    return new_board


def count_lights(in_board):
    size = len(in_board)
    count = 0
    for row in range(1, size - 1):
        for col in range(1, size - 1):
            if in_board[row][col] == '#':
                count += 1

    return count


def count_neighbors(in_board, at_row, at_col):
    neighbors = 0
    for y in [-1, 0, 1]:
        for x in [-1, 0, 1]:
            if in_board[at_row + y][at_col + x] == '#':
                neighbors += 1
    if in_board[at_row][at_col] == "#":  # don't count the state of the location itself, just the neighbors
        neighbors -= 1
    # print(neighbors)

    return neighbors


def loop_part_1(in_board):  # build a new board from the previous one for part 1 interation
    size = len(in_board)
    # new_board = build_board(BOARD_SIZE)

    new_board = [list('.' * (BOARD_SIZE + 2))]

    for i in range(BOARD_SIZE):
        new_board.append(list('.' * (BOARD_SIZE + 2)))

    new_board.append(list('.' * (BOARD_SIZE + 2)))

    for row in range(1, size - 1):
        for col in range(1, size - 1):
            num_neighbors = count_neighbors(in_board, row, col)
            if in_board[row][col] == '#':  # if 'on' and has 2 or 3 neighbors, stays 'on'
                if num_neighbors in [2, 3]:
                    new_board[row][col] = '#'
                else:
                    new_board[row][col] = '.'
            else:  # else if an 'off' light has 3 neighbors, then turn 'on'
                if num_neighbors == 3:
                    new_board[row][col] = '#'

        #     print(' ',new_board[row][col],end='')
        # print()

    return new_board


def part_1(steps):
    board = build_board(BOARD_SIZE)
    # show_board(board)

    for i in range(steps):
        # print(f'Step {i}')
        board = loop_part_1(board)
        # show_board(board)
        # lights = count_lights(board)
        # print(f'{lights} are on')

    lights = count_lights(board)
    # print(f'{lights} are on')

    return lights


def stuck_lights(in_board):  # create the stuck lights for part 2
    in_board[1][1] = '#'
    in_board[1][BOARD_SIZE] = '#'
    in_board[BOARD_SIZE][1] = '#'
    in_board[BOARD_SIZE][BOARD_SIZE] = '#'
    # print('stuck lights at corners')
    # show_board(in_board)
    return


def part_2(steps):
    board = build_board(BOARD_SIZE)
    # show_board(board)

    for i in range(steps):
        # print(f'Step {i}')
        stuck_lights(board)  # stuck lights in part 2
        board = loop_part_1(board)
        stuck_lights(board)  # stuck lights in part 2
        # show_board(board)
        # lights = count_lights(board)
        # print(f'{lights} are on')

    lights = count_lights(board)
    # print(f'{lights} are on')

    return lights


if __name__ == '__main__':
    print(f'Day 18, Part 1--After {NUMBER_STEPS}, {part_1(NUMBER_STEPS)} lights are ON')
    print(f'Day 18, Part 2--After {NUMBER_STEPS}, {part_2(NUMBER_STEPS)} lights are ON')
