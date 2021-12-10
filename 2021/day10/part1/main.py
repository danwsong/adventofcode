import collections

lines = open('input.txt').read().split('\n')

open_close = dict(zip('([{<', ')]}>'))
score_map = {')': 3, ']': 57, '}': 1197, '>': 25137}

score = 0
for line in lines:
    stack = collections.deque()
    for token in line:
        if token in '([{<':
            stack.append(token)
        else:
            opening = stack.pop()
            if open_close[opening] != token:
                score += score_map[token]
print(score)
