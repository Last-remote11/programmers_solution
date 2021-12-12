import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

def main():

    N, M, K, X = map(int, input().split())    
    X -= 1
    l = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        l[a-1].append(b-1)
    visited = [0 for x in range(N)]
    d = [ 1000000 for x in range(N) ]
    d[X] = 0
    q = []
    a = X
    heapq.heappush(q, [0, a])
    while q:
        dis, a = heapq.heappop(q)
        if visited[a]: continue
        for neighbor in l[a]:
            if not visited[neighbor]:
                d[neighbor] = min(d[neighbor], d[a] + 1)
                heapq.heappush(q, [d[neighbor], neighbor])
        visited[a] = 1

    flag = False
    for i, dis in enumerate(d, start=1):
        if dis == K:
            print(i)
            flag = True
    if not flag:
        print(-1)

main()      
