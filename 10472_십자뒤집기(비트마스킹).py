from collections import deque
import sys

N = int(input())

def main():
	board = []  
	mydict = {
		0:[0, 1, 3],
		1:[0, 1, 2, 4],
		2:[1, 2, 5],
		3:[0, 3, 4, 6],
		4:[1, 3, 4, 5, 7],
		5:[2, 4, 5, 8],
		6:[3, 6, 7],
		7:[4, 6, 7, 8],
		8:[5, 7, 8],
	}

	for _ in range(3):
		board += sys.stdin.readline().rstrip()
	ansboard = 0
	for i, char in enumerate(board):
		if char == '*':
			ansboard = ansboard | (1 << (8-i))
	q = deque()
	q.append(0)

	visited = [ 0 for _ in range(512)]
	visited[0] = 1
	
	ans = 0
	while q:
		for _ in range(len(q)):
			current = q.popleft()
			if current == ansboard:
				print(ans)
				return
			for i in range(9):
				next = current
				for j in mydict[i]:
					next = next ^ (1 << j)
				if not visited[next]:
					q.append(next)
					visited[next] = 1

		ans += 1
	print('몰라ㅋ')
for _ in range(N):
	main()
