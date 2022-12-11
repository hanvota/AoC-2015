# Advent of Code 2015, Day-07
# https://adventofcode.com/2015
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np

connections = {}  # wiring board with list of operations - {'operation',['op1','op2','destination']}
wires = {}  # dictionary with 'Name of wire', value for each wire


def print_wires_dict():
    print('\nwires dictionary content')
    for wire, value in wires.items():
        print(f'Wire ({wire}) <<<--- ({value})')


def print_connections():
    print(f'\nconnections content, length is {len(connections)}')
    for wire, connection in connections.items():
        print(wire, connection)


def value_at_wire(wire):  # if a wire exists, return its value, otherwise 0
    if wire in connections:
        return np.uint16(wires[wire])
    else:
        return np.uint16(wire)


def build_connections(connection):
    # print(connection)

    # different types of lines --
    # ['44430', '->', 'b'] -- direct assignment with 3 parts,
    # ['NOT', 'dq', '->', 'dr'] -- NOT with 4 parts,
    # ['eg', 'AND', 'ei', '->', 'ej'] -- AND, OR with 5 parts
    destination = connection[-1]  # the destination is always the last item

    length_of_line = len(connection)
    if length_of_line == 3:  # ['44430', '->', 'b'] -- direct assignment with 3 parts
        operation = '='
        op1 = connection[0]
        op2 = None
    elif length_of_line == 4:  # ['NOT', 'dq', '->', 'dr'] -- NOT with 4 parts
        operation = connection[0]
        op1 = connection[1]
        op2 = None
    elif length_of_line == 5:  # ['eg', 'AND', 'ei', '->', 'ej'] -- AND, OR with 5 parts
        operation = connection[1]
        op1 = connection[0]
        op2 = connection[2]
    else:
        print(f'ERROR--Unknown line {connection}')
        return

    connections[destination] = [op1, op2, operation]


def make_connection(task):  # perform the operation of each task and return the result for that wire connection
    # print(f'task - {task}')

    operation = task[-1]
    # different types of lines --
    # ['44430', '->', 'b'] -- direct assignment with 3 parts,
    # ['NOT', 'dq', '->', 'dr'] -- NOT with 4 parts,
    # ['eg', 'AND', 'ei', '->', 'ej'] -- AND, OR with 5 parts

    if operation == '=':  # assignment operation
        return value_at_wire(task[0])
    elif operation == 'NOT':  #
        return 65536 + ~value_at_wire(task[0])

    op1 = value_at_wire(task[0])
    op2 = value_at_wire(task[1])
    if operation == 'AND':
        return op1 & op2
    if operation == 'OR':
        return op1 | op2
    if operation == 'LSHIFT':
        return op1 << op2
    if operation == 'RSHIFT':
        return op1 >> op2


def process_connections():
    wire_keys = set(connections.keys())  # get a set with all the key wires from connections
    # print(f'keys {wire_keys}')

    while wire_keys:
        wire_keys_copy = wire_keys.copy()
        for wire in wire_keys_copy:  # for each wire, go thru the remainder of the connections to solve the wiring for it
            try:
                wires[wire] = make_connection(connections[wire])
                wire_keys.remove(wire)
            except KeyError as e:
                continue

    # for wire, connection in connections.items():
    #     op1, op2, operation = connection
    #     print(f'wire ({wire}), <-- op1({op1}), op2({op2}), operation ({operation})')
    #     make_connection(destination, op1, op2, operation)
    # print_connections()
    # print_wires_dict()


if __name__ == '__main__':

    # # x = 123
    # # y = 456
    # # print(f'x AND y -> {x & y}')
    # # print(f'x OR y -> {x | y}')
    # # print(f'x LSHIFT 2 -> {x << 2}')
    # # print(f'y RSHIFT 2 -> {y >> 2}')
    # # print(f'NOT x -> {~x}, {65536 + ~x}')
    # # print(f'NOT y -> {~y}, {65536 + ~y}')
    #

    with open('Day-07-data.txt', 'r') as f:
        input_data = f.readlines()

    for input_line in input_data:
        # print(f'{input_line}')
        one_line = input_line.split()  # split into individual components
        build_connections(one_line)

    process_connections()

    print(f'Day7, Part 1--Wire a: {wires["a"]}')

    wire_a = wires["a"]
    wires = {}
    # connections = {}
    # for input_line in input_data:
    #     one_line = input_line.split()  # split into individual components
    #     build_connections(one_line)

    new_connection = f'{wire_a} -> b'
    build_connections(new_connection.split())
    process_connections()
    print(f'Day7, Part 2--Revised Wire a: {wires["a"]}')
    #
