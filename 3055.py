import sys
from collections import deque

N, M = map(int, input().split()) # N-행(y) M-열(x) 
arr = []
for _ in range(N):
	row = list(sys.stdin.readline().strip())
	for i, j in enumerate(row):
		if j == 'D':
			D = [_, i]
		if j == 'S':
			S = [_, i]
	arr.append(row)
dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs(start):
	q = deque()
	q.append(start)
	visited = [[0 for i in range(M)] for j in range(N)]
	visited[start[0]][start[1]] = 1
	depth = 0
	while q:
		depth += 1
		water = []
		for i in range(N):
			for j in range(M):
				if arr[i][j] == '*':
					water.append([i,j])
		for i, j in water:
			for k in range(4):
				ni = i + dy[k]
				nj = j + dx[k]
				if 0 <= ni < N and 0 <= nj < M:
					if arr[ni][nj] == '.':
						arr[ni][nj] = '*'
		for _ in range(len(q)):
			y, x = q.popleft()
			for i in range(4):
				ny = y + dy[i]
				nx = x + dx[i]
				if 0 <= ny < N and 0 <= nx < M:
					if arr[ny][nx] == '.' and visited[ny][nx] == 0:
						visited[ny][nx] = 1
						q.append([ny, nx])
					elif arr[ny][nx] == 'D':
						return depth
	return 'KAKTUS'

print(bfs(S))
