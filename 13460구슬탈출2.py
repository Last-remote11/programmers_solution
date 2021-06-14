from collections import deque
n, m = map(int, input().split())
board = []
for i in range(n):
    a = list(input())
    board.append(a)
    for j in range(m):
        if a[j] == "R":
            ri, rj = i, j
        if a[j] == "B":
            bi, bj = i, j

# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[[[False] * m for i in range(n)] for i in range(m)] for i in range(n)]
# 대충 두 구슬이 방문 여부를 표시하는 4차원 배열(red x, red y, blue x, blue y)


def move(i, j, dx, dy):
    c = 0
    while board[i + dx][j + dy] != "#" and board[i][j] != "O":
        # 벽이나 탈출구를 찾기 전까지 계속 이동
        i += dx
        j += dy
        c += 1
        # 이동한 거리인 c는 나중에 두 구슬이 겹쳤을 때 쓴다.
    return i, j, c

def bfs():
    while q:
        ri, rj, bi, bj, d = q.popleft()
        if d > 10:
            break
        for i in range(4):
            nri, nrj, rc = move(ri, rj, dx[i], dy[i])
            nbi, nbj, bc = move(bi, bj, dx[i], dy[i])
            if board[nbi][nbj] != "O":
                if board[nri][nrj] == "O":
                    print(d)
                    return
                if nri == nbi and nrj == nbj:
                    if rc > bc: 
                        # red가 움직인 거리가 더 길면 (뒤에있었으면) 한칸뒤로
                        nri -= dx[i]
                        nrj -= dy[i]
                    else:
                        # blue가 더 길면 반대로
                        nbi -= dx[i]
                        nbj -= dy[i]
                if not visited[nri][nrj][nbi][nbj]:
                    visited[nri][nrj][nbi][nbj] = True
                    q.append([nri, nrj, nbi, nbj, d + 1])
    print(-1)

q = deque()
q.append([ri, rj, bi, bj, 1])
visited[ri][rj][bi][bj] = True
bfs()
