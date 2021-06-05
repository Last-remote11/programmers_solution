import sys
from collections import deque

M, N = map(int, input().split()) # M-행 N-열 
maze = []
for _ in range(N):
	maze.append(list(map(int, sys.stdin.readline().strip())))
d = [[-1] * M for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1] # 4방향

q = deque()

q.append((0, 0))
d[0][0] = 0 # 다익스트라 행렬

while q:
	x, y = q.popleft()
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if 0 <= nx < N and 0 <= ny < M:
			if d[nx][ny] == -1:
				if maze[nx][ny] == 0:
					d[nx][ny] = d[x][y]
					q.appendleft((nx, ny))
				else:
					d[nx][ny] = d[x][y] + 1
					q.append((nx, ny))
print(d[N-1][M-1])
