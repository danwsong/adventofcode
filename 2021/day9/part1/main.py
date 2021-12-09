lines = open('input.txt').read().split('\n')

lines = list(map(lambda x: [int(y) for y in x], lines))

nr = len(lines)
nc = len(lines[0])

risk = 0
for r in range(nr):
    for c in range(nc):
        if (r == 0 or lines[r][c] < lines[r - 1][c]) and (r == nr - 1 or lines[r][c] < lines[r + 1][c]) and (c == 0 or lines[r][c] < lines[r][c - 1]) and (c == nc - 1 or lines[r][c] < lines[r][c + 1]):
            risk += lines[r][c] + 1
print(risk)
