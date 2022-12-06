part1 = 0
part2 = 0
with open('input.txt', 'r') as file:
    Lines = file.readlines()
    for i, line in enumerate(Lines):
        line = line.replace("\n", "")
        pairs = line.split(',')
        pairs.sort(key=lambda x: int(x.split('-')[1]), reverse=True)
        pairs.sort(key=lambda x: int(x.split('-')[0]))
        if int(pairs[1].split('-')[0]) >= int(pairs[0].split('-')[0]) and int(pairs[1].split('-')[0]) <= int(pairs[0].split('-')[1]):
            if int(pairs[1].split('-')[1]) <= int(pairs[0].split('-')[1]):
                part1 += 1
            part2 += 1

print(f"Part1: {part1}")
print(f"Part2: {part2}")
