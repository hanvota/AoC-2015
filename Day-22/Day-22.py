# Advent of Code 2015, Day-22
# https://adventofcode.com/2015
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import copy
import random

# Magics:   Name        Cost  Damage  Armor  Heal/HP   Recharge   Timer  Mana Effect

spells = {
    'Magic Missile': [53, 4, 0, 0, 0, 0, 0],
    'Drain': [73, 2, 0, 2, 0, 0, 0],
    'Shield': [113, 0, 7, 0, 0, 0, 6],
    'Poison': [173, 3, 0, 0, 0, 0, 6],
    'Recharge': [229, 0, 0, 0, 101, 0, 5]
}
all_spells_list = ('Magic Missile', 'Drain', 'Shield', 'Poison', 'Recharge')
instant_spells = ('Magic Missile', 'Drain')
effect_spells = ('Shield', 'Poison', 'Recharge')
COST = 0
DAMAGE = 1
ARMOR = 2
HEAL = 3
RECHARGE = 4
TIMER = 5
EFFECT = 6

GAMES_TO_PLAY = 150000
SPELLS_PER_BATTLE = 10


class Player:
    def __init__(self, name, hp, mana, damage, armor):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.damage = damage
        self.armor = armor

    def __str__(self):
        return f'{self.name}, HP={self.hp}, Mana={self.mana}, Damage={self.damage}, Armor={self.armor}'


def get_input():
    with open('Day-22-data.txt', 'r') as f:
        input_data = f.readlines()
    hp_ = damage_ = armor_ = 0
    for input_line in input_data:
        n, s = input_line.strip().split(':')
        if n == "Hit Points":
            hp_ = int(s)
        elif n == "Damage":
            damage_ = int(s)
        # elif n == "Armor":
        #     armor_ = int(s)

    return hp_, damage_


def generate_spell_sequence():
    spell_list = ()
    for _ in range(SPELLS_PER_BATTLE):
        spell = random.choice(all_spells_list)
        spell_list += (spell,)
    return spell_list


def battle(p1a, p2a, max_cost, spell_list):  # a round of battle
    turn = 0
    spells_used = ()
    cost = 0
    winner = {}

    def spell_effect():  # handle the effect of the effect spells
        for s in effect_spells:
            if spells[s][TIMER]:
                spells[s][TIMER] -= 1
                p2a.hp -= spells[s][DAMAGE]  # Do spell effect (Poison)
                p1a.armor = 0 if spells['Shield'][TIMER] == 0 else spells['Shield'][ARMOR]
                p1a.mana += spells[s][RECHARGE]  # (Recharge)

    def cast_spell(spell):  # cast the spell selected.
        nonlocal cost
        p1a.mana -= spells[spell][COST]
        cost += spells[spell][COST]
        if spell in instant_spells:
            p2a.hp -= spells[spell][DAMAGE]
            p1a.hp += spells[spell][HEAL]
        else:
            # p1a.armor = spells[spell][ARMOR]
            p1a.armor = 0 if spells['Shield'][TIMER] == 0 else spells['Shield'][ARMOR]
            spells[spell][TIMER] = spells[spell][EFFECT]  # timer for this spell is now active

    def valid_spell(spell):  # is this a valid spell that p1a can cast at this time?
        if p1a.mana < spells[spell][COST]:  # not enough mana
            return False
        if spell in effect_spells and spells[spell][TIMER]:  # cast same spell that is currently in effect.
            return False
        return True

    while not winner and len(spell_list):
        if cost > max_cost:  # if you already spend more than you started with, it's a lost
            winner = p2a
            break
        turn += 1  # p1a --> p2a    (Player's turn)
        spell_effect()  # spell effect
        spell = spell_list[0]  # select spell
        if not valid_spell(spell):
            winner = p2a
            break
        cast_spell(spell)
        spells_used += (spell,)  # add to the list of spells used in this battle
        spell_list = spell_list[1:]  # Take spell used off the list

        turn += 1  # p2a --> p1a    (Boss' turn)
        spell_effect()  # spell effect
        if p2a.hp <= 0:  # if p2.hp <= 0 then p1 wins
            winner = p1a
            break
        p1a.hp -= max(p2a.damage - p1a.armor, 1)  # damage to p1, minimum of 1 point damage
        if p1a.hp <= 0:  # if p1.hp <= 0 then p2 wins
            winner = p2a

    return winner, cost


def play_game(p1, p2):  # play through many games and find the best outcome. Part 1= least mana needed to win.
    # test data set 1 for testing
    # spell_list = ('Poison', 'Magic Missile')  # test--list of spells to use
    # p1.hp = 10
    # p1.mana = 250
    # p2.hp = 13
    # p2.damage = 8

    # test data set 2 for testing
    # spell_list = ('Recharge', 'Shield', 'Drain', 'Poison', 'Magic Missile')  # test--list of spells to use
    # p1.hp = 10
    # p1.mana = 250
    # p2.hp = 14
    # p2.damage = 8

    # end of test data

    best_cost_1 = 999999999
    best_cost_2 = 999999999
    best_cost_count = 0
    spell_list = ()
    sequences_tried = []

    for b in range(GAMES_TO_PLAY):
        found_unique = False
        while not found_unique:
            spell_list = generate_spell_sequence()
            if spell_list not in sequences_tried:
                found_unique = True

        # if b % 100:
        #     print(f'Battle {b} with {spell_list}')

        # copy of player and boss for each battle.
        p1a = copy.deepcopy(p1)
        p2a = copy.deepcopy(p2)
        # reset all the effect spell timers
        for i in effect_spells:
            spells[i][TIMER] = 0

        winner, cost_for_this_game = battle(p1a, p2a, p1.mana,
                                            spell_list)  # Fight a battle with the player's sequence of spells.
        # print(winner)
        sequences_tried.append(spell_list)

        if not winner:
            print(f'NO winner for this battle {spell_list}')
            continue

        if winner.name == 'Me':
            # cost_for_this_game = p1.mana - winner.mana
            if cost_for_this_game > p1.mana:  # cost more that what we started using recharge spell, don't count
                continue
            if cost_for_this_game < 0:
                print('Neg mana')
            elif cost_for_this_game == best_cost_1:
                best_cost_count += 1
                if best_cost_count > 10:
                    print('Best score unchanged for at least 10 tries')
                    break
            elif cost_for_this_game < best_cost_1:  # found new best score
                best_cost_1 = min(best_cost_1, cost_for_this_game)
                print(f'-->I won. {cost_for_this_game} Mana used. Best = {best_cost_1}')
                best_cost_count = 0
            else:
                continue

    return best_cost_1, best_cost_2


if __name__ == '__main__':
    t = get_input()  # read in stats for boss
    # create player and boss
    me = Player("Me", hp=50, mana=500, damage=0, armor=0)
    boss = Player("Boss", hp=t[0], mana=0, damage=t[1], armor=0)

    # me = Player("Me", hp=10, mana=250, damage=0, armor=0)
    # boss = Player("Boss", hp=13, mana=0, damage=8, armor=0)

    cost_to_play_part_1, cost_to_play_part_2 = play_game(me, boss)
    print(f'Day 22, Part 1--You need to spend at least {cost_to_play_part_1} gold to win.')
    # print(f'Day 22, Part 2--You can spend as much as {cost_to_play_part_2} gold and still lose.')

# Part 1: 1824
# Part 2: 1937
