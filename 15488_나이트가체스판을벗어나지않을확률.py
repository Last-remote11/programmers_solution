import sys

input = sys.stdin.readline

dy = [2, 1, -1, -2, -2, -1, 1, 2]
dx = [1, 2, 2, 1, -1, -2, -2, -1]

def main():

    N, x, y, K = map(int, input().split())
    B = [ [0 for _ in range(N)] for _ in range(N) ]
    B[y-1][x-1] = 1

    for _ in range(K):
        temp = [ [0 for _ in range(N)] for _ in range(N) ]
        for i in range(N):
            for j in range(N):
                for d in range(8):
                    ny, nx = i + dy[d], j + dx[d]
                    if 0 <= ny < N and 0 <= nx < N:
                        temp[ny][nx] += B[i][j] * 0.125
                        
        B = temp
    print(sum(map(sum, B)))

main()
