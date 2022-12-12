import copy

rows = []
start = []
end = []
lowest_starting_points = []
with open('input.txt', 'r') as file:
    Lines = file.readlines()
    for i, line in enumerate(Lines):
        if 'S' in line:
            start = [i, line.index('S')]
            line = line.replace('S', 'a')
        if 'E' in line:
            end = [i, line.index('E')]
            line = line.replace('E', 'z')
        lowest_starting_points += [[i,x] for x, ltr in enumerate(line) if ltr =='a']
        rows.append(line.replace('\n', ''))

def bfs(graph, start, end):
    visited = []
    queue = []
    visited.append(start)
    queue.append([start, 0])

    move_v = [1, -1, 0, 0]
    move_h = [0, 0, 1, -1] 

    while queue:
        next_node = queue.pop(0)
        s = next_node[0]
        d = next_node[1]

        for i in range(4):
            neighbour = [s[0] + move_h[i], s[1] + move_v[i]]
            if neighbour not in visited:
                if neighbour[0] >= 0 and neighbour[0] < len(graph) and neighbour[1] >= 0 and neighbour[1] < len(graph[0]):
                    if ord(graph[neighbour[0]][neighbour[1]]) <= ord(graph[s[0]][s[1]]) or ord(graph[neighbour[0]][neighbour[1]]) -1 == ord(graph[s[0]][s[1]]):
                        if neighbour == end:
                            return d + 1
                        visited.append(neighbour)
                        queue.append([neighbour, d + 1])
    return -1

part2 = [bfs(rows, x, end) for x in lowest_starting_points]
part2 = [x for x in part2 if x != -1]

print(f'Part1: {bfs(rows, start, end)}')
print(f'Part2: {min(part2)}')