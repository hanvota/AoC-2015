from itertools import combinations

inp = list(map(int, open("Day-17-data.txt").read().splitlines()))

q1 = 0
q2 = 0
# print(len(inp),inp)
for i in range(len(inp) - 1):
    # print(f'{len(inp)}, taken {i} at a time.--{math.comb(len(inp), i)}')
    for perm in combinations(inp, i):
        if sum(perm) == 150:
            q1 += 1
            # print(perm)

    if q1 and not q2:
        q2 = q1

print("Q1: {0}\nQ2: {1}".format(q1, q2))
