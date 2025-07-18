from collections import deque

row,col,k = map(int,input().split())
grid = [[0] * (col) for _ in range(row)]
queue = deque()
for _ in range(k):
    start_x,start_y,end_x,end_y = map(int,input().split())
    queue.append((start_x,start_y,end_x,end_y))
    for w in range(start_x,end_x):
        for h in range(start_y,end_y):
            grid[h][w] += 1
# 여기까지는 잘 만듬 


dx = [0,0,-1,1]
dy = [-1,1,0,0]
visited = [[False] * col for _ in range(row)]
area = []

# bfs 
def FindAreaBFS(st_x,st_y):
    queue = deque()
    queue.append((st_x,st_y))
    cnt = 1
    visited[st_x][st_y] = True
    while queue:
        x,y = queue.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny]:
                if grid[nx][ny] == 0: 
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    cnt += 1

    return cnt

for r in range(row):
    for c in range(col):
        if grid[r][c] == 0 and not visited[r][c]:
            res = FindAreaBFS(r,c)
            area.append(res)

area.sort()

result = ' '.join(map(str,area))
print(len(area))
print(result)
