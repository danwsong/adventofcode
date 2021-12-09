import collections
import math

lines = open('input.txt').read().split('\n')

lines = list(map(lambda x: [int(y) for y in x], lines))

nr = len(lines)
nc = len(lines[0])

def find(data, i):
    if i != data[i]:
        data[i] = find(data, data[i])
    return data[i]
def union(data, i, j):
    pi, pj = find(data, i), find(data, j)
    if pi != pj:
        data[pi] = pj
def connected(data, i, j):
    return find(data, i) == find(data, j)

uf = [i for i in range(nr * nc)]

def index(r, c):
    return r * nc + c

for r in range(nr):
    for c in range(nc):
        if lines[r][c] == 9:
            continue
        if r > 0 and lines[r][c] > lines[r - 1][c]:
            union(uf, index(r, c), index(r - 1, c))
        if r < nr - 1 and lines[r][c] > lines[r + 1][c]:
            union(uf, index(r, c), index(r + 1, c))
        if c > 0 and lines[r][c] > lines[r][c - 1]:
            union(uf, index(r, c), index(r, c - 1))
        if c < nc - 1 and lines[r][c] > lines[r][c + 1]:
            union(uf, index(r, c), index(r, c + 1))

basins = [find(uf, i) for i in range(nr * nc)]

print(math.prod(map(lambda x: x[1], collections.Counter(basins).most_common(3))))
