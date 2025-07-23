from collections import deque,defaultdict
# 제발 주석을 달아두렴 과거의 민서야.
graph = defaultdict(list)
n = int(input())
m = int(input())

# 친구끼리의 간선 그래프 생성 
for i in range(m):
    key,num = map(int,input().split())
    graph[key].append(num)
    graph[num].append(key)

keys = [numbers for numbers in range(1,n+1)]
results = [0] * (n + 1)
# bfs를 통해 모든 간선이 연결되어 있는 친구만 초대 
def bfs(startnum):
    queue = deque([(startnum,0)])
    visited[startnum] = True
    invitedfriends = 0
    if startnum != 1:
        return invitedfriends
    while queue: 
        node,move = queue.popleft()

        for neighbor in graph[node]:
            if not visited[neighbor] and move < 2:
                queue.append((neighbor,move + 1))
                visited[neighbor] = True
                invitedfriends += 1
    return invitedfriends

for key in range(1,3):
    visited = [False] * (n+1)
    results[key] = bfs(key)
# print(results)
print(max(results[1:]))