# Advent of Code 2015, Day-05
# https://adventofcode.com/2015
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

VOWELS = {'a', 'e', 'i', 'o', 'u'}
MINIMUMNUMEROFVOWELS = 3
FORBIDDEN = ['ab', 'cd', 'pq', 'xy']
ALLOWEDDOUBLELETTERS = ['aa', 'bb', 'cc', 'dd']


def countVowels(string):
    numberOfVowels = 0

    for character in string:
        if character in VOWELS:
            numberOfVowels += 1

    return numberOfVowels


def hasDoubleLetter(string):
    lastChar = ''
    for thisChar in string:
        if thisChar == lastChar:
            return True
        lastChar = thisChar

    return False


def containsForbidden(string):
    for forbiddenPair in FORBIDDEN:
        if forbiddenPair in string:
            return True

    return False


def goodStringPart1(string):  # Check if string is a nice string based on criteria for Part 1

    if containsForbidden(string):
        return False

    if countVowels(string) < MINIMUMNUMEROFVOWELS:
        return False

    if hasDoubleLetter(string) == False:
        return False

    return True


def criteria1ForPart2(string):
    for i in range(len(string) - 3):
        pair = string[i:i + 2]  # take each pair of letters

        if pair in string[i + 2:]:  # and see it they are in the rest of the string
            return True

    return False


def criteria2ForPart2(string):
    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            return True

    return False


def goodStringPart2(string):  # Check if string is a nice string based on criteria for Part 2

    if criteria1ForPart2(string) == False:
        return False

    if criteria2ForPart2(string) == False:
        return False

    return True


if __name__ == '__main__':

    numberOfNiceStringPart1 = 0
    numberOfNiceStringPart2 = 0

    dataFile = open('Day-05-data.txt', 'r')

    oneString = dataFile.readline().strip()
    while oneString != '':

        if goodStringPart1(oneString):
            numberOfNiceStringPart1 += 1

        if goodStringPart2(oneString):
            numberOfNiceStringPart2 += 1

        oneString = dataFile.readline().strip()

    print(f'Day 05, Part 1--Number of nice strings is {numberOfNiceStringPart1} ')
    print(f'Day 05, Part 2--Number of nice strings is {numberOfNiceStringPart2} ')

    dataFile.close()
