grid = list(map(lambda x: list(map(lambda y: int(y), x)), open('input.txt').read().split('\n')))

def flash(grid, r, c, flashed):
    if (r, c) in flashed:
        return
    flashed.add((r, c))
    directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if nr >= 0 and nr < 10 and nc >= 0 and nc < 10:
            grid[nr][nc] += 1
            if grid[nr][nc] > 9:
                flash(grid, nr, nc, flashed)

steps = 100
flashes = 0
for _ in range(steps):
    flashed = set()
    for r in range(10):
        for c in range(10):
            grid[r][c] += 1
    for r in range(10):
        for c in range(10):
            if grid[r][c] > 9:
                flash(grid, r, c, flashed)
    for r, c in flashed:
        grid[r][c] = 0
    flashes += len(flashed)
print(flashes)
