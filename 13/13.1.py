import json, copy

def list_compare(x, y):
    correct_order = True
    for i in range(len(x)):
        try:
            if isinstance(x[i], int):
                if isinstance(y[i], int):
                    if x[i] > y[i]:
                        correct_order = False
                        break
                    elif x[i] < y[i]:
                        break
                    else:
                        continue
                else:
                    x[i] = [x[i]]
                    if x[i] == y[i]:
                        continue
                    correct_order = list_compare(x[i], y[i])
                    break
            else:
                if not isinstance(y[i], list):
                    y[i] = [y[i]]
                if x[i] == y[i]:
                    continue
                correct_order = list_compare(x[i], y[i])
                break
        except:
            correct_order = False
            break
    return correct_order

pairs =[]
signals = [[[2]], [[6]]]

with open('input.txt', 'r') as file:
    lines = file.readlines()
    pair = []
    for line in lines:
        line = line.replace('\n', '')
        if line == '':
            pairs.append(pair)
            pair = []
            continue
        line = json.loads(line)
        pair.append(line)
        signals.append(line)
    pairs.append(pair)


part1 = 0
for i, pair in enumerate(pairs):
    if list_compare(copy.deepcopy(pair[0]),copy.deepcopy(pair[1])):
        part1 += i + 1

for i in range(len(signals)-1):  
    for j in range(0, len(signals)-i-1):
        if list_compare(copy.deepcopy(signals[j+1]), copy.deepcopy(signals[j])):  
            tmp = copy.deepcopy(signals[j])  
            signals[j] = copy.deepcopy(signals[j+1])
            signals[j+1] = tmp  

print(f"Part1: {part1}")
print(f"Part2: {(signals.index([[2]]) + 1) * (signals.index([[6]]) + 1)}")
