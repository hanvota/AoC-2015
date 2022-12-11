# Advent of Code 2015, Day-15
# https://adventofcode.com/2015
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Totally brute force the solution.

import re

TOTAL_TSP = 100
TOTAL_CAL = 500


def get_score(ingredients_, t1, n1, t2, n2, t3, n3, t4, n4):
    score = 1

    for param in range(4):  # 0-capacity, 1-durability, 2-flavor, 3-texture. Omit 4-calories
        s = max((t1 * int(ingredients_[n1][param])) + (t2 * int(ingredients_[n2][param])) + (t3 * int(ingredients_[n3][param])) + (t4 * int(ingredients_[n4][param])), 0)
        score *= s
    cal = (t1 * int(ingredients_[n1][4])) + (t2 * int(ingredients_[n2][4])) + (t3 * int(ingredients_[n3][4])) + (t4 * int(ingredients_[n4][4]))

    return score, cal


def do_parts(ingredients_, total_capacity, cal_goal):
    best_score_1 = 0  # part 1.
    best_score_2 = 0  # part 2, with calories restrictions
    # print(f'{total_capacity} tsp of {ingredients}')
    for tsp_spr in range(101):
        for tsp_but in range(101):
            for tsp_cho in range(101):
                for tsp_can in range(101):
                    if sum([tsp_spr, tsp_but, tsp_cho, tsp_can]) == total_capacity:
                        # print(f'--{tsp_spr:3d}, {tsp_but:3d}, {tsp_cho:3d}, , {tsp_can:3d}')
                        score, cal = get_score(ingredients_, tsp_spr, 'Sprinkles', tsp_but, 'Butterscotch', tsp_cho, 'Chocolate', tsp_can, 'Candy')
                        if score > best_score_1:
                            best_score_1 = score
                        if cal == cal_goal and score > best_score_2:  # with calories restrictions
                            best_score_2 = score

    return best_score_1, best_score_2


def part_2():
    return


if __name__ == '__main__':
    regex = r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (\d+)'
    ingredients = {}  # 'name': [capacity, durability, flavor, texture, calories]
    with open('Day-15-data.txt', 'r') as f:
        input_data = f.read()

    for name, capacity, durability, flavor, texture, calories in re.findall(regex, input_data):
        ingredients.update({name: [capacity, durability, flavor, texture, calories]})
    # print(ingredients)
    # for name, [a,b,c,d,e] in ingredients.items():
    #     print(name, a,b,c,d,e)

    score_1, score_2 = do_parts(ingredients, TOTAL_TSP, TOTAL_CAL)
    print(f'Day 15, Part 1--Best score is {score_1}')
    print(f'Day 15, Part 2--Best score is {score_2}')
