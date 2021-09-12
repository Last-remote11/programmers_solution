from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

dy1 = [-1, 0, 1, 1, 0, -1]  # 짝수행 -> 홀수행
dx1 = [-1, -1, -1, 0, 1, 0]
dy2 = [-1, 1, 0, 0, 1, -1]  # 홀수행 -> 짝수행
dx2 = [0, 0, -1, 1, 1, 1]

tiles = [[[[] for _ in range(2)] for _ in range(N)] for _ in range(N)]
paths = [[[] for _ in range(N)] for _ in range(N)]
steps = [[0 for _ in range(N)] for _ in range(N)]
steps[0][0] = 1

def main():

    for i in range(N):
        if i % 2 == 0:
            for j in range(N):
                tiles[i][j] = list(map(int, input().split()))
        else:
            for j in range(N-1):
                tiles[i][j] = list(map(int, input().split()))
    q = deque([])
    q.append([0,0])
    while q:
        cy, cx = q.popleft()
        if cy % 2 == 0: # 짝수행 -> 홀수행
            for i in range(6):
                ny, nx = cy + dy1[i], cx + dx1[i]
                if 0 <= ny < N and 0 <= nx < N:
                    if steps[ny][nx] == 0: 
                        if dx1[i] >= 0 and tiles[cy][cx][1] == tiles[ny][nx][0]:# 오른쪽이동
                            q.append([ny, nx])
                            steps[ny][nx] = steps[cy][cx] + 1
                            paths[ny][nx] = [cy, cx]
                        elif dx1[i] < 0 and tiles[cy][cx][0] == tiles[ny][nx][1]:
                            q.append([ny, nx])
                            steps[ny][nx] = steps[cy][cx] + 1
                            paths[ny][nx] = [cy, cx]
        else: # 홀수행 -> 짝수행
            for i in range(6):
                ny, nx = cy + dy2[i], cx + dx2[i]
                if 0 <= ny < N and 0 <= nx < N:
                    if steps[ny][nx] == 0:
                        if dx2[i] > 0 and tiles[cy][cx][1] == tiles[ny][nx][0]:
                            q.append([ny,nx])
                            steps[ny][nx] = steps[cy][cx] + 1
                            paths[ny][nx] = [cy, cx]
                        elif dx2[i] <= 0 and tiles[cy][cx][0] == tiles[ny][nx][1]:
                            q.append([ny, nx])
                            steps[ny][nx] = steps[cy][cx] + 1
                            paths[ny][nx] = [cy, cx]


yx_to_label = [ [0 for _ in range(N)] for _ in range(N) ]
label = 1
for i in range(N):
    for j in range(N):
        if i % 2 == 1 and j == N - 1:
            continue
        yx_to_label[i][j] = label
        label += 1

main()
flag, ans = 0, []
for i in range(N-1, -1, -1):
    for j in range(N-1, -1, -1):
        if steps[i][j]:
            print(steps[i][j])
            ans.append(yx_to_label[i][j])
            y, x = i, j
            while y > 0 or x > 0:
                ny, nx = paths[y][x]
                ans.append(yx_to_label[ny][nx])
                y, x = ny, nx
            flag = 1
            break
    if flag:
        break

ans.reverse()
for i in ans:
    print(i, end=' ')
