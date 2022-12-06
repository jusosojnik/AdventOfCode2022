part1 = 0
part2 = 0
with open('input.txt', 'r') as file:
    Lines = file.readlines()
    intersection2 = Lines[0].split("\n")[0]
    for i, line in enumerate(Lines):
        rucksack = line.split("\n")[0]
        comp1 = rucksack[:int(len(rucksack)/2)]
        comp2 = rucksack[int(len(rucksack)/2):]
        intersection1 = list(set(comp1).intersection(comp2))[0]
        part1 += ord(intersection1) - 38 if intersection1.isupper() else ord(intersection1) - 96
        intersection2 = list(set(intersection2).intersection(rucksack))
        if (i + 1) % 3 == 0:
            part2 += ord(intersection2[0]) - 38 if intersection2[0].isupper() else ord(intersection2[0]) - 96
            if i + 1 != len(Lines):
               intersection2 = Lines[i + 1].split("\n")[0]

print(f"Part1: {part1}")
print(f"Part2: {part2}")
        