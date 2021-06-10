field = []
zeros = []

row_arr = [[0]*10 for _ in range(9)]
col_arr = [[0]*10 for _ in range(9)]
section = [[0]*10 for _ in range(9)]

for _ in range(9):
    row = list(map(int, input().split()))
    for i in range(9):
        if row[i] == 0:
            zeros.append([_, i])
        else:
            row_arr[_][row[i]] = 1
            col_arr[i][row[i]] = 1
            section[_//3*3 + i//3][row[i]] = 1
    field.append(row)

zeros_len = len(zeros) # 빈칸들

def fill_num(filled):

    if filled == zeros_len:
        for ans_row in field:
            print(' '.join(str(x) for x in ans_row))
        exit()
    i, j = zeros[filled]

    for num in range(1,10):
        if not row_arr[i][num] and not col_arr[j][num] and not section[i//3*3 + j//3][num]:

            row_arr[i][num] = col_arr[j][num] = section[i//3*3 + j//3][num] = 1
            field[i][j] = num
            fill_num(filled + 1)
            row_arr[i][num] = col_arr[j][num] = section[i//3*3 + j//3][num] = 0
            field[i][j] = 0
filled = 0
fill_num(0)
