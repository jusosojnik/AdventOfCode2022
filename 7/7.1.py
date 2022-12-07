part1 = []
part2 = []
tree = []
_dir = '/'
space_to_free_up = 0

def size_tree(tree, treshold, required_size, total_size):
    global space_to_free_up, part1, part2
    folder_size = 0
    folder_name = "/"
    for e in tree:
        if isinstance(e, list):
            folder_size += size_tree(e, treshold, required_size, total_size)
        elif len(e.split(" ")) != 1:
            folder_size += int(e.split(" ")[0])
        else:
            folder_name = e
    if folder_size <= treshold:
        part1.append(folder_size)
    part2.append(folder_size)
    if folder_name == '/':
        unused_space = total_size - folder_size
        space_to_free_up = required_size - unused_space
    return folder_size

with open('input.txt', 'r') as file:
    Lines = file.readlines()
    for line in Lines:
        line = line.replace("\n", "")
        if line[0] == "$":
            if line == "$ cd /":
                _dir = '/'
            elif line == "$ cd ..":
                _dir = _dir[:_dir[:-1].rfind('/')] + '/'
            elif line.split(' ')[1] == "cd":
                _dir += line.split(' ')[2] + "/"
        else:
            if line.split(' ')[0] == "dir":
                if _dir == '/':
                    tree.append([line.split(' ')[1]])
                else:
                    path = []
                    curr = tree
                    for c in _dir.replace('/', ' ')[1:-1].split(" "):
                        for i, e in enumerate(curr):
                            if e[0] == c:
                                path.append(i)
                                curr = e
                                break
                    curr = tree
                    for p in path:
                        curr = curr[p]
                    curr.append([line.split(' ')[1]])
            else:
                if _dir == '/':
                    tree.append(line)
                else:
                    path = []
                    curr = tree
                    for c in _dir.replace('/', ' ')[1:-1].split(" "):
                        for i, e in enumerate(curr):
                            if e[0] == c:
                                path.append(i)
                                curr = e
                                break
                    curr = tree
                    for p in path:
                        curr = curr[p]
                    curr.append(line)

size_tree(tree, 100000, 30000000, 70000000)
part2.sort()
part2 = list(filter(lambda x : x >= space_to_free_up, part2))

print(f"Part1: {sum(part1)}")
print(f"Part2: {min(part2)}")