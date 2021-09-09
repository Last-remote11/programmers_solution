from collections import deque
import sys
input = sys.stdin.readline

# 탑의 개수 N, 사정 거리 R, 초기 에너지 D

def get_distance(A, B):
    y1, x1 = A
    y2, x2 = B
    return ((y1-y2)**2 + (x1-x2)**2) ** 0.5

def main():
    ans = 0
    N, R, D, X, Y = map(int, input().split())

    towers = []
    for _ in range(N):
        x, y = map(int, input().split())
        towers.append([y, x])

    linked = [ [0 for _ in range(N)] for _ in range(N) ]
    for i_idx, i in enumerate(towers):
        for j_idx, j in enumerate(towers):
            if get_distance(i, j) <= R:
                linked[i_idx][j_idx] = 1
    for tower_n in range(N):
        visited = [ 0 for _ in range(N) ]
        visited[tower_n] = 1
        queue = deque([])
        queue.append([tower_n, 0]) # 타워번호, 건너뛴횟수

        while queue:
            flag = False
            tower_n, d = queue.popleft()
            loc = towers[tower_n]
            if get_distance(loc, [Y, X]) <= R:
                damage = D
                for _ in range(d):
                    damage = damage*0.5
                ans += damage
                flag = True
            if flag:
                break
            
            else:
                for idx, is_linked in enumerate(linked[tower_n]):
                    if is_linked and not visited[idx]:
                        queue.append([idx, d + 1])
                        visited[idx] = 1
    
    print(round(ans,2))

main()
