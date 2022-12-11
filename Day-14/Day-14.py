# Advent of Code 2015, Day-14
# https://adventofcode.com/2015
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

RACE_DURATION = 2503  # seconds


def part_1(reindeer_stats, duration):
    winner_ = ''
    longest_distance = 0

    for reindeer in reindeer_stats:
        # fly_time = reindeer[2]
        # rest_time = reindeer[3]
        # speed = reindeer[1]
        # name = reindeer[0]
        name, speed, fly_time, rest_time = reindeer
        time_increment = fly_time + rest_time  # at each block of time = fly time + rest time,
        distance_per_increment = speed * fly_time  # each reindeer can travel distance = speed * fly time
        number_time_increment = duration // time_increment  # total whole time increment
        distance_ = number_time_increment * distance_per_increment
        remainder_ = duration % time_increment  # the remainder time segment.
        if remainder_ > fly_time:  # still has some flight time left in the remaining segment
            distance_ += min(remainder_, fly_time) * speed
        # print(f'{name}-->{distance_}')
        if distance_ > longest_distance:
            longest_distance = distance_
            winner_ = name

    return winner_, longest_distance


def part_2(reindeer_stats, duration):
    winner_ = ''
    progress = {}
    for reindeer in reindeer_stats:
        progress.update({reindeer[0]: [0, 0]})  # {Reindeer name: [distance, point]}
    # for reindeer in progress.items():
    #     print(reindeer)
    # for reindeer in progress.keys():
    #     progress[reindeer][0] += 1
    #     progress[reindeer][1] += 2
    # for reindeer in progress.keys():
    #     print(reindeer, progress[reindeer])
    # for reindeer in reindeer_stats:
    #     print(reindeer)
    """
    For each reindeer => cycle_length = fly time at a certain speed + rest time (no speed).
    at_each_sec_of_time % cycle_length yield what part of the cycle it is in.
    If within the fly stage, add the distance travel during that second, else add 0
    """
    for time_increment in range(duration):  # at each 1 sec increment of the total race time
        # cycle thru each reindeer
        best_distance = 0  # best distance at each time increment so far
        for reindeer in reindeer_stats:
            name, speed, fly_time, rest_time = reindeer
            cycle_length = fly_time + rest_time
            which_phase = time_increment % cycle_length  # 0 - cycle_length-1
            if which_phase < fly_time:  # in fly phase
                progress[name][0] += speed  # fly speed in 1 sec
            if best_distance < progress[name][0]:  # who's in the lead
                best_distance = progress[name][0]
        # after cycling thru all the reindeers, determine the points.
        # +1 if at the lead or tie for lead.
        for name in progress.keys():
            distance_ = progress[name][0]
            if distance_ == best_distance:
                progress[name][1] += 1
    # Check scores, who won?
    best_score = 0
    for name in progress.keys():
        score = progress[name][1]
        if best_score <= score:
            best_score = score
            winner_ = name

    return winner_, best_score


if __name__ == '__main__':
    reindeer_table = []
    # race_duration = 2503
    with open('Day-14-data.txt', 'r') as f:
        input_line = f.readlines()
    for i in input_line:
        i = i.strip().lstrip().split()
        reindeer_table.append([i[0], int(i[3]), int(i[6]), int(i[-2])])

    winner, distance = part_1(reindeer_table, RACE_DURATION)
    print(f'Day 14, Part 1--At the end of {RACE_DURATION} seconds, {winner} has travelled {distance} km')

    winner, score = part_2(reindeer_table, RACE_DURATION)

    print(f'Day 14, Part 2--At the end of {RACE_DURATION} seconds, {winner} has travelled {score} points')
