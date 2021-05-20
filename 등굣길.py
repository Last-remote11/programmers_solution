def solution(m, n, puddles):

    myMap = [ [ 0 for i in range(m) ] for j in range(n) ]
    myMap[0][0] = 1
    
    for row in range(n):
        for col in range(m):
            if [col+1, row+1] in puddles:
                myMap[row][col] = 0
                continue
            if row == 0:
                prevRow = 0
            else:
                try: 
                    prevRow = myMap[row-1][col]
                except:
                    prevRow = 0
            if col == 0:
                prevCol = 0
            else:
                try: 
                    prevCol = myMap[row][col-1]
                except:
                    prevCol = 0
            myMap[row][col] += prevRow + prevCol
    return myMap[n-1][m-1] % 1000000007
