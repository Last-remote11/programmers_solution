from collections import deque

h, w = map(int, input().split())

board = [list(input().strip()) for _ in range(h)]
coin = []

for i in range(h):
    for j in range(w):
        if board[i][j] == "o":
            coin.append([i, j])

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

q = deque()
q.append(coin)


def bfs():
    for j in range(10):
        for i in range(len(q)):
            a, b = q.popleft()
            ar, ac = a
            br, bc = b

            for i in range(4):
                nar = ar + dy[i]
                nac = ac + dx[i]
                nbr = br + dy[i]
                nbc = bc + dx[i]

                if (
                    (nar < 0 or nar >= h or nac < 0 or nac >= w)
                    and 0 <= nbr < h
                    and 0 <= nbc < w
                ):
                    print(j + 1)
                    return

                if (
                    (nbr < 0 or nbr >= h or nbc < 0 or nbc >= w)
                    and 0 <= nar < h
                    and 0 <= nac < w
                ):
                    print(j + 1)
                    return

                if (
                    0 <= nar < h and 0 <= nac < w and 0 <= nbr < h and 0 <= nbc < w
                ):  # 아무것도 안나감
                    if board[nar][nac] == "#":
                        nar, nac = ar, ac
                    if board[nbr][nbc] == "#":
                        nbr, nbc = br, bc
                    q.append([[nar, nac], [nbr, nbc]])
    print(-1)


bfs()
