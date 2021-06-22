import sys
from collections import deque

input = sys.stdin.readline

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

# 지도 주변을 0으로 한 겹 둘러쌈
def padding():
    for i in board:
        i.insert(0, ".")
        i.append(".")
    board.insert(0, ["."] * (w + 2))
    board.append(["."] * (w + 2))

# 현재 가진 열쇠를 비트로 표시할것임. board의 원소들은 다 0이고 기본 bit 상태는 1이다.
# 방문 표시 기능을 겸하며 열쇠가 하나도 없어도 빈 방을 갈 수는 있기 때문이다.
# dist를 지나갈 때 마다 이전 dist | 다음dist를 다음 dist에 넣어준다.
# dist가 같으면 이미 지났다는 뜻이므로 탐색 끝
# 열쇠를 만나면 현재 비트에 1 << 알파벳 순서+1만큼 합쳐준다.
# 대문자(문)을 만났을 때 현재 비트에 대문자를 << 한 것이 겹치면 지나갈 수 있다.

def bfs(bit):
    ans = 0
    dist = [[0] * (w + 2) for _ in range(h + 2)]
    dist[0][0] = bit
    q = deque()
    q.append([0, 0])
    while q:
        r, c = q.popleft()
        for i in range(4):

            nr = r + dy[i]
            nc = c + dx[i]

            if 0 <= nr < h + 2 and 0 <= nc < w + 2:
                if dist[nr][nc] != dist[r][c]:
                    if board[nr][nc] == ".":
                        dist[nr][nc] = dist[r][c] | dist[nr][nc]
                        q.append([nr, nc])
                    elif 65 <= ord(board[nr][nc]) <= 90:  # 대문자(문)
                        if bit | 1 << (ord(board[nr][nc]) - 64) == bit:
                            dist[r][c] = dist[r][c] | dist[nr][nc]
                            dist[nr][nc] = dist[r][c] | dist[nr][nc]
                            q.append([nr, nc])
                    elif 97 <= ord(board[nr][nc]) <= 122:  # 소문자(열쇠)
                        bit = bit | 1 << (ord(board[nr][nc]) - 96)
                        dist[nr][nc] = bit | dist[nr][nc]
                        q.append([nr, nc])
                        # print("열쇠", board[nr][nc])
                    elif board[nr][nc] == "$":
                        ans += 1
                        dist[nr][nc] = dist[r][c] | dist[nr][nc]
                        # print("찾았당", ans)
                        board[nr][nc] = "."
                        q.append([nr, nc])
    # for x in dist:
    #     print(x)
    return ans


N = int(input())

for _ in range(N):
    h, w = map(int, input().split())
    board = [list(input().strip()) for x in range(h)]
    keys = input()
    bit = 1
    for key in keys:
        if 97 <= ord(key) <= 122:
            bit = bit | (1 << (ord(key) - 96))

    padding()

    print(bfs(bit))

# 대문자: 65~90 소문자: 97~122
