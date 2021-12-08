import itertools

lines = open('input.txt').read().split('\n')

nums = [
    'abcefg',
    'cf',
    'acdeg',
    'acdfg',
    'bcdf',
    'abdfg',
    'abdefg',
    'acf',
    'abcdefg',
    'abcdfg',
]

def next_permutation(a):
    for i in reversed(range(len(a) - 1)):
        if a[i] < a[i + 1]:
            break
    else:
        return False
    j = next(j for j in reversed(range(i + 1, len(a))) if a[i] < a[j])
    a[i], a[j] = a[j], a[i]
    a[i + 1:] = reversed(a[i + 1:])
    return True

def map_num(num, current_map):
    return sorted(current_map[char] for char in num)

total = 0
for line in lines:
    lhs, rhs = map(lambda x: [sorted(num) for num in x.split(' ')], line.split(' | '))
    for current_perm in itertools.permutations('abcdefg'):
        current_map = {char : current_perm[ord(char) - ord('a')] for char in 'abcdefg'}
        mapped_nums = [sorted(current_map[char] for char in num) for num in nums]
        if all(num in lhs for num in mapped_nums):
            total += int(''.join(str(mapped_nums.index(num)) for num in rhs))
            break
print(total)
