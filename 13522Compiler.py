import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

# PH : 레지스터의 값을 복사해 스택에 넣음
# PL : 스택에서 하나 빼 레지스터로 넣음
# AD : 스택에서 맨위 두개빼서 합쳐서 스택에 넣음
# ZE : 레지스터를 0으로 만듦 -> N==0인 경우 제외하고 안 쓸 예정
# ST : 레지스터를 1로 만듦
# DI : 디스플레이하고 종료

visited = [[0 for _ in range(256)] for l in range(512)] # 숫자, 레지스터

def ans(N):
    queue = deque([[['ST', 'PH'], [1], 1]]) # 누적된 명령어들, 스택, 현재 레지스터에 저장된 숫자
    if N == 0:
        print('ZE X')
        print('DI X')

    if N == 1:
        print('ST X')
        print('DI X')
        return

    for j in range(36): # 이 줄은 없어도 될?듯합니다
        for _ in range(len(queue)):
            commands, stack, register = queue.popleft()
            sum_num = sum(stack)
            visited[sum_num][register] = 1
            
            if sum_num == N: # 종료 조건
                for command in commands:
                    if command == 'AD': # AD면 AD만 출력
                        print('AD')
                    else:
                        print(command + ' ' + 'X') # 그 외의 명령어일 땐 {명령어} X 형식
                for i in range(len(stack)-1): # 스택 안에 있는거 다 AD해준 뒤 레지스터로 옮겨(PL) 디스플레이(DI)
                    print('AD')
                print('PL' + ' ' + 'X')
                print('DI' + ' ' + 'X')
                return
            
            elif sum_num < N:
                if len(commands) + len(stack) + 2 <= 40: # 40줄이 넘지 않을 것 같을때만
                    # AD
                    if len(stack) >= 2:
                        tmp = stack[-1] + stack[-2]
                        # if not visited[sum(stack[:-2]) + tmp][register]:
                        queue.append([commands + ['AD'], stack[:-2] + [tmp], register]) # AD

                    # PH
                    if not visited[sum_num + register][register]:
                        queue.append([commands + ['PH'], stack + [register], register]) # 레지스터에있는거 스택에넣음

                    # PL
                    if len(stack) > 0:
                        reg = stack[-1]
                        if not visited[sum(stack[:-1])][reg]:
                            queue.append([commands + ['PL'], stack[:-1], reg]) # 스택맨위꺼 빼서 레지스터로

            else: # 스택 숫자들의 합이 정답보다 크면 cut
                continue

ans(N)
