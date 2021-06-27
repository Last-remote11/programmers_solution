import sys

input = sys.stdin.readline
n, m = map(int, input().split())
r, c, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(n)]

dy = [0, -1, 0, 1] # 현재 방향에서 왼쪽칸
dx = [-1, 0, 1, 0]

by = [1, 0, -1, 0] # 현재 방향에서 뒷칸
bx = [0, -1, 0, 1]

ans = 0

while True:
    if room[r][c] == 0:
        room[r][c] = -1
        ans += 1

    for i in range(4):
        nr = r + dy[d % 4]
        nc = c + dx[d % 4]
        if room[nr][nc] == 0:
            r = nr * 1
            c = nc * 1
            d -= 1 # 왼쪽칸이 0이면 이동 & 왼쪽으로 턴
            if d == -1:
                d = 3
            break
        else: # 벽이거나 이미 청소했으면 왼쪽으로 회전만
            d -= 1
            if d == -1:
                d = 3
        if i == 3: # 네 방향 모두 봤으면 뒤로 이동한다.
            br = r + by[d % 4]
            bc = c + bx[d % 4]

            if room[br][bc] == 1: # 뒤가 벽이면 끝
                print(ans)
                exit()

            r = br * 1
            c = bc * 1
