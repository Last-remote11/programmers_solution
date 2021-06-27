import sys
from collections import Counter

input = sys.stdin.readline
n, l = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
board_pivot = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        board_pivot[j][i] = board[i][j]


def row_scan(board):
    ans = 0
    for row in board:
        p = True
        lamp = [0] * n  # 경사로가 설치 여부 확인용
        for i in range(n - 1):
            if row[i] == row[i + 1] - 1:  # 오르막(1칸차이)
                if i - l + 1 >= 0:
                    try:
                        if len(Counter(row[i - l + 1 : i + 1])) != 1:  # 높이가 달라 설치 불가
                            p = False
                            break
                        else:
                            if (
                                lamp[i - l + 1 : i + 1].count(0) != l
                            ):  # 경사로가 이미 놓여졌는지 확인하는 조건
                                p = False
                                break
                            else:
                                for h in range(i - l + 1, i + 1):
                                    lamp[h] = 1
                    except IndexError:  # 경사로가 밖으로 나가버린 경우
                        p = False
                        break
                else:
                    p = False
                    break
            elif row[i] == row[i + 1] + 1:  # 내리막(1칸차이)
                try:
                    if len(Counter(row[i + 1 : i + l + 1])) != 1:
                        p = False
                        break
                    else:
                        if (
                            lamp[i + 1 : i + l + 1].count(0) != l
                        ):  # 경사로가 이미 놓여졌는지 확인하는 조건
                            p = False
                            break
                        else:
                            for h in range(i + 1, i + l + 1):
                                lamp[h] = 1
                except IndexError:
                    p = False
                    break
            elif abs(row[i] - row[i + 1]) > 1:
                p = False
                break

        if p:
            ans += 1
    return ans


ans = 0
ans += row_scan(board)
ans += row_scan(board_pivot)
print(ans)
