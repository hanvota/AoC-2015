# Advent of Code 2015, Day-21
# https://adventofcode.com/2015
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from itertools import combinations

# Weapons: Cost  Damage  Armor
weapons = {
    'Dagger': [8, 4, 0],
    'Shortsword': [10, 5, 0],
    'Warhammer': [25, 6, 0],
    'Longsword': [40, 7, 0],
    'Greataxe': [74, 8, 0]
}
# Armors:       Cost  Damage  Armor
armors = {
    'No armor': [0, 0, 0],
    'Leather': [13, 0, 1],
    'Chainmail': [31, 0, 2],
    'Splintmail': [53, 0, 3],
    'Bandedmail': [75, 0, 4],
    'Platemail': [102, 0, 5]
}
# Rings:        Cost  Damage  Armor
rings = {
    'No ring l': [0, 0, 0],
    'No ring r': [0, 0, 0],
    'Damage + 1': [25, 1, 0],
    'Damage + 2': [50, 2, 0],
    'Damage + 3': [100, 3, 0],
    'Defense + 1': [20, 0, 1],
    'Defense + 2': [40, 0, 2],
    'Defense + 3': [80, 0, 3]
}


class Player:
    def __init__(self, name, hp, damage, armor):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.armor = armor

    def __str__(self):
        return f'{self.name}, HP={self.hp}, Damage={self.damage}, Armor={self.armor}'


# def attack(attacker, defender):
#     # passing in both attacker and defender.
#     # returns both attacker and defender even though only defender stat (hp) is affected.
#     # attacker's stat is unchanged for this game now, but in case the attacker is also affected, I will return both.
#
#     points = attacker.damage - defender.armor
#     points = max(points, 1)
#     defender.hp -= points
#
#     return attacker, defender


def battle(p1, p2):  # Battles between p1 and p2 and returns winner
    # print(f'{p1} ---- {p2}')

    while True:  # attacks back and forth, starting with p1 attacks p2 until someone wins (the opponent) hp <= 0.
        # p1 attacks p2 first.
        # p1, p2 = attack(p1, p2)
        points = max(p1.damage - p2.armor, 1)
        p2.hp -= points
        if p2.hp <= 0:
            return p1

        # p2 attacks p1.
        # p1, p2 = attack(p2, p1)
        points = max(p2.damage - p1.armor, 1)
        p1.hp -= points
        if p1.hp <= 0:
            return p2


def equipments_stats(w, a, l_r, r_r):
    total_cost = weapons[w][0] + armors[a][0] + rings[l_r][0] + rings[r_r][0]
    total_damage = weapons[w][1] + armors[a][1] + rings[l_r][1] + rings[r_r][1]
    total_armor = weapons[w][2] + armors[a][2] + rings[l_r][2] + rings[r_r][2]

    return total_cost, total_damage, total_armor


def play_part_1(p1, p2):
    minimum_cost = 9999999999
    maximum_cost = -9999999999
    # trying different equipment loads for player (p1) and do battle against p2 (boss)
    # 1 weapon
    # 0 or 1 armor
    # 0 - 2 ring (only 1 of each, no duplicate
    for w in weapons:
        for a in armors:
            for ring_combo in combinations(rings.keys(), 2):
                l_r, r_r = ring_combo
                # if l_r == r_r:        # no duplicate rings
                #   print(f'Duplicate rings {l_r}, {r_r}, --skip')
                #   continue
                cost, damage, armor = equipments_stats(w, a, l_r, r_r)
                # print(f'{w}, {a}, {l_r}, {r_r}==> Cost ({cost}), Damage ({damage}), Armor ({armor})')
                # p1a represents the effective p1 with stats after the equipments are added.
                p1a = Player(p1.name, hp=p1.hp, damage=p1.damage + damage, armor=p1.armor + armor)

                p2a = Player(p2.name, hp=p2.hp, damage=p2.damage, armor=p2.armor)
                # effective p2. No change in the stats for p2 (Boss).
                winner = battle(p1a, p2a)
                if winner.name == p1.name:
                    print(f'I won with--> {w}, {a}, {l_r}, {r_r}, cost {cost} minimum {minimum_cost}')
                    minimum_cost = min(minimum_cost, cost)
                if winner.name == p2.name:
                    maximum_cost = max(maximum_cost, cost)

    return minimum_cost, maximum_cost


def get_input():
    with open('Day-21-data.txt', 'r') as f:
        input_data = f.readlines()
    hp_ = damage_ = armor_ = 0
    for input_line in input_data:
        n, s = input_line.strip().split(':')
        # print(f'{n},{int(s)}')
        if n == "Hit Points":
            hp_ = int(s)
        elif n == "Damage":
            damage_ = int(s)
        elif n == "Armor":
            armor_ = int(s)

    return hp_, damage_, armor_


if __name__ == '__main__':
    t = get_input()
    me = Player("Me", hp=100, damage=0, armor=0)

    boss = Player("Boss", hp=t[0], damage=t[1], armor=t[2])

    cost_to_play_part_1, cost_to_play_part_2 = play_part_1(me, boss)
    print(f'Day 21, Part 1--You need to spend at least {cost_to_play_part_1} gold to win.')
    print(f'Day 21, Part 2--You can spend as much as {cost_to_play_part_2} gold and still lose.')
