n, k = map(int, input().split())

coins = []
for i in range(n):
    coins.append(int(input()))

dp = [0 for _ in range(k + 1)]

for i in range(1, k + 1):
    a = []
    for coin in coins:
        if coin <= i and dp[i - coin] != -1:
            a.append(dp[i - coin])
    if not a:
        dp[i] = -1  # 못만듦
    else:
        dp[i] = min(a) + 1

print(dp[k])
