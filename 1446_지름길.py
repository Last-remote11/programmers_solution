import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

def main():

    N, D = map(int, input().split())    
    
    d = [ x for x in range(D+1) ]
    visited = [ 0 for x in range(D+1) ]
    l = defaultdict(list)
    q = []
    for _ in range(N):
        a, b, dis = map(int, input().split())
        if b > D: continue
        l[a].append([b, dis])
    
    heapq.heappush(q, [0, 0])
    while q:
        dis, a = heapq.heappop(q)
        if visited[a]: continue
        temp = [[a+1, 1]] if a < D else []
        for i in l[a]: 
            temp.append(i) # a 노드와 연결되어 있는 노드들. a와 b의 거리
        for b, p in temp:
            d[b] = min(d[b], d[a] + p)
            heapq.heappush(q, [d[b], b]) # 원점과의 거리, 노드번호
        visited[a] = 1
    print(d[D])
main() 
