n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().strip())))

ans = -1
# 1 = 가로로자름, 0 = 세로로자름
for bit in range(1 << (n * m)):
    sum = 0
    # 세로 합 구하기
    for ri in range(n):
        line_sum = 0
        for ci in range(m):
            idx = ri * m + ci # 종이를 일렬로 늘였을 때 현재 위치
            if bit & (1 << idx): # 가로로자른거 만나면 전에꺼 더하고 초기화
                sum += line_sum
                line_sum = 0
            else:
                line_sum = 10 * line_sum + board[ri][ci]
        sum += line_sum
    # 가로 합 구하기
    for ci in range(m):
        line_sum = 0
        for ri in range(n):
            idx = ri * m + ci
            if bit & (1 << idx):
                line_sum = 10 * line_sum + board[ri][ci]
            else:
                sum += line_sum
                line_sum = 0            
        sum += line_sum
    ans = max(ans, sum)

print(ans)
