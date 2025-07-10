from collections import deque
import sys

# 입력 
#M : 상자의 가로 / N : 상자의 세로 
# graph
M,N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

# 방향 (상,하,좌,우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# BFS용 큐 
queue = deque()

# 익은 토마토들을 큐에 먼저 넣음(여러개 시작점)
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1: 
            queue.append((i,j))

# BFS 시작 
while queue : 
    x,y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M: 
            if arr[nx][ny] == 0: 
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx,ny))

result = 0 
for row in arr: 
    if 0 in row: 
        print(-1)
        sys.exit(0)
    result = max(result,max(row))

print(result - 1)