import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

def main():

    V, E = map(int, input().split()) # 정점, 간선의 갯수
    K = int(input()) # 출발
    K -= 1
    d = [ 1<<18 for x in range(V) ]
    d[K] = 0
    visited = [0 for x in range(V)]
    l = defaultdict(list)

    for _ in range(E):
        a, b, dis = map(int, input().split())
        l[a-1].append([b-1, dis])

    hq = []
    heapq.heappush(hq, [0, K])
    
    while hq:
        dis, a = heapq.heappop(hq)
        if visited[a]: continue
        for b, p in l[a]:
            if not visited[b]:
                d[b] = min(d[b], d[a] + p)
                heapq.heappush(hq, [d[b], b])
        visited[a] = 1
    for i in d:
        print(i if i != 1<<18 else "INF")

main()      
