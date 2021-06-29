import sys
import copy

input = sys.stdin.readline

h, w = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(h)]

# 0,1,2,3 북 동 남 서
def observe(temp_office, loc, d):
    nr, nc = loc

    if d == 0 and nr > 0:
        nr -= 1
        while temp_office[nr][nc] != 6:
            if temp_office[nr][nc] == 0:
                temp_office[nr][nc] = 7
            nr -= 1
            if nr == -1:
                break
    if d == 1 and nc < w - 1:
        nc += 1
        while temp_office[nr][nc] != 6:
            if temp_office[nr][nc] == 0:
                temp_office[nr][nc] = 7
            nc += 1
            if nc == w:
                break
    if d == 2 and nr < h - 1:
        nr += 1
        while temp_office[nr][nc] != 6:
            if temp_office[nr][nc] == 0:
                temp_office[nr][nc] = 7
            nr += 1
            if nr == h:
                break
    if d == 3 and nc > 0:
        nc -= 1
        while temp_office[nr][nc] != 6:
            if temp_office[nr][nc] == 0:
                temp_office[nr][nc] = 7
            nc -= 1
            if nc == -1:
                break
    return temp_office


cctvs = []
arr = []

for i in range(h):
    for j in range(w):
        cell = office[i][j]
        if cell not in (0, 5, 6, 7):
            arr.append(cell)
            cctvs.append([i, j])
        elif cell == 5:
            for k in range(4):
                office = observe(office, [i, j], k)

q = []


def dfs(temp, depth):
    if depth == len(arr):
        q.append(temp)
        return

    if arr[depth] != 2:
        for i in range(4):
            dfs(temp + [i], depth + 1)
    else:
        dfs(temp + [0], depth + 1)
        dfs(temp + [1], depth + 1)


dfs([], 0)
ans = 100
for cq in q:
    this_office = copy.deepcopy(office)
    idx = 0
    for loc, d in zip(cctvs, cq):
        if arr[idx] == 1:
            this_office = observe(this_office, loc, d)
        elif arr[idx] == 2:
            this_office = observe(this_office, loc, d)
            this_office = observe(this_office, loc, (d + 2) % 4)
        elif arr[idx] == 3:
            this_office = observe(this_office, loc, d)
            this_office = observe(this_office, loc, (d + 1) % 4)
        elif arr[idx] == 4:
            this_office = observe(this_office, loc, (d + 0) % 4)
            this_office = observe(this_office, loc, (d + 1) % 4)
            this_office = observe(this_office, loc, (d + 2) % 4)
        idx += 1  # 이거빼먹어서 오래걸림
    n_zero = 0
    for i in range(h):
        for j in range(w):
            if this_office[i][j] == 0:
                n_zero += 1
    ans = min(ans, n_zero)
print(ans)
