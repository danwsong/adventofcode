import heapq
import math

lines = open('input.txt').read().split('\n')

nr = len(lines)
nc = len(lines[0])

scale = 1

grid = [[0 for c in range(nc * scale)] for r in range(nr * scale)]
for br in range(scale):
    for bc in range(scale):
        for r in range(nr):
            for c in range(nc):
                grid[br * nr + r][bc * nc + c] = (int(lines[r][c]) - 1 + br + bc) % 9 + 1

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

src = (0, 0)
dst = (nr * scale - 1, nc * scale - 1)
q = [(0, src)]
visited = set()
min_dist = {src : 0}

while q:
    dist, cur = heapq.heappop(q)
    if cur in visited:
        continue
    r, c = cur
    for dr, dc in directions:
        new_r, new_c = r + dr, c + dc
        if new_r < 0 or new_r >= nr * scale or new_c < 0 or new_c >= nc * scale:
            continue
        neighbor = (new_r, new_c)
        alt = dist + grid[new_r][new_c]
        if alt < min_dist.get(neighbor, math.inf):
            min_dist[neighbor] = alt
            heapq.heappush(q, (alt, neighbor))

print(min_dist[dst])
