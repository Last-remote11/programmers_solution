import sys
input = sys.stdin.readline

n, m, r, c, k = list(map(int, input().split()))

board = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

dice = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
current = [r, c]

dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]


def roll_dice(dice, command):
    if command == 1:
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = (
            dice[3][1],
            dice[1][0],
            dice[1][1],
            dice[1][2],
        )
    elif command == 2:
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = (
            dice[1][1],
            dice[1][2],
            dice[3][1],
            dice[1][0],
        )
    elif command == 3:
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = (
            dice[1][1],
            dice[2][1],
            dice[3][1],
            dice[0][1],
        )
    else:
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = (
            dice[3][1],
            dice[0][1],
            dice[1][1],
            dice[2][1],
        )
    return dice


for command in commands:
    cr, cc = current
    nr = cr + dr[command]
    nc = cc + dc[command]
    if 0 <= nr < n and 0 <= nc < m:
        roll_dice(dice, command)
        current = [nr, nc]
        if board[nr][nc] == 0:
            board[nr][nc] = dice[3][1] * 1
        else:
            dice[3][1] = board[nr][nc] * 1
            board[nr][nc] = 0
        print(dice[1][1])
