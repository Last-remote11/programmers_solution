from collections import deque
import copy

n = int(input())
ans = -1

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

def check_nonzero(board, n):
    nonzero = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                nonzero += 1
    return nonzero

def merge(arr, nonzero):

    for k in range(len(arr)-1):
        if arr[k] == arr[k+1] and arr[k] != 0:
            arr[k] = arr[k] * 2
            del arr[k+1]
            arr.append(0)
            nonzero -= 1
    return [arr, nonzero]

def move_right(c_board, nonzero):

    for i in range(n):
        temp = []
        for j in range(n-1, -1, -1):
            if c_board[i][j] != 0:
                temp.append(c_board[i][j])

        temp, nonzero = merge(temp, nonzero)
        for j in range(n-1, -1, -1):
            if temp:
                c_board[i][j] = temp.pop(0)
            else:
                c_board[i][j] = 0
    return [c_board, nonzero]

def move_left(c_board, nonzero):

    for i in range(n):
        temp = []
        for j in range(n):
            if c_board[i][j] != 0:
                temp.append(c_board[i][j])

        temp, nonzero = merge(temp, nonzero)

        for j in range(n):
            if temp:
                c_board[i][j] = temp.pop(0)
            else:
                c_board[i][j] = 0
    return [c_board, nonzero]

def move_up(c_board, nonzero):

    for i in range(n):
        temp = []
        for j in range(n):
            if c_board[j][i] != 0:
                temp.append(c_board[j][i])

        temp, nonzero = merge(temp, nonzero)

        for j in range(n):
            if temp:
                c_board[j][i] = temp.pop(0)
            else:
                c_board[j][i] = 0
    return [c_board, nonzero]


def move_down(c_board, nonzero):

    for i in range(n):
        temp = []
        for j in range(n-1, -1, -1):
            if c_board[j][i] != 0:
                temp.append(c_board[j][i])

        temp, nonzero = merge(temp, nonzero)

        for j in range(n-1, -1, -1):
            if temp:
                c_board[j][i] = temp.pop(0)
            else:
                c_board[j][i] = 0
    return [c_board, nonzero]


moves = [move_right, move_left, move_up, move_down]
q = deque()
nonzero = check_nonzero(board, n)
q.append([board, nonzero])

for i in range(5):
    for _ in range(len(q)):
        c_board, nonzero = q.popleft()
        for move in moves:
            copy_board = copy.deepcopy(c_board)
            copy_nonzero = nonzero * 1
            n_board, n_nonzero = move(copy_board, copy_nonzero)
            if n_nonzero == 1:
                ans = max(ans, max(map(max, n_board)))
            else:
                q.append([n_board, n_nonzero])

for board in list(q):
    ans = max(ans, max(map(max, board[0])))

print(ans)
