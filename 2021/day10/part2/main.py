import collections

lines = open('input.txt').read().split('\n')

open_close = dict(zip('([{<', ')]}>'))
score_map = {')': 1, ']': 2, '}': 3, '>': 4}

def check_syntax(stack):
    for token in line:
        if token in '([{<':
            stack.append(token)
        else:
            opening = stack.pop()
            if open_close[opening] != token:
                return False
    return True

scores = []
for line in lines:
    stack = collections.deque()
    if check_syntax(stack):
        score = 0
        while stack:
            score *= 5
            token = stack.pop()
            score += score_map[open_close[token]]
        scores.append(score)
print(sorted(scores)[len(scores) // 2])
