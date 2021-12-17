x_input, y_input = open('input.txt').read().split(': ')[1].split(', ')

from_x, to_x = map(lambda x: int(x), x_input[2:].split('..'))
from_y, to_y = map(lambda y: int(y), y_input[2:].split('..'))

def can_reach(x_vel, y_vel):
    x_pos, y_pos = 0, 0
    while True:
        if x_pos > to_x or (y_pos < from_y and y_vel <= 0):
            break
        if from_x <= x_pos <= to_x and from_y <= y_pos <= to_y:
            return True
        x_pos += x_vel
        y_pos += y_vel
        if x_vel > 0:
            x_vel -= 1
        y_vel -= 1
    return False

def triangle(x):
    return x * (x + 1) // 2

max_y = 0
for x_vel in range(to_x + 1):
    if triangle(x_vel) < from_x:
        continue
    for y_vel in range(from_y, -from_y + 1):
        if can_reach(x_vel, y_vel):
            max_y = max(max_y, triangle(y_vel))
print(max_y)
