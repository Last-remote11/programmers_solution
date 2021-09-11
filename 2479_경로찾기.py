from collections import deque
import sys

input = sys.stdin.readline

dy = [1,1,1,0,0,-1,-1,-1,0]
dx = [-1,0,1,1,-1,-1,0,1,0]

def issuare(n):
    while n >= 2:
        n /= 2
    if n == 1:
        return True
    else:
        return False

def main():
    N, K = map(int,input().split())
    codes = []
    for _ in range(N):
        str = input()
        tmp = 0
        for idx in range(K):
            if str[idx] == '1':
                tmp = tmp | 1 << (K-1-idx)
        codes.append(tmp)

    link = [ [0 for _ in range(N)] for _ in range(N) ]

    for i in range(N):
        for j in range(N):
            if issuare(codes[i] ^ codes[j]):
                link[i][j] = 1
    
    visited = [ 0 for _ in range(N) ]

    A, B = map(int,input().split())
    q = deque([])
    q.append([A, [A]])
    visited[A-1] = 1
    ans = 0

    while q:
        for _ in range(len(q)):
            c, paths = q.popleft()
            if c == B:
                for a in paths:
                    print(a, end=' ')
                return
            for i in range(N):
                if link[c-1][i] and not visited[i]:
                    q.append([i+1, paths + [i+1]])
                    visited[i] = 1

        ans += 1
    print(-1)

main()
