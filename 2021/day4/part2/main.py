blocks = open('input.txt').read().split('\n\n')
nums = list(map(lambda x: int(x), blocks[0].split(',')))
blocks = blocks[1:]
boards = [[list(map(lambda x: int(x), row.split())) for row in block.split('\n')] for block in blocks]

def has_won(board):
    for r in range(len(board)):
        if all(slot == -1 for slot in board[r]):
            return True
    for c in range(len(board[0])):
        if all(slot == -1 for slot in [row[c] for row in board]):
            return True
    return False

won_boards = set()
scores = []

for num in nums:
    for board_num, board in enumerate(boards):
        if board_num in won_boards:
            continue
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == num:
                    board[r][c] = -1
        if has_won(board):
            slot_sum = 0
            for r in range(len(board)):
                for c in range(len(board[r])):
                    if board[r][c] != -1:
                        slot_sum += board[r][c]
            won_boards.add(board_num)
            scores.append(slot_sum * num)

print(scores[-1])
