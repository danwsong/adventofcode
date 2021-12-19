scanner_inputs = open('input.txt').read().split('\n\n')

scanners = []
for scanner_input in scanner_inputs:
    scanner = set()
    for beacon_input in scanner_input.split('\n')[1:]:
        scanner.add(tuple(map(lambda x: int(x), beacon_input.split(','))))
    scanners.append(scanner)

# def gen_x_rotations(point):
#     x, y, z = point
#     return [(x, y, z), (x, z, -y), (x, -y, -z), (x, -z, y)]

# def gen_y_rotations(point):
#     x, y, z = point
#     return [(x, y, z), (z, y, -x), (-x, y, -z), (-z, y, x)]

# def gen_z_rotations(point):
#     x, y, z = point
#     return [(x, y, z), (y, -x, z), (-x, -y, z), (-y, x, z)]

# def gen_rotations(point):
#     rotations = set()
#     for x_rotation in gen_x_rotations(point):
#         for y_rotation in gen_y_rotations(x_rotation):
#             for z_rotation in gen_z_rotations(y_rotation):
#                 rotations.add(z_rotation)
#     return rotations

# print(str(sorted(list(gen_rotations((1, 2, 3))), key=lambda x: abs(x[0]) * 9 + (1 if x[0] < 0 else 0) * 108 + abs(x[1]) * 3 + (1 if x[1] < 0 else 0) * 54 + abs(x[2]) + (1 if x[2] < 0 else 0) * 27)).replace('1', 'x').replace('2', 'y').replace('3', 'z'))

def gen_rotations(point):
    x, y, z = point
    return [(x, y, z), (y, z, x), (z, x, y), (x, z, -y), (y, x, -z), (z, y, -x), (x, -z, y), (y, -x, z), (z, -y, x), (x, -y, -z), (y, -z, -x), (z, -x, -y), (-x, z, y), (-y, x, z), (-z, y, x), (-x, y, -z), (-y, z, -x), (-z, x, -y), (-x, -y, z), (-y, -z, x), (-z, -x, y), (-x, -z, -y), (-y, -x, -z), (-z, -y, -x)]

import operator
import collections

unvisited = set(i for i in range(1, len(scanners)))
queue = collections.deque()

queue.append(0)

def scanner_overlap(scanner_i, scanner_j):
    for beacon_i in scanner_i:
        rotated_scanner_j = [gen_rotations(beacon) for beacon in scanner_j]
        for rotation_index in range(24):
            rotated_beacons_j = set(beacons[rotation_index] for beacons in rotated_scanner_j)
            for rotated_beacon_j in rotated_beacons_j:
                offset = tuple(map(operator.sub, rotated_beacon_j, beacon_i))
                same_beacons = 0
                for beacon in scanner_i:
                    offset_beacon = tuple(map(operator.add, beacon, offset))
                    if offset_beacon in rotated_beacons_j:
                        same_beacons += 1
                if same_beacons >= 12:
                    return True, rotated_beacons_j, offset
    return False, None, None

scanner_mapping = {0: (0, (0, 0, 0))}
while queue:
    i = queue.popleft()
    scanner_i = scanners[i]
    overlapped = []
    for j in unvisited:
        scanner_j = scanners[j]
        overlap, rotated, offset = scanner_overlap(scanner_i, scanner_j)
        if overlap:
            scanners[j] = rotated
            overlapped.append(j)
            scanner_mapping[j] = (i, offset)
            queue.append(j)
    for scanner in overlapped:
        unvisited.remove(scanner)

offsets = []
for i, scanner in enumerate(scanners):
    base_scanner, offset = scanner_mapping[i]
    while base_scanner != 0:
        base_scanner, next_offset = scanner_mapping[base_scanner]
        offset = tuple(map(operator.add, offset, next_offset))
    offsets.append(offset)

max_dist = 0
for offset_i in offsets:
    for offset_j in offsets:
        max_dist = max(max_dist, sum(map(abs, map(operator.sub, offset_i, offset_j))))
print(max_dist)
