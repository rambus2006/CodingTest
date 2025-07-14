from collections import deque

n,m = map(int,input().split())
grid = [list(str(input())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

# 이동할 4방향(상,하,좌,우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def getI(grid):
    for row in range(n):
        for col in range(m):
            if grid[row][col] == 'I':
                return row,col

def bfs(start_x,start_y):
    people = 0 
    queue = deque()
    queue.append((start_x,start_y))
    visited[start_x][start_y] = True

    while queue: 
        x,y = queue.popleft()
        # print(f"({x},{y}) 방문완료")

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] != True:
                    if grid[nx][ny] == 'O':
                        queue.append((nx, ny))
                        visited[nx][ny] = True
                    if grid[nx][ny] == 'P':
                        people += 1
                        queue.append((nx, ny))
                        visited[nx][ny] = True

    if people == 0:
        return 'TT'
    return people

start_x,start_y = getI(grid)
people = bfs(start_x,start_y)
print(people)
