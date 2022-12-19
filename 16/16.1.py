from collections import deque
import time

valves = {}
flow_rates = {}
working_valves = 0

lines = open('input.txt', 'r').read().splitlines()

for line in lines:
    line = line.replace('=', ' ').replace(',', '').replace(';', '').split()

    flow_rates[line[1]] = int(line[5])
    valves[line[1]] = line[10:]

    if int(line[5]) != 0:
        working_valves += 1


def bfs_part1(flow_rates, valves):
    queue = deque([(0, (), "AA", 0)])
    visited = set()
    water_pressure = 0
    
    while queue:
        minutes, opened_valves, valve_name, total_pressure = queue.popleft()
        
        if minutes == 30:
            water_pressure = max(water_pressure,total_pressure)
            continue

        if (opened_valves, valve_name) in visited:
            continue

        visited.add((opened_valves,valve_name))

        new_total_pressure = total_pressure

        for i in opened_valves:
            new_total_pressure += flow_rates[i]

        if flow_rates[valve_name] != 0:
            if valve_name not in opened_valves:
                queue.append((minutes + 1, tuple(list(opened_valves) + [valve_name]), valve_name, new_total_pressure))

        for i in valves[valve_name]:
            queue.append((minutes + 1, opened_valves, i, new_total_pressure))
    
    return water_pressure


def bfs_part2(flow_rates, valves):
    queue = deque([(0, ((), "AA"), ((), "AA"), 0)])
    visited = set()
    water_pressure = 0
    max_score = 0
    opened_num = 0

    while queue:
        minutes, elff, elephant, total_pressure = queue.popleft()
        elff_opened_valves, elff_valve_name = elff
        elephant_opened_valves, elephant_valve_name = elephant
        
        if minutes == 26:
            water_pressure = max(water_pressure, total_pressure)
            continue

        if ((elff_opened_valves, elff_valve_name), (elephant_opened_valves, elephant_valve_name)) in visited:
            continue

        visited.add(((elff_opened_valves, elff_valve_name), (elephant_opened_valves, elephant_valve_name)))

        new_total_pressure = total_pressure
            
        if len(elff_opened_valves) + len(elephant_opened_valves) == working_valves:
            cppm = 0
            for i in elff_opened_valves:
                cppm += flow_rates[i]
            for i in elephant_opened_valves:
                cppm += flow_rates[i]

            water_pressure = max(water_pressure, (26 - minutes) * cppm + total_pressure)

        if minutes > 10 and total_pressure < (0.9 * max_score): continue
        max_score = max(max_score, total_pressure)

        if minutes > 10 and len(elff_opened_valves) + len(elephant_opened_valves) < opened_num - 2: continue
        opened_num = max(opened_num, len(elff_opened_valves) + len(elephant_opened_valves))

        for i in elff_opened_valves:
            new_total_pressure += flow_rates[i]
        for i in elephant_opened_valves:
            new_total_pressure += flow_rates[i]

        #BOTH
        if elff_valve_name != elephant_valve_name:
            if flow_rates[elff_valve_name] != 0:
                if elff_valve_name not in elff_opened_valves and elff_valve_name not in elephant_opened_valves:
                    if flow_rates[elephant_valve_name] != 0:
                        if elephant_valve_name not in elephant_opened_valves and elephant_valve_name not in elff_opened_valves:
                            queue.append((minutes + 1, (tuple(list(elff_opened_valves) + [elff_valve_name]), elff_valve_name), (tuple(list(elephant_opened_valves) + [elephant_valve_name]), elephant_valve_name), new_total_pressure))

        #ELFF
        for i in valves[elephant_valve_name]:
            if flow_rates[elff_valve_name] != 0:
                if elff_valve_name not in elff_opened_valves and elff_valve_name not in elephant_opened_valves:
                    queue.append((minutes + 1, (tuple(list(elff_opened_valves) + [elff_valve_name]), elff_valve_name), (elephant_opened_valves, i), new_total_pressure))
                    skrat = True
                    continue
            break

        #ELEPHANT
        for i in valves[elff_valve_name]:
            if flow_rates[elephant_valve_name] != 0:
                if elephant_valve_name not in elephant_opened_valves and elephant_valve_name not in elff_opened_valves:
                    queue.append((minutes + 1, (elff_opened_valves, i), (tuple(list(elephant_opened_valves) + [elephant_valve_name]), elephant_valve_name), new_total_pressure))
                    slon = True
                    continue
            break

        #NONE
        for i in valves[elff_valve_name]:
            for j in valves[elephant_valve_name]:
                queue.append((minutes + 1, (elff_opened_valves, i), (elephant_opened_valves, j), new_total_pressure))        
    
    return water_pressure


st = time.time()
print(f'Part1: {bfs_part1(flow_rates, valves)}')
et = time.time()
elapsed_time = et - st
print('Execution time (part1):', elapsed_time, 'seconds')
st = time.time()
print(f'Part2: {bfs_part2(flow_rates, valves)}')
et = time.time()
elapsed_time = et - st
print('Execution time (part2):', elapsed_time, 'seconds')