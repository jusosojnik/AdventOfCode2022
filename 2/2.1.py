legend_part1 = { "AX": 4, "AY" : 8, "AZ" : 3,
                 "BX": 1, "BY" : 5, "BZ" : 9,
                 "CX": 7, "CY" : 2, "CZ" : 6
                }

legend_part2 = { "AX": 3, "AY" : 4, "AZ" : 8,
                 "BX": 1, "BY" : 5, "BZ" : 9,
                 "CX": 2, "CY" : 6, "CZ" : 7
                }

part1 = 0
part2 = 0

with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        moves = line.replace("\n", "").split(" ")
        part1 += legend_part1[moves[0] + moves[1]]
        part2 += legend_part2[moves[0] + moves[1]]

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")