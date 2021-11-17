import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

M = []
visited = [[0] * 5 for _ in range(5)]

for _ in range(5):
    M.append(input())

def is_connected(start, temp):
    v = 1
    q = deque([start])
    temp[start[0]][start[1]] = 0
    while q:
        cr, cc = q.popleft()
        for i in range(4):
            nr, nc = cr + dy[i], cc + dx[i]
            if 0 <= nr < 5 and 0 <= nc < 5:
                if temp[nr][nc]:
                    q.append([nr, nc])
                    v += 1
                    temp[nr][nc] = 0
    if v == 7:
        return True
    else:
        return False

def main():
    ans = 0

    for c in combinations(range(25), 7):
        temp = [[0] * 5 for _ in range(5)]
        num_s = 0
        seats = list(map(lambda x: [x//5, x%5], c))
        for y, x in seats:
            temp[y][x] = 1
            if M[y][x] == "S":
                num_s += 1
        if is_connected(seats[0], temp) and num_s >= 4:
            ans += 1
    print(ans)
                
main()
