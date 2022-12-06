part1 = 4
part2 = 14
with open('input.txt', 'r') as file:
    text = file.read()
    j = 13
    part1_check = False
    part2_check = False
    for i in range(3, len(text)):
        if not part2_check and len(set(text[j-13:j + 1])) == len(text[j-13:j + 1]):
            part2 = j + 1
            part2_check = True
        if not part1_check and len(set(text[i-3:i + 1])) == len(text[i-3:i + 1]):
            part1 = i + 1
            part1_check = True
        j += 1
        if part2_check and part1_check:
            break

print(f"Part1: {part1}")
print(f"Part2: {part2}")