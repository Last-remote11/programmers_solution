n, k = map(int, input().split())

dp = [0] * (max(n,k)*2+1)
num = 0
for i, idx in enumerate(range(n, k*2+1)):
	dp[idx] = i
for i, idx in enumerate(range(n, -1, -1)):
	dp[idx] = i

for i in range(n+1, k*2):
	if i % 2 == 0:
		dp[i] = min(dp[i], dp[int(i/2)])
	else:
		dp[i] = dp[i-1] + 1
	if i != 0:
		dp[i-1] = min(dp[i-1], dp[i]+1)
print(dp[k])
