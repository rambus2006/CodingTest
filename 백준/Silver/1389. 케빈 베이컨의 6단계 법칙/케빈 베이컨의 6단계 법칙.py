from collections import deque,defaultdict


# default dict 선언 
graph = defaultdict(list)
# 입력값 받기 
n,m = map(int,input().split())

# 양 방향 그래프 생성
for i in range(m):
    key,num = map(int,input().split())
    graph[key].append(num)
    graph[num].append(key)


# bfs
# visited 배열 

keys = [numbers for numbers in range(1,n+1)]
results = [0] * (n + 1)

def bfs(startnum):
    # start_x,start_y 를 큐에 넣기 
    queue = deque([(startnum,0)])
    visited[startnum] = True
    movesum = 0

    # while True 문 
    while queue:
        node,move = queue.popleft()
        
        for neighbor in graph[node]:
            if not visited[neighbor]: 
                queue.append((neighbor,move+1))
                visited[neighbor] = True
                movesum += (move + 1)
    return movesum
for key in keys:
    visited = [False] * (n+1)
    results[key] = bfs(key)

print(results.index(min(results[1:])))