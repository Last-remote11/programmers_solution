from collections import deque


def bfs():
    q = deque()
    q.append([0, 0, 0])

    while q:
        cur, line, time = q.popleft()

        if cur >= n - k:
            return 1

        for i in (1, -1):
            if cur + i > time and board[line][cur + i]:
                q.append([cur + i, line, time + 1])
                board[line][cur + i] = 0

        if board[int(bool(not line))][cur + k]:
            q.append([cur + k, int(bool(not line)), time + 1])
            board[int(bool(not line))][cur + k] = 0

    return 0


n, k = map(int, input().split())
board = []  # [0or1][높이]

for i in range(2):
    board.append(list(map(int, input().strip())))

print(bfs())
