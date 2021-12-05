lines = open('input.txt').read().split('\n')

grid = [[0 for c in range(1000)] for r in range(1000)]

for line in lines:
    l, r = line.split(' -> ')
    lx, ly = map(int, l.split(','))
    rx, ry = map(int, r.split(','))
    if lx == rx:
        dir = 1 if ly < ry else -1
        for y in range(ly, ry + dir, dir):
            grid[lx][y] += 1
    if ly == ry:
        dir = 1 if lx < rx else -1
        for x in range(lx, rx + dir, dir):
            grid[x][ly] += 1
    if (rx - lx) == (ry - ly) or (rx - lx) == (ly - ry):
        dirx = 1 if lx < rx else -1
        diry = 1 if ly < ry else -1
        for x, y in zip(range(lx, rx + dirx, dirx), range(ly, ry + diry, diry)):
            grid[x][y] += 1

multiple = 0
for row in grid:
    for slot in row:
        if slot > 1:
            multiple += 1
print(multiple)
