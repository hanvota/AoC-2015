# Advent of Code 2015, Day-23
# https://adventofcode.com/2015
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# import re


# inspect_set = ('hlf', 'tpl', 'inc', 'jmp', 'jie', 'jio')
# pattern =r'^(\w{3}) (.),?(.*)$'

# op1 = ('hlf','tlp','inc','jmp')
op2 = ('jio', 'jie')  # opcodes with 2 operands


def run_program(codes):
    # print(f'({code:10})--({opcode})--({operand})')
    reg = {'a': 0, 'b': 0}
    pc = 0
    while pc < len(codes):
        offset = 0
        opcode = codes[pc][:3]
        operand = codes[pc][4:].strip()
        if opcode in op2:
            offset = int(operand[2:])
            operand = operand[0]
        elif opcode == 'jmp':
            offset = int(operand)

        if opcode == 'hlf':
            reg[operand] //= 2
        elif opcode == 'tpl':
            reg[operand] *= 3
        elif opcode == 'inc':
            reg[operand] += 1
        elif opcode == 'jmp':
            pc += offset - 1
        elif opcode == 'jie':
            if reg[operand] % 2 == 0:
                pc += offset - 1
        elif opcode == 'jio':
            if reg[operand] == 1:
                pc += offset - 1
        else:
            print(f'Unknown operation {opcode} {operand}')
        # print(pc, reg_a, reg_b)
        pc += 1
    return reg


if __name__ == '__main__':
    with open('Day-23-data.txt', 'r') as f:
        input_data = f.readlines()

    registers = run_program(input_data)
    reg_b = registers['b']
    print(f'Day 23, Part 1--Register b has {reg_b}')

    # print(f'Day 23, Part 2--')
