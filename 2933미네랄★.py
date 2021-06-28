import sys
from collections import deque

input = sys.stdin.readline

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def check_cluster(x):
    cr, cc = x
    visited = [[0] * c for _ in range(r)]
    visited[cr][cc] = 1
    q = deque([[cr, cc]])
    cluster = [[cr, cc]]
    while q:
        cr, cc = q.popleft()
        for i in range(4):
            nr = cr + dy[i]
            nc = cc + dx[i]
            if 0 <= nr < r and 0 <= nc < c:
                if board[nr][nc] == "x" and not visited[nr][nc]:
                    cluster.append([nr, nc])
                    visited[nr][nc] = 1
                    q.append([nr, nc])
    return cluster, visited


def fall_cluster(cluster, visited):
    global dropped
    temp = 1000  # 떨어질 단차
    for row, col in cluster:
        gap = 0
        if row >= r - 1:
            print("바닥에 닿은 클러스터")
            return
        while True:
            gap += 1
            row += 1
            if row >= r - 1:
                break
            if visited[row + 1][col]:
                gap = 1000
                break
            if board[row + 1][col] == "x":
                break
        temp = min(temp, gap)
    # print("temp", temp)
    new_cluster = list(map(lambda x: [x[0] + temp, x[1]], cluster))
    for i in cluster:
        board[i[0]][i[1]] = "."
    for j in new_cluster:
        board[j[0]][j[1]] = "x"
    dropped = True


r, c = map(int, input().split())
board = []

for _ in range(r):
    board.append(list(map(lambda x: x, input().strip())))

n_mineral = 0
for i in range(r):
    for j in range(c):
        if board[i][j] == "x":
            n_mineral += 1

n = int(input())
throws = list(map(int, input().split()))

for _ in range(n):
    height = throws[_]
    height = r - height
    dropped = False
    if _ % 2 == 0:  # 왼쪽에서던짐
        for i in range(c):
            if board[height][i] == "x":
                board[height][i] = "."
                n_mineral -= 1
                if height != 0:
                    if board[height - 1][i] == "x":
                        cluster, visited = check_cluster([height - 1, i])
                        if len(cluster) <= n_mineral:
                            print("위떨굼")
                            fall_cluster(cluster, visited)

                if height + 1 < r:
                    if board[height + 1][i] == "x" and not dropped:
                        cluster, visited = check_cluster([height + 1, i])
                        if len(cluster) <= n_mineral:
                            print("아래떨굼")
                            fall_cluster(cluster, visited)

                if i + 1 != c:
                    if board[height][i + 1] == "x" and not dropped:
                        cluster, visited = check_cluster([height, i + 1])

                        if len(cluster) <= n_mineral:
                            print("오른쪽떨굼")
                            fall_cluster(cluster, visited)
                            break
                break
    else:  # 오른쪽에서던짐
        for i in range(c - 1, -1, -1):
            if board[height][i] == "x":
                dropped = False
                board[height][i] = "."
                n_mineral -= 1
                if height != 0:
                    if board[height - 1][i] == "x":
                        cluster, visited = check_cluster([height - 1, i])
                        if len(cluster) <= n_mineral:
                            print("윗쪽떨굼")
                            fall_cluster(cluster, visited)

                if height + 1 < r:
                    if board[height + 1][i] == "x" and not dropped:
                        cluster, visited = check_cluster([height + 1, i])
                        if len(cluster) <= n_mineral:
                            print("아래떨굼")
                            fall_cluster(cluster, visited)

                if i != 0:
                    if board[height][i - 1] == "x" and not dropped:
                        cluster, visited = check_cluster([height, i - 1])
                        if len(cluster) <= n_mineral:
                            print("왼쪽떨굼")
                            fall_cluster(cluster, visited)

                break

for i in board:
    print("".join(str(x) for x in i))
