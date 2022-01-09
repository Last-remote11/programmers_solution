import sys
from collections import deque
input = sys.stdin.readline


def main():
    n = int(input())
    a, b = map(int,input().split())
    m = int(input())
    l = [ [0 for _ in range(n+1)] for _ in range(n+1) ]
    visited = [ 0 for x in range(n+1) ]
    
    for _ in range(m):
        p, q = map(int,input().split())
        l[p][q] = 1
        l[q][p] = 1

    q = deque([])
    q.append(a)
    visited[a] = 1
    ans = 0
    while q:
        for i in range(len(q)):
            now = q.popleft()
            for j in range(1, n+1):
                if l[j][now] and not visited[j]:
                    if j == b:
                        print(ans+1)
                        return
                    q.append(j)
                    visited[j] = 1
                if l[now][j] and not visited[j]:
                    if j == b:
                        print(ans+1)
                        return
                    q.append(j)
                    visited[j] = 1
        ans += 1
    print(-1)
main()
