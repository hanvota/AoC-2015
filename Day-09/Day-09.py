# Advent of Code 2015, Day-09
# https://adventofcode.com/2015
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import itertools


def print_distances_table(table):
    for row in list(table.keys())[::2]:  # print every other row, since
        print(row, table[row])


if __name__ == '__main__':

    places = set()
    pairs = {}

    with open('Day-09-data.txt', 'r') as input_data_file:
        input_data = input_data_file.readlines()

    for input_line in input_data:
        place1, _, place2, _, distance = input_line.strip().split()
        distance = int(distance)
        places.add(place1)
        places.add(place2)
        # print(f'Places -- {places}')
        pairs[(place1, place2)] = distance
        pairs[(place2, place1)] = distance
        # print(f'Pairs -- {pairs}')

    print_distances_table(pairs)

    places = list(places)

    places_permutation = itertools.permutations(places)
    routes = {}

    for i in places_permutation:
        distance = 0
        # Check each entry separately.
        for n in range(len(i) - 1):
            # try:
            distance += pairs[(i[n], i[n + 1])]
            # except KeyError:
            #     distance = -1
            #     break
        # if distance != -1:
        routes[i] = distance

    shortest_distance = min(routes.values())
    shortest_route = min(routes, key=routes.get)
    print(f'Shortest route is {shortest_route}, Distance = {shortest_distance}')
    longest_distance = max(routes.values())
    longest_route = max(routes, key=routes.get)
    print(f'Longest route is {longest_route}, Distance = {longest_distance}')
