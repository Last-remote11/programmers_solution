from collections import deque
import sys
import copy

input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    board = list(map(int, input().split()))

    switch = dict()
    visited = set()
    visited.add(''.join(str(x) for x in board))

    for i in range(1, K+1):
        switch[i] = list(map(int,input().split()))[1:]

    q = deque([])
    q.append(board)
    ans = 0
    while q:
        for _ in range(len(q)):
            c = q.popleft()
            if len(set(c)) == 1:
                print(ans)
                return 
            for i in range(1, K+1):
                next = copy.deepcopy(c)
                for idx in switch[i]:
                    next[idx-1] = next[idx-1] + i if next[idx-1] + i < 5 else (next[idx-1] + i) % 5
                visit_str = ''.join(str(x) for x in next)
                if visit_str not in visited:
                    q.append(next)
                    visited.add(visit_str)
        ans += 1
    print(-1)

main()
