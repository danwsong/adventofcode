import math

lines = open('input.txt').read().split('\n')

nr = len(lines)
nc = len(lines[0])

src = (0, 0)

distance = {}
vertices = set()
for r in range(nr):
    for c in range(nc):
        if (r, c) != src:
            distance[(r, c)] = math.inf
            vertices.add((r, c))

distance[src] = 0
vertices.add(src)

while vertices:
    cur = min(vertices, key=lambda x: distance[x])
    vertices.remove(cur)
    r, c = cur
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dr, dc in directions:
        new_r, new_c = r + dr, c + dc
        if new_r < 0 or new_r >= nr or new_c < 0 or new_c >= nc:
            continue
        neighbor = (new_r, new_c)
        alt = distance[cur] + int(lines[new_r][new_c])
        if alt < distance[neighbor]:
            distance[neighbor] = alt
print(distance[(nr - 1, nc - 1)])
