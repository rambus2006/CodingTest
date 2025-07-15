from collections import defaultdict,deque

res = []
# 입력받기 
while True: 
    w,h = map(int,input().split())
    if w == 0 and h == 0: 
        break
    grid = [list(map(int,input().split())) for _ in range(h)]
    
    visited = [[False] * w for _ in range(h)]

    dx = [1,1,0,-1,-1,-1,0,1]
    dy = [0,-1,-1,-1,0,1,1,1]

    def bfs(start_x,start_y):
        queue = deque()
        queue.append((start_x,start_y))

        while queue: 
            x,y = queue.popleft()

            for dir in range(8): 
                nx = x + dx[dir]
                ny = y + dy[dir]
                # 만약 방문하지 않았고 1이라면 
                if 0 <= nx < h and 0 <= ny < w:
                    if not visited[nx][ny] and grid[nx][ny] == 1:
                        visited[nx][ny] = True
                        queue.append((nx,ny))
        return 
    cnt = 0
    for row in range(h):
        for col in range(w):
            if grid[row][col] == 1 and not visited[row][col]:
                island = bfs(row,col)
                cnt +=1
    res.append(str(cnt))
print('\n'.join(res))

