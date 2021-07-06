from collections import deque
import sys

input = sys.stdin.readline

visited = [[0] * 1500 for i in range(1500)]

a, b, c = list(map(int, input().split()))


def bfs():
    q = deque()
    q.append([a, b, c])
    visited[a][b] = 1

    while q:
        ca, cb, cc = q.popleft()
        # print(ca, cb, cc)
        if ca == cb == cc:
            return 1
        if ca > cb:
            na = ca - cb
            nb = cb * 2
            nc = cc
            if not visited[na][nb]:
                q.append([na, nb, nc])
                visited[na][nb] = 1
        if ca < cb:
            na = ca * 2
            nb = cb - ca
            nc = cc
            if not visited[na][nb]:
                q.append([na, nb, nc])
                visited[na][nb] = 1
        if ca > cc:
            na = ca - cc
            nb = cb
            nc = cc * 2
            if not visited[na][nb]:
                q.append([na, nb, nc])
                visited[na][nb] = 1
        if ca < cc:
            na = ca * 2
            nb = cb
            nc = cc - ca
            if not visited[na][nb]:
                q.append([na, nb, nc])
                visited[na][nb] = 1
        if cb > cc:
            na = ca
            nb = cb - cc
            nc = cc * 2
            if not visited[na][nb]:
                q.append([na, nb, nc])
                visited[na][nb] = 1
        if cb < cc:
            na = ca
            nb = cb * 2
            nc = cc - cb
            if not visited[na][nb]:
                q.append([na, nb, nc])
                visited[na][nb] = 1

    return 0


print(bfs())
