import sys
from collections import deque

input = sys.stdin.readline

dy = [1,0,-1,0]
dx = [0,-1,0,1]

def pop(P):
    flag = False
    visited = [[0 for x in range(6)] for x in range(12)]
    for i in range(12):
        for j in range(6):
            if P[i][j] != '.' and not visited[i][j]:
                color = P[i][j]
                visited[i][j] = 1
                block = [[i, j]]
                q = deque([[i, j]])
                while q:
                    cy, cx = q.popleft()
                    for k in range(4):
                        ny, nx = cy + dy[k], cx + dx[k]
                        if 0 <= ny < 12 and 0 <= nx < 6:
                            if P[ny][nx] == color and not visited[ny][nx]:
                                q.append([ny, nx])
                                visited[ny][nx] = 1
                                block.append([ny, nx])

                if len(block) >= 4:
                    flag = True
                    for y, x in block:
                        P[y][x] = '.'
    return flag, P

def fall(P):
    for i in range(10, -1, -1):
        for j in range(6):
            if P[i+1][j] == '.':                
                t = i*1
                while P[t+1][j] == '.':
                    P[t+1][j] = P[t][j]
                    P[t][j] = '.'
                    t += 1
                    if t == 11:break
    return P

def main():

    P = []
    ans = 0

    for _ in range(12):
        P.append([x for x in input().rstrip()])

    while True:
        poped, P = pop(P)
        if not poped:
            print(ans)
            return
        else:
            ans += 1
            P = fall(P)

main()



