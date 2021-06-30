import sys
from itertools import combinations

n, m = map(int, input().split())

city = []
chickens = []
homes = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 1:
            homes.append([i, j])
        elif line[j] == 2:
            chickens.append([i, j])
    city.append(line)
ans = sys.maxsize

for comb in combinations(chickens, m):
    temp = 0
    for home in homes:
        d = 1000
        for c in comb:
            d = min(d, abs(home[0] - c[0]) + abs(home[1] - c[1]))
        temp += d
    ans = min(ans, temp)

print(ans)
