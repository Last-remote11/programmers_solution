from collections import deque
import sys

input = sys.stdin.readline

dy = [-2,-2,0,0,2,2]
dx = [-1,1,-2,2,-1,1]

def main():
    N = int(input())
    y1, x1, y2, x2 = map(int, input().split())
    board = [ [ 0 for _ in range(N) ] for _ in range(N)]
    board[y1][x1] = 1

    q = deque([])
    q.append([y1,x1])
    ans = 0
    while q:
        for _ in range(len(q)):
            cy, cx = q.popleft()
            if cy == y2 and cx == x2:
                print(ans)
                return
            for i in range(6):
                ny = cy + dy[i]
                nx = cx + dx[i]
                if 0 <= ny < N and 0 <= nx < N:
                    if not board[ny][nx]:
                        q.append([ny, nx])
                        board[ny][nx] = 1
        ans += 1
    print(-1)
main()
