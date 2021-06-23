import sys
from collections import deque

input = sys.stdin.readline


def check_nine(str):
    if len(str) <= 2:
        return False
    middle = str[1:-1]
    for i in middle:
        if i != "9":
            return False
    if int(str[0]) + int(str[-1]) == 9:
        return True
    return False


def bfs(n):
    q = deque()
    q.append(1)
    while q:
        koo_int = q.popleft()
        koo = str(koo_int)
        if len(koo) > 100:
            return "BRAK"
        if koo_int % int(n) == 0:
            return koo
        q.append(int(koo + "1"))
        q.append(int(koo + "0"))


def bfs_nine(n):
    q = deque()
    q.append("1")
    while q:
        koo_int = q.popleft()
        koo = str(koo_int)
        if len(koo) <= 5:
            int_koo = int(koo)
            if int_koo % int(n) == 0:
                return koo
            q.append(int(koo + "1"))
            q.append(int(koo + "0"))
        elif 5 < len(koo) < 100:
            if koo_int % int(n) == 0:
                return koo
            q.append(int("1" + koo))
        elif len(koo) >= 100:
            return "BRAK"


t = int(input())
for _ in range(t):

    int_n = int(input())
    n = str(int_n)
    nine = check_nine(n)
    only_nine = True
    for i in n:
        if i != "9":
            only_nine = False
    if only_nine:
        print("111111111" * len(n))
    elif nine:
        print(bfs_nine(n))
    else:
        print(bfs(n))
