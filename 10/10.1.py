register_x = 1
cycles = 0
part1 = 0
next_signal_at = 20
sprite_position = '###' + ('.' * 37)
pos = 0
CRT = ""
part2 = ""

with open('input.txt', 'r') as file:
    Lines = file.readlines()
    for line in Lines:
        line = line.replace('\n', '').split(" ")
        if line[0] == 'addx':
            for i in range(2):
                cycles += 1
                CRT += '#' if sprite_position[pos] == '#' else '.'
                pos += 1
                if pos == 40:
                    pos = 0 
                    part2 += CRT + '\n'
                    CRT = ""
                if cycles == next_signal_at:
                    part1 += register_x * next_signal_at
                    next_signal_at += 40
            register_x += int(line[1])
            sprite_position = ('.' * (register_x - 1)) + "###" + ('.' * (40 - (register_x - 1 + 3)))

        elif line[0] == 'noop':
            cycles += 1
            CRT += '#' if sprite_position[pos] == '#' else '.'
            pos += 1
            if pos == 40:
                pos = 0
                part2 += CRT + '\n'
                CRT = ""
            if cycles == next_signal_at:
                part1 += register_x * next_signal_at
                next_signal_at += 40

print(f"Part1: {part1}")
print(f"Part2:\n{part2}")
