import sys
from itertools import combinations

input = sys.stdin.readline

def detected(hall, teacher):
    for y, x in teacher:
        u = [[i, x] for i in reversed(range(y))]
        d = [[i, x] for i in range(y, len(hall))]
        r = [[y, i] for i in range(x, len(hall))]
        l = [[y, i] for i in reversed(range(x))]
        for direct in [u, d, r, l]:
            for c in direct:
                if hall[c[0]][c[1]] == "S":
                    return True
                elif hall[c[0]][c[1]] == "O":
                    break
    return False
    

def main():

    hall = []
    binkan = []
    teacher = []
    N = int(input())

    for _ in range(N):
        line = input().split()
        for i, o in enumerate(line):
            if o == "X":
                binkan.append([_, i])
            elif o == "T":
                teacher.append([_, i])
        hall.append(line)
    for a, b, c in combinations(binkan, 3):
        hall[a[0]][a[1]] = 'O'
        hall[b[0]][b[1]] = 'O'
        hall[c[0]][c[1]] = 'O'
        if not detected(hall, teacher):
            print('YES')
            return
        hall[a[0]][a[1]] = 'X'
        hall[b[0]][b[1]] = 'X'
        hall[c[0]][c[1]] = 'X'        
    print("NO")
    
main()
