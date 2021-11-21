import sys

input = sys.stdin.readline

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


h, w = map(int, input().split())
maze = []
visited = [[0] * w for _ in range(h)]
exit = [[0] * w for _ in range(h)]

for _ in range(h):
    maze.append([x for x in input().rstrip()])
    
def main():
    ans = 0

    for i in range(h):
        for j in range(w):
            if not visited[i][j]:
                temp = [[i, j]]
                cy, cx = i*1, j*1
                loop = 1
                while True:
                    try:
                        if cy < 0 or cx < 0:
                            raise IndexError
                        haha = maze[cy][cx]

                        if exit[cy][cx]:
                            visited[cy][cx] = 1
                            ans += loop-1
                            for y, x in temp:
                                exit[y][x] = 1
                            break

                        if visited[cy][cx]: break
                        visited[cy][cx] = 1
                            
                        if maze[cy][cx] == "U": 
                            cy, cx = cy-1, cx
                        elif maze[cy][cx] == "D": 
                            cy, cx = cy+1, cx
                        elif maze[cy][cx] == "R": 
                            cy, cx = cy, cx+1
                        else: 
                            cy, cx = cy, cx-1
                        temp.append([cy*1, cx*1])
                        loop += 1

                    except IndexError:
                        ans += loop-1
                        for y, x in temp:
                            if 0 <= y < h and 0 <= x < w:
                                exit[y][x] = 1
                        break
    print(ans)
main()
