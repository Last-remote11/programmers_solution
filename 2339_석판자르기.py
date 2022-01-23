import sys
input = sys.stdin.readline

N = int(input())
board = [ [int(x) for x in input().split()] for _ in range(N)]
ans = 0

def cut(piece, direction):
    ans = 0
    '''
    나눈 조각이 불순물도 없고 보석도 한개만 있으면 return
    아니면 재귀적으로 cut 다시 사용
    direction 0-가로 1-세로
    '''
    jew = 0
    dirt = 0
    for r in piece:
        for i in r:
            if i == 2:
                jew += 1
            if i == 1:
                dirt += 1

    if jew == 0:# 보석이 없는 석판
        return False
    if jew == 1 and dirt == 0:# 더 이상 자를 필요가 없는 석판
        return True

    if direction == 0:
        for r, line in enumerate(piece):
            if r == 0 or r == len(piece)-1: continue # 두 조각으로 잘리지 않는 경우
            for i in line:
                if i == 1:
                    jew_inside = False
                    for j in line:
                        if j == 2: jew_inside = True
                    if not jew_inside:
                        piece_1 = piece[:r]
                        piece_2 = piece[r+1:]
                        if cut(piece_1, 1) and cut(piece_2, 1):
                            ans += cut(piece_1, 1) * cut(piece_2, 1)
    elif direction == 1:
        for c in range(len(piece[0])):
            if c == 0 or c == len(piece[0])-1: continue
            line = map(lambda x: x[c], piece) # 세로줄
            for i in line:
                if i == 1:
                    jew_inside = False
                    for j in line:
                        if j == 2: jew_inside = True
                    if not jew_inside:
                        piece_1 = list(map(lambda x: x[:c], piece))
                        piece_2 = list(map(lambda x: x[c+1:], piece))
                        if cut(piece_1, 0) and cut(piece_2, 0):
                            ans += cut(piece_1, 0) * cut(piece_2, 0)
    return ans
jew=0
dirt=0
for r in board:
    for i in r:
        if i == 2:
            jew += 1
        if i == 1:
            dirt += 1

if jew==1 and dirt == 0:
    print(1)

else:
    ans += cut(board, 1)
    ans += cut(board, 0)

    if ans == 0:
        print(-1)
    else:
        print(ans)
