players = open('input.txt').read().split('\n')
players[0] = int(players[0].split(' ')[-1])
players[1] = int(players[1].split(' ')[-1])

cur_dice = 1
cur_turn = 0

player_scores = [0, 0]

dice_rolls = 0

while True:
    dice_roll = 0
    for _ in range(3):
        dice_roll += cur_dice
        cur_dice += 1
        dice_rolls += 1
        if cur_dice > 100:
            cur_dice = 1
    players[cur_turn] = (players[cur_turn] + dice_roll - 1) % 10 + 1
    player_scores[cur_turn] += players[cur_turn]
    if player_scores[cur_turn] >= 1000:
        break
    cur_turn = 1 - cur_turn

print(min(player_scores) * dice_rolls)
