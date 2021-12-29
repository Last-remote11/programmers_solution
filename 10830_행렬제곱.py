import sys
input = sys.stdin.readline

def product(matrix1, matrix2):

    n = len(matrix1)
    ans = [ [ 0 for _ in range(n) ] for _ in range(n) ]
    for y in range(n):
        for x in range(n):
            tmp = 0
            for i in range(n):
                tmp += matrix1[y][i] * matrix2[i][x]
            ans[y][x] = tmp % 1000

    return ans

def main():

    N, B = map(int, input().split())
    matrix = []
    for _ in range(N):
        line = list(map(int, input().split()))
        matrix.append(line)

    ans = [ [ 0 for _ in range(N) ] for _ in range(N) ]
    for i in range(N):
        ans[i][i] = 1 # 단위행렬

    binary_str = "{0:b}".format(B)
    binary_length = len(binary_str)
    d = dict()

    for i in range(binary_length):
        d[i+1] = matrix
        matrix = product(matrix, matrix)

    for i, b in enumerate(binary_str[::-1]):
        if b == '1':
            ans = product(ans, d[i+1])

    for i in ans:
        print(' '.join(str(x) for x in i))

main()
