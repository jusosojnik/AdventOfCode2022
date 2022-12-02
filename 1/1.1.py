elves = []

with open('input.txt', 'r') as file:
    Lines = file.readlines()
    cals = 0
    for line in Lines:
        if line == "\n":
            elves.append(cals)
            cals = 0
        else:
            cals += int(line)

    elves.append(cals)

part1 = max(elves)
elves.sort()
part2 = sum(elves[-3:])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")