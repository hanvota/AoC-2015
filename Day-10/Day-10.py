# Advent of Code 2015, Day-10
# https://adventofcode.com/2015
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

STARTING_STRING = '1113222113'
# STARTING_STRING = '1'
TOTAL_ITERATION_TO_RUN = 40


def process_string(s: str) -> str:  # takes in 1 string, process, returns a new string
    new_string = ''
    in_string = s
    current_char_count = 1
    previous_char = ''
    char = ''
    while in_string:
        char = in_string[0]
        if previous_char == '':  # at the beginning of string
            pass
        elif char == previous_char:  # in a run of same char
            current_char_count += 1
        else:  # new char from the previous run
            new_string += str(current_char_count) + previous_char
            current_char_count = 1  # reset the count
        previous_char = char
        in_string = in_string[1:]  # advance 1 letter
    new_string += str(current_char_count) + char
    return new_string


if __name__ == '__main__':
    input_string = STARTING_STRING
    result_string = ''
    for _ in range(TOTAL_ITERATION_TO_RUN):
        result_string = process_string(input_string)

        input_string = result_string

    # print(f'Day 10, Part 1--Final result ({result_string}), Length {len(result_string)}')
    print(f'Day 10, Part 1--Length {len(result_string)}')
    # part 2 using 50 iterations takes a long time to run and result is length 3579328

    # print(f'Day 10, Part 2--')
