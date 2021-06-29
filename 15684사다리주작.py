from itertools import combinations

n, m, h = map(int, input().split())

vertical = [list(map(int, input().split())) for _ in range(m)] # 이미 존재하는 가로줄



board = [[0] * (n * 2 - 1) for _ in range(h + 1)] 
width = (n * 2) - 1

for i in range(h + 1):
    for j in range(len(board[0])):
        if j % 2 == 0:
            board[i][j] = 1
# 구현을 쉽게 하기 위해 세로줄들 사이를 0으로 채운 새로운 배열을 만들어준다.
# 이러면 짝수 번째(0부터센다면) 열에 있는 1들은 세로줄이 되고 홀수 번째 열에 있는 1은 가로줄이 된다.
# 또한 편의를 위해 맨 아래에 가로선없는 행을 하나 더 추가해준다

convert_v = list(map(lambda x: [x[0] - 1, (x[1] * 2) - 1], vertical))
for r, c in convert_v:
    board[r][c] = 1
# 새로 만든 배열에 맞게 이미 존재하는 가로줄의 좌표들도 수정해준 다음 추가


def is_equal(i): # 시작열과 끝열이 같은지 확인하는 함수
    cr, cc = 0, i * 1
    while cr < h + 1:
        if cc < width - 1:
            if board[cr][cc + 1] == 1:  # 오른쪽 가로선
                cc += 2
                cr += 1
                continue
        if cc > 1:
            if board[cr][cc - 1] == 1:  # 왼쪽 가로선
                cc -= 2
                cr += 1
                continue
            # 가로선이 없음
        cr += 1
    if cc == i:
        return True
    else:
        return False


mylist = []  # 가로선놓을수있는칸(좌표)

# 가로선을 놓는 것이 가능한 좌표들을 수집한다.
# 만약 같은 행에 반대 방향에 이미 가로선이 있다면 가로선을 놓을 수 없다.
# (가로선이 왼쪽 오른쪽 동시에 나오면 안됨)
for r in range(h): 
    for c in range(1, width, 2):
        if n == 2:
            if board[r][c] == 0:
                mylist.append([r, c])
        elif c == 1:
            if board[r][c] == 0 and board[r][c + 2] == 0:
                mylist.append([r, c])
        elif c == width - 2:
            if board[r][c] == 0 and board[r][c - 2] == 0:
                mylist.append([r, c])
        else:
            if board[r][c] == 0 and board[r][c - 2] == 0 and board[r][c + 2] == 0:
                mylist.append([r, c])


def solve():

    if m == 0:
        return 0 # 가로선이 하나도 없으면 굳이 가로줄을 놓을 필요가 없다.
    equal = True 
    
    for i in range(0, width, 2): # 기존에 가로선이 있지만 가로선을 추가하지 않아도 조건을 만족하는 경우
        if not is_equal(i):
            equal = False
            break
    if equal == True:
        return 0

    for num in range(1, 4):  # num : 놓을 가로선 수(1, 2, 3)

        for comb in combinations(mylist, num): 
          # 가로선을 놓을 수 있는 좌표들 중에서 중복없이 num개만큼 고른다.
            equal = True
            for r, c in comb:  # 가로선설치
                board[r][c] = 1

            for i in range(0, width, 2):
                if not is_equal(i):
                    equal = False
                    break
            if equal == True:
                return num

            for r, c in comb:  # 가로선철거
                board[r][c] = 0
    return -1


print(solve())
