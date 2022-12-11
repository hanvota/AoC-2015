# Advent of Code 2015, Day-03
# https://adventofcode.com/2015

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Santa starts at house 0,0. He moves -- ^ - N - y -= 1
#                                        < - W - x -= 1
#                                        v - S - y += 1
#                                        > - E - x += 1

santaX = 0  # coordinate for Santa
santaY = 0
roboX = 0  # cordinate for Robo-Santa
roboY = 0

house = (santaX, santaY)  # a tuple of coordinate of a house (Both Santa and Robo-Santa start at the same house)
housesVisited = {house}  # a set representing all the houses that have been visited by Santa, starting at 1st house.
numberofHouseWithPresent = 1


# using a set since we don't care that a house can be visited more than once.

def moveLocation(direction):
    deltaX = deltaY = 0

    if direction == '^':
        deltaY = -1
    elif direction == '<':
        deltaX = -1
    elif direction == 'v':
        deltaY = 1
    elif direction == '>':
        deltaX = 1
    else:
        print(f'Unknown instruction "{instruction}"')

    return (deltaX, deltaY)


if __name__ == '__main__':
    dataFile = open('Day-03-data.txt', 'r')
    instructionsList = dataFile.readlines()[0]

    print(f'Length of Intruction is {len(instructionsList)}')

    for instruction in instructionsList:  # Santa's movements

        x, y = moveLocation(instruction)
        santaX += x
        santaY += y

        house = (santaX, santaY)
        housesVisited.add(house)

    print(f'Part 1--Santa visited {len(housesVisited)} houses and is at location {santaX}, {santaY}')

    # Part 2--reset starting points. Now with Santa and Rpbp-Santa
    santaX = 0  # coordinate for Santa
    santaY = 0
    roboX = 0  # cordinate for Robo-Santa
    roboY = 0

    house = (santaX, santaY)  # a tuple of coordinate of a house (Both Santa and Robo-Santa start at the same house)
    housesVisited = {house}  # a set representing all the houses that have been visited by Santa, starting at 1st house.
    numberofHouseWithPresent = 1
    # using a set since we don't care that a house can be visited more than once.

    # Part 2 involves Santa and Robo-Santa, each taking turn with the instruction from the instructionList

    if len(instructionsList) % 2 != 0:  # need even nunmber of instructions since we have to move Santa AND Robo-Santa
        print(f'Odd number of instructions to involve BOTH Santa and Robo-Santa. Please check')

    while instructionsList != '':
        instruction = instructionsList[0]  # Santa's movements
        x, y = moveLocation(instruction)
        santaX += x
        santaY += y

        house = (santaX, santaY)
        housesVisited.add(house)
        instructionsList = instructionsList[1::]  # Remove the instruction taken by Santa

        instruction = instructionsList[0]  # Robo-Santa's movements
        x, y = moveLocation(instruction)
        roboX += x
        roboY += y

        house = (roboX, roboY)
        housesVisited.add(house)
        instructionsList = instructionsList[1::]  # Remove the instruction taken by Robo-Santa

    print(f'Part 2--Santa and Robo-Santa visited {len(housesVisited)} houses and \n'
          f'\t\tSanta is at location {santaX}, {santaY}, and \n'
          f'\t\tRobo-Santa is at location {roboX}, {roboY}')

    dataFile.close()
