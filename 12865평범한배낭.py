import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

wv_arr = []
for _ in range(n):
    wv_arr.append(list(map(int, input().split())))

dp = [0] * (k + 1)
for w, v in wv_arr:
    if w <= k:
        temp = deque()
        for i in range(1, k - w + 1):
            temp.append(max(dp[i + w], dp[i] + v))
        # print(temp)
        dp[w] = max(dp[w], v)
        for i in range(k - w):
            dp[i + w + 1] = temp.popleft()

    # print(dp)

print(max(dp))
