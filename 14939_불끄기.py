import sys
import copy

input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def turn_on(y, x, bulbs):
    temp_bulbs = copy.deepcopy(bulbs)

    temp_bulbs[y] = temp_bulbs[y] ^ (1 << 9 - x) # 누른거동작
    for i in range(4):
        cy, cx = y + dy[i], x + dx[i]
        if 0 <= cx < 10 and 0 <= cy < 10: # 누른거의 위아래왼쪽오른쪽 동작
            temp_bulbs[cy] = temp_bulbs[cy] ^ (1 << 9 - cx)
    return temp_bulbs

def dfs(bulbs, depth, ans):
    # print(depth)
    # print('asd', sum(bulbs))
    for i in range(10):
        if bulbs[depth-1] & (1 << 9-i):
            bulbs = turn_on(depth, i, bulbs)
            ans += 1
    if depth == 9:
        if sum(bulbs) == 0: # 다꺼짐
            print(ans)
            exit()
        else:
            return
    dfs(bulbs, depth+1, ans)
        

def main():

    bulbs = []
    for _ in range(10):
        line = input()
        t = 0
        for i, c in enumerate(line):
            if c == "O": # 켜짐
                t = t | ( 1 << (9 - i))
        bulbs.append(t)
    
    for i in range(1024):
        temp = copy.deepcopy(bulbs)
        ans = 0
        for j in range(10):
            if i & ( 1 << 9-j):
                temp = turn_on(0, j, temp)
                ans += 1
        # print(i, bin(i) , ans)
        dfs(temp, 1, ans)
    print(-1)
main()
