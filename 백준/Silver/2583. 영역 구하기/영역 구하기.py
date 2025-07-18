from collections import deque

row,col,k = map(int,input().split())
grid = [[0] * (col) for _ in range(row)]
queue = deque()
for _ in range(k):
    start_x,start_y,end_x,end_y = map(int,input().split())
    queue.append((start_x,start_y,end_x,end_y))
    
    for y in range(start_y,end_y):
        for x in range(start_x,end_x):
            grid[row-y-1][x] += 1
# 여기까지는 잘 만듬 


dx = [0,0,-1,1]
dy = [-1,1,0,0]
visited = [[False] * col for _ in range(row)]
area = []

# bfs 
def FindAreaBFS(st_y,st_x):
    queue = deque()
    queue.append((st_y,st_x))
    cnt = 1
    visited[st_y][st_x] = True
    while queue:
        y,x = queue.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if 0 <= ny < row and 0 <= nx < col and not visited[ny][nx]:
                if grid[ny][nx] == 0: 
                    visited[ny][nx] = True
                    queue.append((ny,nx))
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
