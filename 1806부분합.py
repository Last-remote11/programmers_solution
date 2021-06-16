n, s = map(int, input().split())
arr = list(map(int, input().split()))

ans = 1000000
right, left = 0, 0
temp_sum = 0

while True:

    if temp_sum >= s:
        ans = min(ans, right - left)
        temp_sum -= arr[left]
        left += 1
    
    elif right == n:
        break

    else:
        temp_sum += arr[right]
        right += 1

print(ans if ans != 1000000 else 0)
