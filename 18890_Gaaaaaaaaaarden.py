import sys
from itertools import combinations
from collections import deque
import copy

input = sys.stdin.readline

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

Garden = []
visited = [[0] * 5 for _ in range(5)]

h, w, G, R = map(int, input().split())
avail = []

for _ in range(h):
    line = list(map(int, input().split()))
    for i, char in enumerate(line):
        if char == 2:
            avail.append([_, i])
        if char != 0:
            line[i] = 0
        else:
            line[i] = "L"
    Garden.append(line)
l = list(range(len(avail))) # 배양액놓기가능한점의 수

def sim(reds, greens):
    flowers = 0

    temp_G = copy.deepcopy(Garden)
    redq = deque(reds)
    greenq = deque(greens)

    for red in reds:
        temp_G[red[0]][red[1]] = -1
    for green in greens:
        temp_G[green[0]][green[1]] = 1

    while redq or greenq:
        try:
            for _ in range(len(redq)):
                cy, cx = redq.popleft()
                if temp_G[cy][cx] == "F": continue
                for i in range(4):
                    ny, nx = cy + dy[i], cx + dx[i]
                    if 0 <= ny < h and 0 <= nx < w:
                        if temp_G[ny][nx] not in ["F", "L"]:
                            if temp_G[ny][nx] == 0:
                                temp_G[ny][nx] = temp_G[cy][cx] - 1
                                redq.append([ny, nx])
                                
        except:pass
        try:
            for _ in range(len(greenq)):
                cy, cx = greenq.popleft()
                for i in range(4):
                    ny, nx = cy + dy[i], cx + dx[i]
                    if 0 <= ny < h and 0 <= nx < w:
                        if temp_G[ny][nx] not in ["F", "L"]:
                            if temp_G[ny][nx] == 0:
                                temp_G[ny][nx] = temp_G[cy][cx] + 1
                                greenq.append([ny, nx])
                            elif temp_G[ny][nx] + temp_G[cy][cx] + 1 == 0:
                                temp_G[ny][nx] = "F"
                                flowers += 1
        except:pass
    
    return flowers




def main():
    ans = 0

    for reds_idx in combinations(l, R):
        temp = set(l)
        for i in reds_idx:
            temp.remove(i)
        for greens_idx in combinations(temp, G):
            reds = [avail[x] for x in reds_idx]
            greens = [avail[x] for x in greens_idx]

            flowers = sim(reds, greens)
            ans = max(ans, flowers)

    print(ans)
                
main()
