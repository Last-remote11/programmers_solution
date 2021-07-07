from collections import deque
import sys

input = sys.stdin.readline

k = int(input())
w, h = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(h)]
d = [[[0] * (k + 1) for _ in range(w)] for i in range(h)]


def bfs():
    q = deque()
    q.append([0, 0, 0])  # 좌표, 점프횟수
    while q:
        r, c, b = q.popleft()
        if r == h - 1 and c == w - 1:
            return d[r][c][b]
        for i in range(4):
            nr = r + dy1[i]
            nc = c + dx1[i]

            if 0 <= nr < h and 0 <= nc < w:
                if board[nr][nc] == 0 and not d[nr][nc][b]:
                    d[nr][nc][b] = d[r][c][b] + 1
                    q.append([nr, nc, b])
        if b < k:
            for j in range(8):
                nr = r + dy2[j]
                nc = c + dx2[j]

                if 0 <= nr < h and 0 <= nc < w:
                    if board[nr][nc] == 0 and not d[nr][nc][b + 1]:
                        d[nr][nc][b + 1] = d[r][c][b] + 1
                        q.append([nr, nc, b + 1])
    return -1


dy1 = [1, -1, 0, 0]
dx1 = [0, 0, 1, -1]
dy2 = [-2, -1, 1, 2, 2, 1, -1, -2]
dx2 = [1, 2, 2, 1, -1, -2, -2, -1]
print(bfs())
