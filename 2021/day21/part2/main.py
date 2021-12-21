players = open('input.txt').read().split('\n')
players[0] = int(players[0].split(' ')[-1])
players[1] = int(players[1].split(' ')[-1])

dp = {}

def solve(p1_score, p2_score, p1_pos, p2_pos, turn):
    if (p1_score, p2_score, p1_pos, p2_pos, turn) in dp:
        return dp[(p1_score, p2_score, p1_pos, p2_pos, turn)]
    if p1_score < 0:
        return 0
    if p2_score < 0:
        return 0
    if p1_score == 0 and p2_score == 0 and p1_pos == players[0] and p2_pos == players[1] and turn == 1:
        return 1
    probabilities = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
    worlds = 0
    if turn == 0:
        for i in range(3, 9+1):
            new_pos = p1_pos - i
            while new_pos < 1:
                new_pos += 10
            worlds += probabilities[i] * solve(p1_score - p1_pos, p2_score, new_pos, p2_pos, 1)
    else:
        for i in range(3, 9+1):
            new_pos = p2_pos - i
            while new_pos < 1:
                new_pos += 10
            worlds += probabilities[i] * solve(p1_score, p2_score - p2_pos, p1_pos, new_pos, 0)
    dp[(p1_score, p2_score, p1_pos, p2_pos, turn)] = worlds
    return worlds

winning_score = 21

p1_worlds = 0
for p1_score in range(winning_score-1+1, winning_score-1+10+1):
    for p2_score in range(winning_score-1+1):
        for p1_pos in range(1, 10+1):
            for p2_pos in range(1, 10+1):
                if p1_score - p1_pos > winning_score-1:
                    continue
                p1_worlds += solve(p1_score, p2_score, p1_pos, p2_pos, 0)

p2_worlds = 0
for p2_score in range(winning_score-1+1, winning_score-1+10+1):
    for p1_score in range(winning_score-1+1):
        for p2_pos in range(1, 10+1):
            for p1_pos in range(1, 10+1):
                if p2_score - p2_pos > winning_score-1:
                    continue
                p2_worlds += solve(p1_score, p2_score, p1_pos, p2_pos, 1)

print(p1_worlds)
print(p2_worlds)
