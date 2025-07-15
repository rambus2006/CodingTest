from collections import deque

# 입력 받기 
# 테스트케이스 개수 
# 체스판 한변의 길이 
# 나이트가 현재 있는 칸의 좌표 
# 나이트가 가려고 하는 칸의 좌표
t = int(input())
resultarr = []

# 테스트 케이스만큼 반복 
for tc in range(1,t+1):
    # 체스판 한변의 길이
    n = int(input())
    # 나이트 시작점 
    start = list(map(int,input().split()))
    # 나이트 끝점 
    end = list(map(int,input().split())) 
    # 방문 여부를 체크하는 배열 
    visited = [[False] * n for _ in range(n)]
    # 델타 탐색을 위한 배열(8번)
    dx = [2,1,-1,-2,-2,-1,1,2]
    dy = [-1,-2,-2,-1,1,2,2,1]

    # bfs 함수 
    def bfs(start_x,start_y,depth):
        # 큐 생성 
        queue = deque()
        # 나이트가 몇번 이동하는지 세는 배열 
        move = 0
        # 처음에 시작 위치 넣어주기 
        queue.append((start_x,start_y,move))
        
        # 큐에 값이 있는동안 반복 
        while queue: 
            # x,y를 queue에서 빼오기 
            x,y,move = queue.popleft()
            if x == end[0] and y == end[1]:
                return (x,y,move)
            # 8방향 탐색 
            for dir in range(8):
                nx = x + dx[dir]
                ny = y + dy[dir]

                # 탐색하게 될 곳이 범위 안에 있고 
                if 0 <= nx < n and 0 <= ny < n:
                    # 아직 방문하지 않았다면 
                    if not visited[nx][ny]:
                        # else: 
                        visited[nx][ny] = True
                        # 한번 이동할 때마다 +1 
                        queue.append((nx,ny,move+1))

    # bfs 함수 호출  +  나이트가 현재 있는 칸 
    res = bfs(start[0],start[1],0)
    # print(res[2])
    resultarr.append(str(res[2]))
print('\n'.join(resultarr))
