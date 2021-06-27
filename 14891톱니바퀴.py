import sys
input = sys.stdin.readline

wheels = [list(map(int, input().strip())) for _ in range(4)]
wheels.insert(0, [])

def move_wheel(wheel, direction):
    if direction == 1:
        wheel.insert(0, wheel.pop())
    if direction == -1:
        wheel.append(wheel.pop(0))
    return wheel

# 오른쪽 2 왼쪽 6
n = int(input())
for _ in range(n):
    w_num, direction = map(int, input().split())
    wheels[w_num] = move_wheel(wheels[w_num], direction)
    for n, i in enumerate(range(w_num, 1, -1), start=1):
        # 문제의 조건에 맞으려면 이미 회전한 바퀴의 회전하기 전 톱니와 다음 바퀴의 현재 톱니를 비교해야 한다
        if (
            wheels[i][6 + int(direction * ((-1) ** (n + 1)))] != wheels[i - 1][2]
        ):
            wheels[i - 1] = move_wheel(wheels[i - 1], direction * (-1) ** n)
        else:
            break # 같은 극이면 반복문을 끝낸다
    for n, i in enumerate(range(w_num, 4), start=1):
        if wheels[i][2 + int(direction * ((-1) ** (n + 1)))] != wheels[i + 1][6]:
            wheels[i + 1] = move_wheel(wheels[i + 1], direction * (-1) ** n)
        else:
            break

score = wheels[1][0] + wheels[2][0] * 2 + wheels[3][0] * 4 + wheels[4][0] * 8
print(score)
