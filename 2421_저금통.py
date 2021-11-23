import sys
# from itertools import combinations
# from collections import deque
import copy

input = sys.stdin.readline

def main():

    N = int(input())
    if N == 1:
        print(0)
        return
    is_prime = [1 for _ in range(1000000)]
    is_prime[0] = 0
    is_prime[1] = 0
    lognum = int(1000000**0.5)+1
    for i in range(2, lognum):
        if is_prime[i]:
            n = i*1
            while True:
                try:
                    n += i
                    is_prime[n] = 0
                except IndexError:
                    break
                   
    prev_layer = [0]
    for _ in range(1, (N-1)*2 + 1):
        new_layer = [0 for _ in range(_+1)]

        for i in range(len(new_layer)):
            l = prev_layer[i-1] if i != 0 else 0
            r = prev_layer[i] if i != _ else 0
            current_number = int(str(_+1-i) + str(i+1))
            try:is_prime[current_number]
            except:continue
            new_layer[i] = is_prime[current_number] + max(l, r)

        prev_layer = copy.deepcopy(new_layer)
    print(new_layer[N-1])
    
main()
