algorithm, image = open('input.txt').read().split('\n\n')
image = image.split('\n')

flipped = algorithm[0] == '#'

alive = set()
for r, row in enumerate(image):
    for c, pixel in enumerate(row):
        if pixel == '#':
            alive.add((r, c))

min_r, max_r = 0, len(image)
min_c, max_c = 0, len(image[0])

for step in range(50):
    min_r -= 1
    max_r += 1
    min_c -= 1
    max_c += 1
    new_alive = set()
    for r in range(min_r, max_r):
        for c in range(min_c, max_c):
            locs = [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1), (r, c - 1), (r, c), (r, c + 1), (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)]
            binary = 0
            for loc in locs:
                binary <<= 1
                if flipped:
                    if step % 2 == 0:
                        if loc in alive:
                            binary |= 1
                    else:
                        lr, lc = loc
                        if lr < (min_r + 1) or lr >= (max_r - 1) or lc < (min_c + 1) or lc >= (max_c - 1):
                            binary |= 1
                        elif loc in alive:
                            binary |= 1
                else:
                    if loc in alive:
                        binary |= 1
            if algorithm[binary] == '#':
                new_alive.add((r, c))
    alive = new_alive

print(len(alive))
