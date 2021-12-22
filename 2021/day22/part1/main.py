spaces = set()

for line in open('input.txt').readlines():
    on, line = line.split(' ')
    x, y, z = (tuple(map(int, dim.split('=')[1].split('..'))) for dim in line.split(','))
    for _x in range(x[0], x[1] + 1):
        for _y in range(y[0], y[1] + 1):
            for _z in range(z[0], z[1] + 1):
                if on == "on":
                    spaces.add((_x, _y, _z))
                elif (_x, _y, _z) in spaces:
                    spaces.remove((_x, _y, _z))

print(len(spaces))
