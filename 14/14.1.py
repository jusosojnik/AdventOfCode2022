import copy

def collision_rock(x, rocks):
    for rock in rocks:
        for i in range(1, len(rock)):
            if x[0] >= int(rock[i].split(',')[0]) and x[0] <= int(rock[i-1].split(',')[0]) or x[0] <= int(rock[i].split(',')[0]) and x[0] >= int(rock[i-1].split(',')[0]):
                if x[1] >= int(rock[i].split(',')[1]) and x[1] <= int(rock[i-1].split(',')[1]) or x[1] <= int(rock[i].split(',')[1]) and x[1] >= int(rock[i-1].split(',')[1]):
                    return True

    return False

def collision(rocks, sand, last_x):
    yheight = 100000
    x = [500, 0]
    for rock in rocks:
        for i in range(1, len(rock)):
            if x[0] >= int(rock[i].split(',')[0]) and x[0] <= int(rock[i-1].split(',')[0]) or x[0] <= int(rock[i].split(',')[0]) and x[0] >= int(rock[i-1].split(',')[0]):
                if int(rock[i].split(',')[1]) < yheight:
                    x[1] = int(rock[i].split(',')[1]) - 1
                    yheight = int(rock[i].split(',')[1])
    fall = 0
    if len(sand) != 0:
        x = copy.deepcopy(last_x)
    else:
        last_x = copy.deepcopy(x)
    while True:
        if fall > 1000:
            return -1, -1
        if len(sand) != 0:
            if x in sand:
                x[1] -= 1
                last_x = copy.deepcopy(x)
                continue
            if not [x[0], x[1] + 1] in sand and not collision_rock([x[0], x[1] + 1], rocks):
                x[1] += 1
                fall += 1
                continue
            elif not [x[0] - 1, x[1] + 1] in sand and not collision_rock([x[0] - 1, x[1] + 1], rocks):
                x[0] -= 1
                x[1] += 1
                continue
            elif not [x[0] + 1, x[1] + 1] in sand and not collision_rock([x[0] + 1, x[1] + 1], rocks):
                x[0] += 1
                x[1] += 1
                continue
        break
    
    return copy.deepcopy(x), last_x


rocks = []

with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        rocks.append(line.replace('\n', '').split(' -> '))

minx = 1000000
maxx = 0

miny = 100000000
maxy = 0

for rock in rocks:
    for r in rock:
        if int(r.split(',')[0]) > maxx:
            maxx = int(r.split(',')[0])
        if int(r.split(',')[0]) < minx:
            minx = int(r.split(',')[0])
        if int(r.split(',')[1]) > maxy:
            maxy = int(r.split(',')[1])
        if int(r.split(',')[1]) < miny:
            miny = int(r.split(',')[1])

minx -= 10
maxx += 10
maxy += 3

grid = [['.' for y in range(minx, maxx)] for x in range(0, maxy)]

for rock in rocks:
    for i in range(1, len(rock)):
        if int(rock[i].split(',')[0]) == int(rock[i - 1].split(',')[0]):
            if int(rock[i].split(',')[1]) < int(rock[i-1].split(',')[1]):
                for j in range(int(rock[i].split(',')[1]), int(rock[i-1].split(',')[1]) + 1):
                    grid[j][int(rock[i].split(',')[0]) - minx] = '#'
            else:
                for j in range(int(rock[i-1].split(',')[1]), int(rock[i].split(',')[1]) + 1):
                    grid[j][int(rock[i].split(',')[0]) - minx] = '#'
        else:
            if int(rock[i].split(',')[0]) < int(rock[i-1].split(',')[0]):
                for j in range(int(rock[i].split(',')[0]), int(rock[i-1].split(',')[0]) + 1):
                    grid[int(rock[i].split(',')[1])][j - minx] = '#'
            else:
                for j in range(int(rock[i-1].split(',')[0]), int(rock[i].split(',')[0]) + 1):
                    grid[int(rock[i].split(',')[1])][j - minx] = '#'

grid[0][500 - minx] = '+'

sand = []

x = [500, 0]
last_x = [500, 0]

part1 = 0
while True:
    nx, last_x = collision(rocks, copy.deepcopy(sand), copy.deepcopy(last_x))
    if nx != -1:
        sand.append(nx)
    else:
        break
    part1 += 1
    for grain in sand:
        grid[grain[1]][grain[0] - minx] = 'o'

print(f"Part1: {part1}")
for row in grid:
    for col in row:
        print(col, end="")
    print()

rocks.append(['-100000,'+str(maxy-1), '100000,'+str(maxy-1)])
grid[maxy-1] = ['#' for x in range(minx, maxx)]

x = [500, 0]
last_x = [500, 0]

part2 = 0
sand = []
while True:
    nx, last_x = collision(rocks, copy.deepcopy(sand), copy.deepcopy(last_x))
    if nx != -1:
        sand.append(nx)
    else:
        break
    part2 += 1
    for grain in sand:
        try:
            grid[grain[1]][grain[0] - minx] = 'o'
        except:
            pass

    if grid[0][500 - minx] != '+':
        break

print(f"Part2: {part2}")
for row in grid:
    for col in row:
        print(col, end="")
    print()
