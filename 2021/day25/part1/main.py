import itertools

grid = open('input.txt').read().split('\n')

nr = len(grid)
nc = len(grid[0])

east_moving = set()
south_moving = set()
for r in range(nr):
    for c in range(nc):
        if grid[r][c] == '>':
            east_moving.add((r, c))
        elif grid[r][c] == 'v':
            south_moving.add((r, c))

for step in itertools.count(1):
    new_east_moving = set()
    new_south_moving = set()
    moved = False
    for r, c in east_moving:
        east = (r, (c + 1) % nc)
        if east not in east_moving and east not in south_moving:
            new_east_moving.add(east)
            moved = True
        else:
            new_east_moving.add((r, c))
    for r, c in south_moving:
        south = ((r + 1) % nr, c)
        if south not in new_east_moving and south not in south_moving:
            new_south_moving.add(south)
            moved = True
        else:
            new_south_moving.add((r, c))
    if not moved:
        print(step)
        break
    east_moving = new_east_moving
    south_moving = new_south_moving
