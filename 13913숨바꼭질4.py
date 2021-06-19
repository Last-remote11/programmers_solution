from collections import deque

def path(x):
    arr = []
    temp = x
    for _ in range(dist[x] + 1):
        arr.append(temp)
        temp = move[temp]
    print(' '.join(map(str, arr[::-1])))
    # 지나온 노드들을 바탕으로 부모 노드를 차례대로
    # move에서 조회하여 역순으로 출력

def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(dist[x])
            path(x)
            return x
        for i in (x+1, x-1, 2*x): # i: 다음노드, x: 부모노드
            if 0<=i<=100000 and dist[i]==0:
                q.append(i)
                dist[i] = dist[x] + 1
                move[i] = x

N, K = map(int, input().split())
dist = [0]*100001
move = [0]*100001
bfs()
