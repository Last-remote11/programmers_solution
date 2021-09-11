from collections import deque
import sys

input = sys.stdin.readline

dy = [1,1,1,0,0,-1,-1,-1,0]
dx = [-1,0,1,1,-1,-1,0,1,0]

def main():
    h, w = map(int, input().split())

    board = [ list(input().strip()) for _ in range(h) ]
    for i, line in enumerate(board):
        for j, char in enumerate(line):
            if char == 'A': start_Ay, start_Ax = [i,j]
            if char == 'B': start_By, start_Bx = [i,j]

    visited = [[[[0 for _ in range(w)] for _ in range(h)] for _ in range(w)] for _ in range(h)] # ay, ax, by, bx
    q = deque([])
    q.append([start_Ay, start_Ax, start_By, start_Bx])
    visited[start_Ay][start_Ax][start_By][start_Bx] = 1
    ans = 0
    while q:
        for _ in range(len(q)):
            ay, ax, by, bx = q.popleft()
            if ay == start_By and ax == start_Bx and by == start_Ay and bx == start_Ax:
                print(ans)
                return
            
            for i in range(9):
                nay, nax  = ay + dy[i], ax + dx[i]
                for j in range(9):
                    nby, nbx = by + dy[j], bx + dx[j]
                    if nay == by and nax == bx and nby == ay and nbx == ax: continue # swap
                    if nay == nby and nax == nbx: continue
                    if (
                        0 <= nay < h and
                        0 <= nax < w and
                        0 <= nby < h and
                        0 <= nbx < w
                    ):
                        if not visited[nay][nax][nby][nbx] and board[nay][nax] != 'X' and board[nby][nbx] != 'X':
                            q.append([nay,nax,nby,nbx])
                            visited[nay][nax][nby][nbx] = 1
        ans += 1
    print(-1)

main()
