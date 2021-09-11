from collections import deque
import sys
input = sys.stdin.readline


def main():
	N = int(input())
	board = [ list(map(int,input().split())) for _ in range(N) ]

	q = deque()
	q.append([0, 0])
	while q:
		cy, cx = q.popleft()
		j = board[cy][cx] # 점프력
		if j == 0:
			continue
		elif j == -1:
			print('HaruHaru')
			return
		else:
			if cy + j < N:
				q.append([cy+j, cx])
			if cx + j < N:
				q.append([cy, cx+j])
	print('Hing')

main()
