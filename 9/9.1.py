import copy

part1 = [[0, 0]]
part2 = [[0, 0]]
pos_h = [0, 0]
pos_t = [0, 0]

knots = [[0, 0] for x in range(10-1)]

def is_touching(pos_h, pos_t):
    if pos_t[0] == pos_h[0] + 1 or pos_t[0] == pos_h[0] - 1 or pos_t[0] == pos_h[0]:
        if pos_t[1] == pos_h[1] + 1 or pos_t[1] == pos_h[1] - 1 or pos_t[1] == pos_h[1]:
            return True
    return False


def move_tail(pos_h, pos_t):
    if pos_t[0] == pos_h[0]:
        if pos_t[1] < pos_h[1]:
            pos_t[1] = pos_h[1] - 1
        elif pos_t[1] > pos_h[1]:
            pos_t[1] = pos_h[1] + 1
    elif pos_t[1] == pos_h[1]:
        if pos_t[0] < pos_h[0]:
            pos_t[0] = pos_h[0] - 1
        elif pos_t[0] > pos_h[0]:
            pos_t[0] = pos_h[0] + 1
    else:
        if abs(pos_h[1] - pos_t[1]) < abs(pos_h[0] - pos_t[0]):
            pos_t[1] = pos_h[1]
            if pos_t[0] < pos_h[0]:
                pos_t[0] = pos_h[0] - 1
            elif pos_t[0] > pos_h[0]:
                pos_t[0] = pos_h[0] + 1
        elif abs(pos_h[1] - pos_t[1]) > abs(pos_h[0] - pos_t[0]):
            pos_t[0] = pos_h[0]
            if pos_t[1] < pos_h[1]:
                pos_t[1] = pos_h[1] - 1
            elif pos_t[1] > pos_h[1]:
                pos_t[1] = pos_h[1] + 1
        else:
            if pos_t[0] < pos_h[0]:
                pos_t[0] = pos_h[0] - 1
            elif pos_t[0] > pos_h[0]:
                pos_t[0] = pos_h[0] + 1
            if pos_t[1] < pos_h[1]:
                pos_t[1] = pos_h[1] - 1
            elif pos_t[1] > pos_h[1]:
                pos_t[1] = pos_h[1] + 1
    
    return pos_t

def process_knots():
    global part1, part2, knots, pos_h, pos_t
    if not is_touching(pos_h, pos_t):
        pos_t = move_tail(pos_h, pos_t)
        if pos_t not in part1:
            part1.append(copy.deepcopy(pos_t))
        knots[0] = copy.deepcopy(pos_t)
    for j in range(1, len(knots)):
        if not is_touching(knots[j-1], knots[j]):
            knots[j] = move_tail(knots[j-1], knots[j])
    if knots[-1] not in part2:
        part2.append(copy.deepcopy(knots[-1]))

with open('input.txt') as file:
    Lines = file.readlines()
    for line in Lines:
        line = line.replace("\n", "").split(' ')
        if line[0] == 'R':
            for i in range(int(line[1])):
                pos_h[1] += 1
                process_knots()
        elif line[0] == 'L':
            for i in range(int(line[1])):
                pos_h[1] -= 1
                process_knots()
        elif line[0] == 'U':
            for i in range(int(line[1])):
                pos_h[0] += 1
                process_knots()
        elif line[0] == 'D':
            for i in range(int(line[1])):
                pos_h[0] -= 1
                process_knots()

print(f"Part1: {len(part1)}")
print(f"Part2: {len(part2)}")