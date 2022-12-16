lines = open('input.txt', 'r').readlines()
data = list(map(lambda x: [[int(x.split(' ')[2][2:-1]),int(x.split(' ')[3][2:-1])],[int(x.split(' ')[8][2:-1]),int(x.replace('\n', '').split(' ')[9][2:])]], lines))

beacons = []
row = []
y = 2000000

for sb in data:
    sb.append(abs(sb[0][0]-sb[1][0])+abs(sb[0][1]-sb[1][1]))
    if sb[1][1] == y:
        if sb[1][0] not in beacons:
            beacons.append(sb[1][0])

for sb in data:
    if sb[0][1] <= y + sb[2] and sb[0][1] >= y or sb[0][1] >= y - sb[2] and sb[0][1] <= y:
        r = sb[2] - abs(y - sb[0][1])
        row += [x for x in range(sb[0][0] - r, sb[0][0] + r + 1) if x not in beacons]

part1 = len(set(row))

min = 0
max = 4000000

row_index = None
part2 = None

for i in range(max + 1):
    row_range = []
    for sb in data:
        if sb[0][1] <= i + sb[2] and sb[0][1] >= i or sb[0][1] >= i - sb[2] and sb[0][1] <= i:
            dist = sb[2] - abs(sb[0][1] - i)
            span = [(sb[0][0] - dist if sb[0][0] - dist >= min else 0), (sb[0][0] + dist if sb[0][0] + dist <= max else max)]
            row_range.append(span)

    row_range.sort(key=lambda x: x[1])
    row_range.sort(key=lambda x: x[0])

    final_span = [row_range[0][0], row_range[0][1]]
    for j in range(1, len(row_range)):
        if final_span[1] + 1 >= row_range[j][0]:
            if row_range[j][1] > final_span[1]:
                final_span[1] = row_range[j][1]

    if final_span[0] != min or final_span[1] != max:
        part2 = (final_span[1] + 1) * 4000000 + i
        break

print(f"Part1: {part1}")
print(f"Part1: {part2}")