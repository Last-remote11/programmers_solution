import sys
from collections import deque

input = sys.stdin.readline

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

# 지도 주변을 0으로 둘러싸서 한겹 더 생성
def padding():
    for i in board:
        i.insert(0, ".")
        i.append(".")
    board.insert(0, ["."] * (w + 2))
    board.append(["."] * (w + 2))

# [0, 0](바깔 아무데나)와, 수감자 방 두개에서 탐색을 시작하여
# 모든 칸을 몇 최소 개의 문을 따고 갈 수 있는지를 표시
# 빈칸이면 appendleft를 하여 우선으로 처리
def bfs(y, x):

    visited = [[-1] * (w + 2) for _ in range(h + 2)]
    visited[y][x] = 0
    q = deque()
    q.append([y, x])
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dy[i]
            nc = c + dx[i]

            if 0 <= nr < h + 2 and 0 <= nc < w + 2:
                if visited[nr][nc] == -1:
                    if board[nr][nc] == "." or board[nr][nc] == "$":
                        visited[nr][nc] = visited[r][c]
                        q.appendleft([nr, nc])
                    if board[nr][nc] == "#":
                        visited[nr][nc] = visited[r][c] + 1
                        q.append([nr, nc])
    return visited


N = int(input())

for _ in range(N):
    h, w = map(int, input().split())
    board = [list(input().strip()) for x in range(h)]
    prisoner = []

    padding()

    for i in range(h + 2):
        for j in range(w + 2):
            if board[i][j] == "$":
                prisoner.append([i, j])

    v1 = bfs(0, 0)
    v2 = bfs(prisoner[0][0], prisoner[0][1])
    v3 = bfs(prisoner[1][0], prisoner[1][1])

    ans = sys.maxsize
    # 모든 칸을 체크해 가장 작은거 출력, 만약 그 칸이 '#'(문)이면 -2
    for i in range(h + 2):
        for j in range(w + 2):
            if v1[i][j] != -1 and v2[i][j] != -1 and v3[i][j] != -1:
                cnt = v1[i][j] + v2[i][j] + v3[i][j]
                if board[i][j] == "#":
                    cnt -= 2
                ans = min(ans, cnt)
    print(ans)
