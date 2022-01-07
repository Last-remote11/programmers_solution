import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

def main():

    n = int(input())
    m = []
    for _ in range(n):
        m.append(list(map(int, input().split())))
    dp = [ [0 for x in range(n)] for x in range(n) ]
    ans = 0

    def dfs(y, x):
        if dp[y][x]:
            return dp[y][x]
        dp[y][x] = 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if m[y][x] < m[ny][nx]:
                    dp[y][x] = max(dp[y][x], dfs(ny, nx) + 1)
        
        return dp[y][x]
    
    for y in range(n):
        for x in range(n):
            ans = max(ans, dfs(y, x))

    print(ans)

main()
