from collections import deque


def bfs():
    q = deque()
    q.append(N)
    visited[N][0] = 0
    visited[N][1] = 1

    while q:
        x = q.popleft()

        for next in (x + 1, x - 1, 2 * x):
            if 0 <= next <= 100000:
                if visited[next][0] == -1:
                    visited[next][0] = visited[x][0] + 1
                    visited[next][1] = visited[x][1]
                    q.append(next)

                elif visited[next][0] == visited[x][0] + 1:
                    visited[next][1] += visited[x][1]

    print(visited[K][0])
    print(visited[K][1])


N, K = map(int, input().split())
visited = [[-1, 0] for _ in range(100001)]
bfs()
