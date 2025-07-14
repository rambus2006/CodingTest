from collections import defaultdict,deque

# 노드 개수(컴퓨터개수) 입력받기 
n = int(input())
# 간선의 개수 입력받기
trunk = int(input())
# 그래프 선언
graph = defaultdict(list)

# 그래프 생성 
for i in range(trunk):
    key,num = map(int,input().split())
    graph[key].append(num)
    graph[num].append(key)
# print(graph)

# visited 배열(방문을 확인하는 배열 만들기)
visited = [False] * (n + 1)

def bfs(start,graph,visited):
    # 루프 돌기 전 
    queue = deque([start])
    visited[start] = True

    # 루프 돌기 후 
    while queue: 
        node = queue.popleft()
        # print(node,"방문 완료")

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

bfs(1,graph,visited)
vircnt = 0
for cnt in range(2,n+1):
    if visited[cnt] == True:
        vircnt += 1
print(vircnt)