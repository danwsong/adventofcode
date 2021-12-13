top, bottom = open('input.txt').read().split('\n\n')

points = []
for line in top.split('\n'):
    x, y = line.split(',')
    x, y = int(x), int(y)
    points.append((x, y))

for line in bottom.split('\n'):
    new_points = set()
    _, _, temp = line.split(' ')
    axis, num = temp.split('=')
    num = int(num)
    for x, y in points:
        if axis == 'x':
            if x > num:
                new_points.add((2 * num - x, y))
            else:
                new_points.add((x, y))
        else:
            if y > num:
                new_points.add((x, 2 * num - y))
            else:
                new_points.add((x, y))
    points = list(new_points)
    break

print(len(points))
