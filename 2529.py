k = int(input())
arr = input().split()

max = -1
min = -1

def dfs(num, depth):
    global min, max
    if depth == k+1:
        min = ''.join(str(x) for x in num) if min == -1 else min
        max = ''.join(str(x) for x in num)
        return
    else: 
        for i, j in enumerate(visited):
            if not j:
                if arr[depth-1] == '<':
                    if num[-1] < i:
                        visited[i] = True
                        dfs(num + [i], depth+1)
                        visited[i] = False
                elif arr[depth-1] == '>':
                    if num[-1] > i:
                        visited[i] = True
                        dfs(num + [i], depth+1)
                        visited[i] = False

for h in range(10):
    visited = [False] * 10
    visited[h] = True
    dfs([h], 1)

print(max)
print(min)
