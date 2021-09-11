from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

def main():

	l = int(input())
	board = []
	ans = 0

	dy = [1, 1, 1, 0 ,0 ,-1, -1, -1]
	dx = [1, 0, -1, 1 ,-1 ,1, 0, -1]

	for _ in range(l):
		line = list(input())
		board.append(line[:-1])
	for y in range(l):
		for x in range(l):
			if board[y][x] == 'w':
				q = deque([])
				q.append([y, x])
				while q:
					cy, cx = q.popleft()
					for i in range(8):
						ny, nx = cy + dy[i], cx + dx[i]
						if 0<=ny<l and 0<=nx<l:
							if board[ny][nx] == '-':
								q.append([ny, nx])
								board[ny][nx] = 'w'
								ans += 1
	print(ans)

for _ in range(N):
	main()
