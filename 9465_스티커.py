import sys

input = sys.stdin.readline

def main():

    T = int(input())

    for _ in range(T):
        n = int(input())
        lst1 = list(map(int, input().split()))
        lst2 = list(map(int, input().split()))
        dp = [ [0, 0] for _ in range(n) ]
        if n == 1:
            print(max(*lst1, *lst2))
        else:
            dp[0][0] = lst1[0]
            dp[0][1] = lst2[0]
            dp[1][1] = lst1[0] + lst2[1]
            dp[1][0] = lst1[1] + lst2[0]
            for i in range(2, n):
                dp[i][0] = lst1[i] + max(dp[i-1][1], dp[i-2][0], dp[i-2][1])
                dp[i][1] = lst2[i] + max(dp[i-1][0], dp[i-2][1], dp[i-2][0])
            print(max(dp[-1][0], dp[-1][1], dp[-2][0], dp[-2][1]))
            
main()
