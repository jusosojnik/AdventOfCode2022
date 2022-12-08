forest = []

with open('input.txt', 'r') as file:
    Lines = file.readlines()
    for line in Lines:
        line = line.replace("\n", "")
        forest.append([int(x) for x in line])

part1 = 0
visible = []

part1 += 2 * (len(forest) + len(forest[0]) - 2)

# TOP
for i in range(1, len(forest[0]) - 1):
    max_h = 0
    for j in range(len(forest)):
        if forest[j][i] > max_h:
            max_h = forest[j][i]
            if j != 0 and j != len(forest) - 1:
                if [j, i] not in visible:
                    visible.append([j, i])
                    part1 += 1

# BOTTOM
for i in range(1, len(forest[0]) - 1):
    max_h = 0
    for j in range(len(forest)):
        if forest[len(forest)-1-j][i] > max_h:
            max_h = forest[len(forest)-1-j][i]
            if len(forest)-1-j != 0 and len(forest)-1-j != len(forest) - 1 and [len(forest)-1-j, i] not in visible:
                visible.append([len(forest)-1-j, i])
                part1 += 1


# LEFT
for i in range(1, len(forest) - 1):
    max_h = 0
    for j in range(len(forest[0])):
        if forest[i][j] > max_h:
            max_h = forest[i][j]
            if j != 0 and j != len(forest[0]) - 1 and [i, j] not in visible:
                visible.append([i, j])
                part1 += 1

# RIGHT
for i in range(1, len(forest) - 1):
    max_h = 0
    for j in range(len(forest[0])):
        if forest[i][len(forest[0])-1-j] > max_h:
            max_h = forest[i][len(forest[0])-1-j]
            if len(forest[0])-1-j != 0 and len(forest[0])-1-j != len(forest[0]) - 1 and [i, len(forest[0])-1-j] not in visible:
                visible.append([i, len(forest[0])-1-j])
                part1 += 1

part2 = 0

for i in range(1, len(forest)-1):
    for j in range(1, len(forest[0]) - 1):
        product = 1
        # UP
        c = 0
        for k in range(i):
            c += 1
            if forest[i - 1 - k][j] >= forest[i][j]:
                break
        product *= c
        # DOWN
        c = 0
        for k in range(i + 1, len(forest)):
            c += 1
            if forest[k][j] >= forest[i][j]:
                break
        product *= c
        # LEFT
        c = 0
        for k in range(j):
            c += 1
            if forest[i][j - 1 - k] >= forest[i][j]:
                break
        product *= c
        # RIGHT
        c = 0
        for k in range(j + 1, len(forest[0])):
            c += 1
            if forest[i][k] >= forest[i][j]:
                break
        product *= c

        if product > part2:
            part2 = product

print(f"Part1: {part1}")
print(f"Part2: {part2}")