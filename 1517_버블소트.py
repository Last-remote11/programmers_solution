import sys
input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
swap = 0

def merge(left, right):
    global swap
    result = []
    lp, rp = 0, 0
    while lp != len(left) or rp != len(right):
        if left[lp] <= right[rp]:
            result.append(left[lp])
            lp += 1
            if lp == len(left): 
                for i in right[rp:]:
                    result.append(i)
                break
        elif left[lp] > right[rp]: 
            result.append(right[rp])
            rp += 1
            swap += len(left) - lp
            if rp == len(right): 
                for i in left[lp:]:
                    result.append(i)
                break
    return result

def main():

    N = int(input())
    l = list(map(lambda x: [x], map(int,input().split())))

    while len(l) > 1:
        next_l = []
        for i in range(0, len(l), 2):
            try: 
                next_l.append(merge(l[i], l[i+1]))
            except IndexError:
                next_l.append(l[i])
        l = next_l
        # print(l, swap)
    print(swap)

main()
