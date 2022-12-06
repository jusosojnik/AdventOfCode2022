stacks1 = []
stacks2 = []
with open('input.txt', 'r') as file:
    Lines = file.readlines()
    stack_read = False
    lines_t = []
    for line in Lines:
        if not stack_read:
            if line == '\n':
                stack_read = True
                lines_t.pop()
                stacks1 = [[] for x in range(len(lines_t[0]))]
                stacks2 = [[] for x in range(len(lines_t[0]))]
                for i in range(len(lines_t[0])):
                    for line_t in lines_t:
                        if line_t[i] != '0':
                            stacks1[i].append(line_t[i])
                            stacks2[i].append(line_t[i])
                    stacks1[i].reverse()
                    stacks2[i].reverse()
                continue
            lines_t.append(line.replace("\n", "").replace("    ", " [0] ").replace(" ", "").replace("[", "").replace("]", ""))
        else:
            move = line.replace("move ", "").replace("from ", "").replace("to ", "").replace("\n", "").split(" ")
            moved1 = stacks1[int(move[1]) - 1][-int(move[0]):]
            moved2 = stacks2[int(move[1]) - 1][-int(move[0]):]
            moved1.reverse()
            del stacks1[int(move[1]) - 1][-int(move[0]):]
            del stacks2[int(move[1]) - 1][-int(move[0]):]
            stacks1[int(move[2]) - 1] += moved1
            stacks2[int(move[2]) - 1] += moved2

print("Part1: ", end="")
for e in stacks1:
    print(e[len(e)-1], end="")
print()
print("Part2: ", end="")
for e in stacks2:
    print(e[len(e)-1], end="")
print()