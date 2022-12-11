# Advent of Code 2015, Day-11
# https://adventofcode.com/2015
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import re
from string import ascii_lowercase

BANNED_LETTERS = 'iol'


def rule_1(passwd):  # Contains triplets from 'abc' to 'xyz'
    for letter in ascii_lowercase[:-2]:  # generate triplets from 'abc' to 'xyz'
        triplet = letter + chr(ord(letter) + 1) + chr(ord(letter) + 2)
        if triplet in passwd:
            break
    else:
        return False

    return True


def rule_2(passwd):  # Ban letters
    m = re.search(r'[iol]', passwd)
    return not m


def rule_3(passwd):  # at least 2 couplets, i.e. 'aa' to 'zz'
    m = re.findall(r'(\w)\1.*(\w)\2', passwd)
    return m


def valid_password(passwd):
    m = [rule_1(passwd), rule_2(passwd), rule_3(passwd)]
    return all(m)


def generate_next_password(passwd):
    char_list = list(passwd)
    # iterate over string in reverse order
    for i in range(len(char_list) - 1, -1, -1):
        c = char_list[i]
        while True:
            next_char = chr((ord(c) - ord('a') + 1) % 26 + ord('a'))
            if next_char not in BANNED_LETTERS:
                break
            else:
                c = next_char
        char_list[i] = next_char

        # a..z => 0..25
        # ord(password[i]) - ord('a')
        # a..z => (1..26) % 26 = 1..25 0
        # ord(password[i]) - ord('a') + 1) % 26
        # a..z => b..z a
        # if this character is now 'a', it was 'z' and we should convert next character, or break otherwise
        if next_char != 'a':
            break

    return ''.join(char_list)


if __name__ == '__main__':
    password = 'hxbxwxba'

    while True:
        password = generate_next_password(password)

        valid = valid_password(password)
        if valid:
            break

    print(f'Day 11, Part 1--Next valid password is {password}')

    while True:
        password = generate_next_password(password)

        valid = valid_password(password)
        if valid:
            break

    print(f'Day 11, Part 2--Next valid password is {password}')
    # print(f'Day 11, Part 2--')
