import copy

monkeys = {}

with open('input.txt', 'r') as file:
    Lines = file.readlines()
    monkey = None
    monkey_bool = []
    for line in Lines:
        line = line.replace('\n', '')
        if line.split(' ')[0] == 'Monkey':
            monkeys[line] = [0]
            monkey = line
        elif 'Operation' in line:
            monkeys[monkey].append(line.split("= ",1)[1])
        elif 'divisible' in line:
            monkeys[monkey].append([int(x) for x in line.replace(',', '').split(' ') if x.isnumeric()][0])
        elif 'Starting' in line:
            monkeys[monkey].append([int(x) for x in line.replace(',', '').split(' ') if x.isnumeric()])
        elif 'throw' in line:
            monkey_bool.append([int(x) for x in line.replace(',', '').split(' ') if x.isnumeric()][0])
            if len(monkey_bool) == 2:
                monkeys[monkey].append(monkey_bool)
                monkey_bool = []

def monkey_play(rounds, devide_by_3, monkeys):
    round = 0
    devider = 1
    for x in monkeys:
        devider *= monkeys[x][3]

    while round < rounds:
        for x in monkeys:
            for item in copy.deepcopy(monkeys[x][1]):
                monkeys[x][0] += 1
                worry_level = item
                if monkeys[x][2].split(" ")[1] == '+':
                    if monkeys[x][2].split(" ")[2] == 'old':
                        worry_level += item
                    else:
                        worry_level += int(monkeys[x][2].split(" ")[2])
                elif monkeys[x][2].split(" ")[1] == '*':
                    if monkeys[x][2].split(" ")[2] == 'old':
                        worry_level *= item
                    else:
                        worry_level *= int(monkeys[x][2].split(" ")[2])
                monkeys[x][1].pop(0)
                if devide_by_3:
                    worry_level //= 3
                else:
                    worry_level %= devider
                if worry_level % monkeys[x][3] == 0:
                    monkeys[f'Monkey {monkeys[x][4][0]}:'][1].append(worry_level)
                else:
                    monkeys[f'Monkey {monkeys[x][4][1]}:'][1].append(worry_level)
        round += 1

    monkey_lst = [(value, key) for key, value in monkeys.items()]
    monkey_lst.sort(key=lambda x : x[0][0], reverse=True)
    return(monkey_lst[0][0][0] * monkey_lst[1][0][0])

print(f'Part1 {monkey_play(20, True, copy.deepcopy(monkeys))}')
print(f'Part2 {monkey_play(10000, False, copy.deepcopy(monkeys))}')
