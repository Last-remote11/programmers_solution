import sys
from itertools import combinations, permutations

input = sys.stdin.readline

n = int(input())
s = []
ans = 10**7

for _ in range(n):
    s.append(list(map(int, input().split())))

people = [x for x in range(n)]

for team_a in combinations(people, int(n/2)):
    score_a = 0
    score_b = 0
    team_b = people.copy()
    for i in team_a:
        team_b.remove(i)

    for i, j in permutations(team_a, 2):
        score_a += s[i][j]
    for i, j in permutations(team_b, 2):
        score_b += s[i][j]

    ans = min(ans, abs(score_a - score_b))

print(ans)
