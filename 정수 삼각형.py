def solution(triangle):
    
    if len(triangle) == 1:
        return triangle[0][0]

    myList = list(range(1, len(triangle)))
    myList.reverse()
    for line in myList:
        for i, j in enumerate(triangle[line][:-1]):
            triangle[line-1][i] += max(j, triangle[line][i+1])

    return triangle[0][0]
