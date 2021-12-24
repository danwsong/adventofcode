div_z = []
add_x = []
add_y = []

for line_number, line in enumerate(open('input.txt').read().split('\n')):
    op, *params = line.split(' ')
    if line_number % 18 == 4:
        div_z.append(int(params[1]))
    elif line_number % 18 == 5:
        add_x.append(int(params[1]))
    elif line_number % 18 == 15:
        add_y.append(int(params[1]))

def process_digit(i, w, z):
    x = z % 26 + add_x[i]
    z = z // div_z[i]
    if x != w:
        z *= 26
        z += w + add_y[i]
    return z

def solve(nums, z):
    if len(nums) == 14:
        print(''.join(map(str, nums)))
        return True
    for num in range(9, 1-1, -1):
        new_z = process_digit(len(nums), num, z)
        pops_left = div_z[len(nums)+1:].count(26)
        if new_z // 26 ** pops_left != 0:
            continue
        if solve(nums + [num], new_z):
            return True
    return False

solve([], 0)
