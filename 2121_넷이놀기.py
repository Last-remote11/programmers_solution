import sys

input = sys.stdin.readline


def main():
    N = int(input())
    ans = 0
    w, h = map(int, input().split())
    myset = set([])
    for _ in range(N):
        myset.add(input().rstrip())
    
    for i in myset:
        x, y = map(int, i.split())
        nx, ny = x + w, y + h
        if (
            str(x) + ' ' + str(ny) in myset and
            str(nx) + ' ' + str(y) in myset and
            str(nx) + ' ' + str(ny) in myset
        ):
            ans += 1
    print(ans)
main()
