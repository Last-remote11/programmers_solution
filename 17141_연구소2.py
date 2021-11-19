import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

dy = [1,0,-1,0]
dx = [0,-1,0,1]


def boom(P, virus):
    visited = [[0 for x in range(N)] for x in range(N)]
    q = deque()
    for v in virus:
        q.append(v)
        visited[v[0]][v[1]] = 1
    loop = 0
    v = 0
    while q:
        for _ in range(len(q)):
            cy, cx = q.popleft()
            for k in range(4):
                ny, nx = cy + dy[k], cx + dx[k]
                if 0 <= ny < N and 0 <= nx < N:
                    if P[ny][nx] == 0 and not visited[ny][nx]:
                        q.append([ny, nx])
                        visited[ny][nx] = 1
                        v += 1
        loop += 1

    return v, loop-1

N, M = map(int, input().split())

def main():

    P = []
    vlist = []
    vnum = 0
    ans = 999
    flag = False
    for _ in range(N):
        line = list(map(int, input().split()))
        for idx, i in enumerate(line):
            if i == 2:
                vlist.append([_, idx])
                line[idx] = 0
                vnum += 1
            elif i == 0:
                vnum += 1
        P.append(line)
    vnum -= M
    for combi in combinations(vlist, M):
        v, loop = boom(P, combi)
        if v == vnum:
            flag = True
            ans = min(ans, loop)
    
    if not flag:
        print(-1)
    else:
        print(ans)

main()
