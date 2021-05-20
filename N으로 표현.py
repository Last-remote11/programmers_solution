def solution(N, number):
    
    if N == number:
        return 1
    
    s = [ set() for x in range(0, 8) ]
    for i, x in enumerate(s, start = 1):
        x.add(int(str(N) * i))
    
    for i in range(1, 8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if (op2 != 0):
                        s[i].add(op1 // op2)
        
        if (number in s[i]):
            return i + 1
    
    return -1

# N을 1번 쓴 것부터 8번 쓴 것 까지 각각의 집합을 차례로 만듦
# N을 i번 쓴 것의 집합은 i-1번 쓴 것의 집합의 각 원소에
# 더하기, 빼기, 곱하기, 나누기를 한 것과 N을 i번 붙인 수를 추가한 것이다.
# 집합을 만들 때 마다 찾고자 하는 값이 새로 만들어진 집합에 있는지 확인
