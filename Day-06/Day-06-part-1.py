# Advent of Code 2015, Day-06-part-1
# https://adventofcode.com/2015
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

MAX_X = 999
MAX_Y = 999
ON = 1
OFF = 0
TOGGLE = -1


def print_grid(grid):
    for y in range(MAX_Y):
        print(grid[y])
    print('')


def count_lights(grid, state):
    count = 0
    for y in range(MAX_Y):
        for x in range(MAX_X):
            if grid[y][x] == state:
                count += 1

    return count


def turn_light(grid, start, stop, state):
    start_x, start_y = start
    stop_x, stop_y = stop

    from_x = min(start_x, stop_x)
    to_x = max(start_x, stop_x)
    from_y = min(start_y, stop_y)
    to_y = max(start_y, stop_y)
    # print(f'From ({from_x}, {from_y}) to ({to_x}, {to_y}) -- {state}')

    for x in range(from_x, to_x + 1):
        for y in range(from_y, to_y + 1):
            if state == TOGGLE:
                grid[y][x] = (grid[y][x] + 1) % 2  # 0 -> 1 and 1 -> 0
            else:
                grid[y][x] = state
    # print_grid(grid)


def parse(command):
    state_dict = {'on': ON,
                  'off': OFF,
                  'toggle': TOGGLE}

    # print(f'Command is ({command})')
    commands_list = command.split(' ')
    if commands_list[0] == 'turn':
        commands_list.pop(0)
    state_str = commands_list[0].lower()
    state = state_dict[state_str]
    start = tuple(int(num) for num in (commands_list[1].split(',')))  # split at the ',' and convert to int
    stop = tuple(int(num) for num in (commands_list[3].split(',')))

    # print(state,start,stop)
    return start, stop, state


if __name__ == '__main__':
    grid = [[0] * (MAX_X + 1) for _ in range(MAX_Y + 1)]
    start = stop = (0, 0)
    # turn_light(grid, (0, 0), (5, 5), ON)
    # turn_light(grid, (3, 3), (4, 4), OFF)
    # turn_light(grid, (2, 2), (6, 6), TOGGLE)

    # print(f'{grid}')
    data_file = open('Day-06-data.txt', 'r')

    command_string = data_file.readline().strip()
    while command_string != '':
        start, stop, state = parse(command_string)

        # print(command_string,start,stop,state)
        turn_light(grid, start, stop, state)
        # print_grid(grid)
        command_string = data_file.readline().strip()

    print(f'Day 06, Part 1--Total lights is {count_lights(grid, ON)}')

    data_file.close()
